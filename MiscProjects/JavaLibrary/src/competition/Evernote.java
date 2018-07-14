package competition;
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Evernote{

    public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String command;
            HashMap<String,String> note = new HashMap<String,String>();
            
            while(true)
            {
              command = br.readLine();
              // Work on command 
              if(command == null||command.equalsIgnoreCase(""))
            	  break;
              else if(command.equals("create")){
            	  String newNote = "";
            	  String newLine = "";
            	  do{
            		  newLine = br.readLine();
            		  newNote += newLine+"\n";
            	  }while(!newLine.equalsIgnoreCase("</note>"));
              }
              else if(command.equalsIgnoreCase("search")){
            	  
              }
              else if(command.equalsIgnoreCase("delete")){
            	  
              }
              else if(command.equals("update")){
            	  
              }
            }
    }
}

class Note{
	String guid, date, content;
	ArrayList<String> tags;
	public Note(String guid, String date, String content, ArrayList<String> tags){
		this.guid = guid;
		this.date = date;
		this.content = content;
		this.tags = tags;
	}
}