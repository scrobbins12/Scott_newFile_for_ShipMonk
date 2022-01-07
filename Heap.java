// Scott Robbins & CJ Duncan
// Final Project
// Stock Simulator Game
// This game uses random values to make imagined stocks fluctuate
// The player is prompted to choose a different stock each quarter,
// The player wins when they earn $8k

import java.lang.Math;   
import java.util.Scanner;
//lets us use randomness to simulate stock market
//Note: heapArray @ [0] == null
public class Heap {
	
	public HeapNode [] heapArray;
	protected int size = 0;
	protected int capacity = 6;
	// small array because only 5 stocks
		
	protected static class HeapNode {
		
		protected double key;
		protected String value;
		protected double price;
		// our nodes have 3 elements instead of 2
		
		public HeapNode(double k, String v, double p) {
			key = k;
			value = v;
			price = p;
		}
		
		public double getKey() { return key;}
		public String getElement() { return value;}
		public double getPrice() { return price;}
		
		public void setKey(double k) { key = k;}
		public void setElement(String s) { value = s;}
		public void setPrice(double p) { price = p;}
		
	}
		
		
	public Heap() {
		heapArray = new HeapNode[capacity];
	}
	
	public int size() { return size;}
	
	public double trade(int x){
		return heapArray[x].getPrice();
	}
	
	public HeapNode reStock(){
		// this multiplies stock prices my either 0.x or 1.x (x being volatility percentage)
		for (int i = 1; i <= size; i++) {
			double coinFlip=Math.random();
			// half and half chance value goes either up or down
			if(coinFlip>=0.5){
				double lastQuart = (heapArray[i].getKey()/100)*heapArray[i].getPrice()+heapArray[i].getPrice();
				heapArray[i].setPrice(lastQuart);
				upHeap(i);
			}
			if(coinFlip<0.5){
				double lastQuart = heapArray[i].getPrice()-(heapArray[i].getKey()/100)*heapArray[i].getPrice();
				heapArray[i].setPrice(lastQuart);
				upHeap(i);
			}
		}
		return null;
	}
	
	public void insert(double k, String v, double p) {
		//function adds a new stock
		HeapNode node = new HeapNode(k, v,p);
		heapArray[++size] = node;
		upHeap(size);		
	}
	
	public void swap(int x, int y) {
		//swaps two nodes
		HeapNode tempNode = heapArray[x];
		heapArray[x] = heapArray[y];
		heapArray[y] = tempNode;
		
	}
		
	public void upHeap(int v) {
		
		// compare v's key to parent's key
		// check if v has a parent
		if (v == 1)		// root. no more to go
			return;
		
		int u = (int)(v / 2);	// parent index
		if (heapArray[v].getKey() < heapArray[u].getKey() ) {
			swap(u, v);
			upHeap(u);	
		}
		// else: do nothing
	}
	
	public String toString() {
		// format of how our nodes will look when we write them
		String outStr = "";
		
		for (int i=1; i<size+1; i++) {
			outStr += i +" "+heapArray[i].getElement() + " "+ "Price:$"+ heapArray[i].getPrice() + " " + "Volatility:" + heapArray[i].getKey() + "%\n";
		}
		
		return outStr;
	}
	
