import java.io.File;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
/* 
 * Quora's Nearby Coding Challenge
 */
public class QuoraChallenge {
		
	public class Position{
		double x,y;
		public Position(double x, double y){
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		HashMap<Integer, Position> topicInfo = new HashMap<Integer, Position>(); 
		HashMap<Integer,ArrayList<Integer>> topicQues = new HashMap<Integer,ArrayList<Integer>>();
		Scanner console = new Scanner(new File(".\\src\\input"));//new File(".\\src\\input")
		
		String[] firstLine = (console.nextLine()).split(" ");
		int T = Integer.parseInt(firstLine[0]);
		int Q = Integer.parseInt(firstLine[1]);
		int N = Integer.parseInt(firstLine[2]);
		
		//Topic Info
		for(int i=0; i<T ; i++){
			String[] topicLine = (console.nextLine()).split(" ");
			int topicID = Integer.parseInt(topicLine[0]);
			double xCoord = Double.parseDouble(topicLine[1]);
			double yCoord = Double.parseDouble(topicLine[2]);
			Position curPos = new QuoraChallenge().new Position(xCoord, yCoord);
			topicInfo.put(topicID, curPos);
		}
		
		//int[][] mat = new int[5][6];//{{1,2,3,4,5}, {3,4,5,6,7},{3,4,5,6,7},{3,4,5,6,7},{3,4,5,6,7},{3,4,5,6,7}};
		//System.out.println(mat[1][3]);
		//Topic Ques
		for(int i=0 ; i<Q ; i++){
			String[] quesLine = console.nextLine().split(" ");
			int quesID = Integer.parseInt(quesLine[0]);
			int nofTopics = Integer.parseInt(quesLine[1]);
			//int[] topicList = new int[nofTopics];
			for(int j=0; j<nofTopics ; j++){
				
				int topicID = Integer.parseInt(quesLine[j+2]);
				//topicList[j] = topicID;
				if(topicQues.containsKey(topicID)){
					topicQues.get(topicID).add(quesID);
				}
				else{
					ArrayList<Integer> quesList = new ArrayList<Integer>();
					quesList.add(quesID);
					topicQues.put(topicID, quesList);
				}
			}
			//quesInfo.put(quesID, topicList);
		}
		//String dummy = console.nextLine();
		List<Integer> listIDs = new ArrayList<Integer>();
		//Query Processing
		for(int i=0 ; i<N ; i++){
			String[] queryLine = (console.nextLine()).split(" ");
			String queryType = queryLine[0];
			int nofEnt = Integer.parseInt(queryLine[1]);
			double xCoord = Double.parseDouble(queryLine[2]);
			double yCoord = Double.parseDouble(queryLine[3]);
			Position queryPos = new QuoraChallenge().new Position(xCoord, yCoord);
			
			DecimalFormat df = new DecimalFormat("0.000");
			Object[] keys = topicInfo.keySet().toArray();
			Map<Double,ArrayList<Integer>> topicDist = new TreeMap<Double,ArrayList<Integer>>();
			for(int j=0; j<topicInfo.size() ; j++){
				double distance = getDistance(queryPos,topicInfo.get(keys[j]));
				distance = Double.parseDouble(df.format(distance));
				if(topicDist.containsKey(distance)){
					topicDist.get(distance).add((Integer) keys[j]);
				}
				else{
					ArrayList<Integer> topArray = new ArrayList<Integer>();
					topArray.add((Integer) keys[j]);
					topicDist.put(distance, topArray);
				}
			}
			
			if(queryType.equalsIgnoreCase("t")){
				listIDs = getTopicIDs(nofEnt, topicDist);
			}
			
			else if(queryType.equalsIgnoreCase("q")){
				listIDs = getQuesIDs(nofEnt, topicDist, topicQues);
			}
			//Iterator<Integer> printIter = listIDs.iterator();
			
			for(int l=0 ; l<listIDs.size() ; l++){
				System.out.print(listIDs.get(l)+" ");
			}
			System.out.println();
		}
		console.close();
	}
	
	public static List<Integer> getTopicIDs(int nofEnts, Map<Double,ArrayList<Integer>> topicDist){
		
		Iterator<Entry<Double, ArrayList<Integer>>> entIter = topicDist.entrySet().iterator();
		//ArrayList<Integer> entList = new ArrayList<Integer>();
		Set<Integer> entSet = new LinkedHashSet<Integer>();
		List<Integer> cappedEntList = new ArrayList<Integer>();
		while(entIter.hasNext()){
			Entry<Double,ArrayList<Integer>> curEntry = entIter.next();
			Collections.sort(curEntry.getValue());
			//Collections.reverse(curEntry.getValue());
			entSet.addAll(curEntry.getValue());
		}
		cappedEntList.addAll(entSet);
		if(cappedEntList.size()>nofEnts){
			cappedEntList = cappedEntList.subList(0, nofEnts);
		}
		
		//System.out.println(topicDist.entrySet().iterator().next().getValue());
		return cappedEntList;
	}
	
	public static List<Integer> getQuesIDs(int nofEnts, Map<Double,ArrayList<Integer>> topicDist, HashMap<Integer,ArrayList<Integer>> topicQues){

		Iterator<Entry<Double, ArrayList<Integer>>> entIter = topicDist.entrySet().iterator();
		Set<Integer> orderTopicSet = new LinkedHashSet<Integer>();
		while(entIter.hasNext()){
			Entry<Double,ArrayList<Integer>> curEntry = entIter.next();
			
			Collections.sort(curEntry.getValue());
			//Collections.reverse(curEntry.getValue());
			orderTopicSet.addAll(curEntry.getValue());
			}
		List<Integer> orderTopicList = new ArrayList<Integer>();
		orderTopicList.addAll(orderTopicSet);
		
		Set<Integer> entSet = new LinkedHashSet<Integer>();
		List<Integer> cappedEntList = new ArrayList<Integer>();
		
		for(int k=0 ; k<orderTopicList.size() ; k++){
			if(topicQues.containsKey(orderTopicList.get(k))){
				Collections.sort(topicQues.get(orderTopicList.get(k)));
				Collections.reverse(topicQues.get(orderTopicList.get(k)));
				entSet.addAll(topicQues.get(orderTopicList.get(k)));
			}		
		}
		cappedEntList.addAll(entSet);
		if(cappedEntList.size()>nofEnts){
			cappedEntList = cappedEntList.subList(0, nofEnts);
		}
	
		//System.out.println(topicDist.entrySet().iterator().next().getValue());
		return cappedEntList;
	}
	
	public static double getDistance(Position pos1, Position pos2){
		double distance = Math.sqrt((Math.pow((pos1.x-pos2.x),2)+Math.pow((pos1.x-pos2.x),2)));
		return distance;
	}
}
