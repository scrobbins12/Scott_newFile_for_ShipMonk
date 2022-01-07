import java.util.StringTokenizer;//must import the scanner and tokenizer because they are not in the folder
import java.util.Scanner;
public class postFixCalc {
    public postFixCalc(String userInput){//userInput is the string that is the string
        // that is then broken down to opArray and numsArray (opArray holds operators and numsArray holds the numbers inputted)
		StringTokenizer st = new StringTokenizer(userInput);
        while (st.hasMoreTokens()) {//the has more tokens will continue to build the opArray and
            // numsArray until everything the user inputted is properly inputted
			// get one token (separated by whitespace)
			String str = st.nextToken();
			if (isOperator(str)==0) {
                int value = Integer.parseInt(str);//string must be parsed into number
                numsArray.push(value);//add it to end of arrayStack
            }
            else{
                opArray.push(str);
			}
		}
    }
    ArrayStack numsArray=new ArrayStack();//initliaze these using arrayStack
    ArrayStack opArray=new ArrayStack();
    public static int isOperator(String str){//isoperator checks if it is an operator or integer
        //depending on type of operator, a different number is returned
        //if it is a number, not an operator, then I return 0
        if (str.compareTo("+")==0)
            return 1;
        if (str.compareTo("-")==0)
            return 2;
        if (str.compareTo("*")==0)
            return 3;
        if (str.compareTo("/")==0)
            return 4;
        return 0;
    }
    public Double calcIt() {
        String numString;//number read in from user as a string
        String str; //string that holds the operator
        Double num;//numString after being parsed
        if ((opArray.size()+1)!=numsArray.size())//bonus part/there should always be 1 more number than numbers inputted
        //so if it is not the case, the user entered an invalid expression, so this is why 
        //the whole thing would break as I would simply return null
            return null;
        Double result=new Double(numsArray.pop().toString());
        int iteration=numsArray.size();
        for (int i=0;i<iteration;i++){//loop runs however many times the number of numbers inputted
            numString=numsArray.pop().toString();//each time, numString stores the number as a string
            num=new Double(numString);//numString parsed (changed to number form)
            str=opArray.pop().toString();//str is the string of operator
            if (isOperator(str)==1)//the following calculations are performed based on the type of operator it is
                result=result+num;
            else if (isOperator(str)==2)
                result=result-num;
            else if (isOperator(str)==3)
                result=result*num;
            else if (isOperator(str)==4)
                result=result/num;
        }
        return result;//the calcIt method returns the result if valid expression
    }
}