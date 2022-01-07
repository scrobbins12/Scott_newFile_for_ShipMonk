/**
 * COM212 Data Structures
 * Stack implementation with Array
 */

public class ArrayStack<E> {
	private int capacity = 100;//capacity is set/meaning the lenght of the ArrayStack is set to 100 always
	public E[] elements;//E means all types can be stored
	private int t = -1;
	
	public ArrayStack() {
		elements = (E[])(new Object[capacity]);//constructor method
	}
	
	public int size() { return t+1; }//size is index of each element on ArrayStack
	public boolean isEmpty() { return t==-1;}//t is intiliazed at -1, and each new element
	//t increases by 1, so when t=-1, the ArrayStack is empty
	
	public void push(E e) {
		if (size() == elements.length) {//if arrayStack is full, cannot add and error mesage prints out
			System.out.println("Error: stack is full.");
			return;
		}
		
		elements[++t] = e;//t goes up by 1 each new element added and element is added at the new spot each time
	}
	
	public E pop() {
		// empty?
		if (isEmpty()) {//if arrayStack is empty, cannot remove, so error message
			System.out.println("Error: stack is empty.");
			return null;
		}
		E val = elements[t];
		elements[t] = null;
		t--;//each removing, size goes down by 1 and the new last spot goes down by 1
		return val;
	}
	
	public E top() {
		// empty?//returns last element unless empty in which there is none
		if (isEmpty()) {
			System.out.println("Error: stack is empty.");
			return null;
		}
		
		return elements[t];
	}
	
	public String toString() {
		
		//this method simply makes the element as a string
		if (isEmpty())//can't return any elements if no elements are in the ArrayStack
			return "The list is empty";
		
		String outstr = "Elements in the stack:\n";
		for (int i=0; i<t+1; i++) {
			outstr = outstr + elements[i].toString() + "\n";	
		}
		
		return outstr;	
	}
}
	
	