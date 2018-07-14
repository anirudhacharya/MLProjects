package webStuff;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;

public class tClient {
	public static void main(String[] args){
		Socket client;
		try{
			client = new Socket("yahoo.com",80);
			PrintWriter out = new PrintWriter(client.getOutputStream(), true);
			BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
			
			out.println("GET /index.jsp HTTP/1.1");
			out.println("Host: localhost:8080");
			out.println("Connection: Close");
			out.println();

			// read the response
			boolean loop    = true;
			StringBuffer sb = new StringBuffer(8096);

			while (loop) {
			    if ( in.ready() ) {
			        int i=0;
			        while (i!=-1) {
			            i = in.read();
			            sb.append((char) i);
			        }
			        loop = false;
			    }
			    //Thread.currentThread().sleep(50);
			}

			// display the response to the out console
			System.out.println(sb.toString());
			client.close();
		}
		catch(Exception e){
			System.out.println(e);
		}
	}
}
