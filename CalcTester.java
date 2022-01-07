import java.util.Scanner;//must import again because I scanner and tokenizer
import java.util.StringTokenizer;
public class CalcTester{
    public static void main(String args []) {
		// scanner for user input here/system.in takes in what what was put into input box from user
		Scanner scanner = new Scanner(System.in);
		// will run infinite loop & take user input until 'quit' command
		boolean running=true;//initliaze running equal to true because otherwise the loop below will never run
		System.out.println("*** type quit and enter to exit the program ***");
		while(running) {//while user is still entering numbers and not quiting
			System.out.print("type expression > ");
			String inStr = scanner.nextLine();//reads each thing typed in and stores it
			//on the given iteration as inStr
			// if it returns 0 when compareTo is used, it means the string is identical to the given one
			if (inStr.compareTo("quit")==0) {
				running = false;	// this will terminate while loop
				System.out.println("Good-Bye!");
			}
			else {
				postFixCalc a=new postFixCalc(inStr);//creating instance of postFix Calc and passing the inStr into it each time
				Double result=a.calcIt();//this returns the result or null if invalid
				System.out.println(result);//this prints result
			}
		}
	}
}