	public static void main(String[] args) {
		Scanner scanner=new Scanner (System.in);
		// scanner for taking user input
		boolean running=true;
		//tracks that they want to play simulator
		int quarter=0;
		// amount of quarters works like a score
		double goal = 8000;
		//threshold at which game is won
		int yearsLoan= 0;
		// counter for if they choose to play a new game
		double coupon = 0;
		//money owed if they choose to play new game
		Heap h = new Heap();
		double wallet = 6000;
		// money that the player starts with
		double[] volat = new double[5];
		//assign random volatility to each stock
		for (int i = 0; i < 5; i++) {
			double rando= Math.random()*100;
			int rand= (int)rando;
			volat[i]=rand;
		}
		int choice = 0;
		// holder for when user picks a stock to buy
		h.insert(volat[0], "Chunkbook", 287.52);
		h.insert(volat[1], "Peach", 123.08);
		h.insert(volat[2], "Sahara", 3203.53);
		h.insert(volat[3], "Webscene", 503.38);
		h.insert(volat[4], "Million", 1824.97);
		// 5 stocks
		System.out.println("Welcome to Stock Simulator!");
		System.out.println("Earn $8,000 to win");
		System.out.println("Press 'q' to quit \n");
		// intro message
		//everything below will be in a repeating while loop
		while (running == true){
			System.out.println("Funds: $"+wallet+"\n");
			System.out.println(h);
			System.out.println("Which number stock would you like to buy?");
			
			boolean questioning =true;
			while (questioning==true){
				// This loop asks for user input until an approved answer is given
				String instr =scanner.nextLine();
				if (instr.compareTo("q")==0){
					// q to quit
					running=false;
				}
				else{
					if (instr.compareTo("1")==0){
						choice = 1;
						questioning = false;
					}
					else if (instr.compareTo("2")==0){
						choice = 2;
						questioning = false;
					}
					else if (instr.compareTo("3")==0){
						choice = 3;
						questioning = false;
					}
					else if (instr.compareTo("4")==0){
						choice = 4;
						questioning = false;
					}
					else if (instr.compareTo("5")==0){
						choice = 5;
						questioning = false;
					}
					else{
						System.out.println("Invalid input: Type again");
						questioning = true;
					}
				}
			}	
			// stock chosen dictated by user choice
			wallet = wallet - h.trade(choice);
			System.out.println("You bought a stock in "+ h.heapArray[choice].getElement()+"\n");
			//buy option takes money from wallet to buy stock
			h.reStock();
			//function makes stock value change for each quarter
			System.out.println("A new quarter has arrived; stock values fluctuated \n");
			// print statement saying money has gotten back
			wallet = wallet + h.trade(choice);
			// adds new value back to wallet
			
			if (yearsLoan >= 1){
				wallet-=coupon;
				System.out.println("Your debts are due. Your payment was removed from your wallet");
				System.out.println("-"+coupon);
				yearsLoan-=1;
				if (yearsLoan==0){
					System.out.println("Debt Paid in full!");
				}
				else{
					System.out.println("You have "+yearsLoan+" quarters left on your debt.");

				}
			}
			
			if (wallet>=goal){
				System.out.println("You Win!");
				System.out.println("It took "+ quarter+ " quarters");
				running= false;
			}
			else if (wallet<=0){
				questioning= true;
				while (questioning==true){
					System.out.println("Sorry, You're Bankrupt!");
					System.out.println("Do you want to take out a loan at a 10% interest quarterly? (y/n)");
					String loanstr =scanner.nextLine();
					if (loanstr.compareTo("n") ==0){
						System.out.println("You lasted "+ quarter+ " quarters");
						System.out.println("Thank you for playing");
						return;
					}
					if (loanstr.compareTo("q") ==0){
						System.out.println("You lasted "+ quarter+ " quarters");
						System.out.println("Thank you for playing");
						return;
					}
					else{
						if (loanstr.compareTo("y")==0){
							System.out.println("What is the value of your withdrawn loan?");
							System.out.println("(Enter value without symbols or punctuation marks)");
							String debtstr =scanner.nextLine();
							wallet+= Double.parseDouble(debtstr);
							coupon = 0.1 * Double.parseDouble(debtstr);
							//quarterly payments of 10?
							yearsLoan += 11;
							// pay 110% total in interest
							goal= 1.33*wallet;
							// goal shifts to match money amount
							questioning = false;
						}
						else{
							System.out.println("Invalid input: Type again");
							questioning = true;
						}
					}
				}
			}
		quarter++;
		}
		
	}	
}