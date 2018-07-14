package threads.streamGobbler;
import java.util.*;
import java.io.*;

public class StreamGobbler extends Thread{
	InputStream is;
	String type;
	OutputStream os;
	
	StreamGobbler(InputStream is, String type){
		this(is,type,null);
	}

	public StreamGobbler(InputStream is, String type, OutputStream redirect) {
		// TODO Auto-generated constructor stub
		this.is= is;
		this.type = type;
		this.os = redirect;
	}
	
	public void run(){
		try{
			PrintWriter pw = null;
			if(os != null)
				pw = new PrintWriter(os);
				
			InputStreamReader isr = new InputStreamReader(is);
			BufferedReader br = new BufferedReader(isr);
			BufferedWriter output = new BufferedWriter(new FileWriter(new File("E:/Dev/Java/Workspace/JavaLibrary/src/threads/streamGobbler/queries.txt")));

			String line = null;
			while((line=br.readLine()) != null){
				if (pw!=null)
					pw.println(line);
				output.write(line+" ");
			output.write("\n");
			}
			output.close();
			if(pw!=null)
				pw.flush();
			}
		
			catch(IOException ioe){
				ioe.printStackTrace();
			}
		}
	}
