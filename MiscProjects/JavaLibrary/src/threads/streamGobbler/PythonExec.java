package threads.streamGobbler;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class PythonExec {

	public static void main(String[] args) throws IOException, InterruptedException {
			
		String sentence = "Jane gave Joan candy because she was hungry";
		Runtime rt = Runtime.getRuntime();
		Process pr = null;
		try {
			pr = rt.exec("cmd.exe /c python E:/Dev/Java/Workspace/JavaLibrary/src/threads/streamGobbler/QueryTerms.py "+sentence);
			//System.out.println(pr.waitFor());
			
			StreamGobbler errorGobbler = new StreamGobbler(pr.getErrorStream(), "ERROR");
			
			StreamGobbler outputGobbler = new StreamGobbler(pr.getInputStream(), "");
			
			errorGobbler.start();
			outputGobbler.start();
			
			int exitVal = pr.waitFor();
			//System.out.println("Exit Value: "+exitVal);
			
		} catch (Throwable t) {
			// TODO Auto-generated catch block
			t.printStackTrace();
		}	
		
		BufferedReader br = new BufferedReader(new FileReader("./src/queries.txt"));
		String t = "";
		while((t=br.readLine()) != null){
			System.out.println(t);
		}
	}
}
