package threads.streamGobbler;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Runtime rt = Runtime.getRuntime();
		Process pr = null;
		
		try {
			
			pr = rt.exec("cmd.exe /c python E:/Dev/Java/Workspace/JavaLibrary/src/threads/streamGobbler/QueryTerms.py");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		BufferedReader br = new BufferedReader(new InputStreamReader(pr.getInputStream()));
		String line = null;
		while((line=br.readLine())!=null)
			System.out.println(line);
	}
}
