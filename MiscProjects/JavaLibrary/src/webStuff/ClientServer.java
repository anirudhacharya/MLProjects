package webStuff;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;


public class ClientServer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class server implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		ServerSocket ser = null;
		System.out.println("Opening server connection at port 85");
		try {
			ser = new ServerSocket(85);
			
		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			Socket remote = ser.accept();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}
}

class client implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		
	}
	
}