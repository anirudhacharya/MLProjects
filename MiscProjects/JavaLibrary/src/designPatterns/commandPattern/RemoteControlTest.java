package designPatterns.commandPattern;

public class RemoteControlTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SimpleRemoteControl rc = new SimpleRemoteControl();
		Light light = new Light();
		LightOnCommand lightOn = new LightOnCommand(light);
		
		rc.setCommand(lightOn);
	}

}
