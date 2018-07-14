package designPatterns.commandPattern;

public class SimpleRemoteControl {
	private Command slot1;
	
	public SimpleRemoteControl(){
	}
	
	public void setCommand(Command command1){
		slot1 = command1;
	}
	
	public void buttonPressed(){
		slot1.execute();
	}
}
