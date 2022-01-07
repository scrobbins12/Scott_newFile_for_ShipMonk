public class myArrayTest {
    public static void main (String [] args){
        MyArray a= new MyArray(10);
        a.insert(5);
        a.insert(2);
        a.insert(3);
        a.insert(4);
        a.insert(5);
        a.display();
        System.out.println(a.findMax());
        System.out.println(a.findMin());
        System.out.println(a.find(4));
        System.out.println(a.find(7));
        System.out.println(a.total());
        System.out.println(a.average());
        a.remove(3);
        a.display();
        a.removeMax();
        a.removeMin();
        a.reverseArray();
        a.display();
        System.out.println(a.allDistinct());
    }
}
//recieved help on this project from TAs, Jhonny, and Professor Douglass
//was significantly helped with some lines of code by people above