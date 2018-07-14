package webStuff;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;


public class WebServer{
	static ServerSocket sev = null;
	static Socket remote = null;
	static int listenPort = 80;
	
	public static void main(String[] args) throws IOException{
				
		System.out.println("Web Server starting at port "+listenPort);
		try {
			sev = new ServerSocket(listenPort, 100, InetAddress.getByName("127.0.0.1"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		while(true){
		try {
			
			System.out.println("Waiting for Connection...");
			remote = sev.accept();
			PrintWriter out = new PrintWriter(remote.getOutputStream());
			BufferedReader in = new BufferedReader(new InputStreamReader(remote.getInputStream()));
			
			boolean loop = true;
			
			while(true){
				String str = in.readLine();
				if(str==null)
					break;
				else if(str.equals(""))
					break;
				else
					System.out.println(str);
			}
				
			out.println("HTTP/1.0 200 OK");
		    out.println("Content-Type: text/html");
		    out.println("Server: Bot");
		    // this blank line signals the end of the headers
		    out.println("");
		    // Send the HTML page
		    out.println("<H1>Welcome to the Ultra Mini-WebServer</H2>");
		    out.flush();
		    //System.out.println("Connection Success...");		
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		finally{
			remote.close();
		}
		}
	}

	private static void start() {
		// TODO Auto-generated method stub
		
	}
}