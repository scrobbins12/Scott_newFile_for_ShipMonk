public class ordArraytester {
public static void main (String [] args){
    ordArray b= new ordArray(10);
        b.insert(4);
        b.insert(2);
        b.insert(3);
        b.insert(100);
        b.insert(48);
        b.display();
        System.out.println(b.find(7));
        System.out.println(b.find(4));
        b.display();
        b.remove(2);
        b.display();
    }
}