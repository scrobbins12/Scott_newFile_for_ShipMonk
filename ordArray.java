public class ordArray {
    private int [] array;//declaring type of variables
    private int n;
    public ordArray(int maxsize){//maxsize is array length
        array=new int[maxsize];
        n=0;//n is just numbers I care about in the array//TA helped me understand what n variable is 
    }
    public void sort(){//bubble sort
        int orgnum;//if iteration of array is greater than the one
        //after it, then I swap them because the array is sorted from low to high
        for (int i=0; i<n-1;i++){
            if (array[i]>array[i+1]){
                orgnum=array[i];//orngum stores original variable in array[i] 
        //so array[i] value is not overwritten when swapping
                array[i]=array[i+1];
                array[i+1]=orgnum;
            }
        }
    }
    public void Sort(){//sort method for insertion sort
        int insertPos;//position the number will go when sorting
        for (int i=0; i<(n-1);i++){
            insertPos=i;//=insertposition/intilaize it at i because that 
            //is where insertposition of variable is at first
            while (array[i]<arrray[i+1]){//finding insert position
                insertPos++;
            }
            for (int j=insertPos; j>0;j--){//shift all 1 to left before insertPos to make space for it
                array[j-1]=array[j];
            }
            array[insertPos]=array[i];
        }
    } 
    public boolean remove(int value){
        for (int i=0; i<n; i++){//looping through each integer I care about
            if (array[i]==value){
                for (int j=i; j<n-1; j++){
                    array[j]=array[j+1];//simply move each one after array[i] to the left
                    //this overwrites variable I want to get rid of
                    //but keeps the others to the left
                }
                n--;//one fewer variable I care about because one was just removed
                return true;
            }
        }
        return false;//after iterating through each integer we care about
        //if not found, return false to indiate variable was not in array
    }
    public boolean find(int value){//finding if value is in array using binary search
        int start=0;
        int end=n-1;//indices mean last n will array[n-1] and 
        //first will be array[0], so start=0
        int mid;
        while (start<=end){//as long as end is not negative, 
            //then keep on running loop to find value by continously changing mid
            mid=(start+end)/2;
            if (array[mid]<value){
                start=mid+1;
            }
            else if (array[mid]>value){
                end=mid-1;
            }
            else if (array[mid]==value){
                return true;
            }
        }
        return false;//if not found
    }
    public void insert(int value){//value is just value that we want to insert
        int i=0;//i is the index I will insert it at
        if (n!=0){
            if (value>array[n-1]){
                array[n]=value;
                n++;
                return;
            }
            else{
                while (array[i]<value){
                    i++;//keep on moving insert position over 1 if it is less than the value
                    //in other words, I add 1 to i to do this
                }
                for (int j=n; j>i; j--){//shift all integers to the 
                    //right that are bigger than i
                    array[j]=array[j-1];//by decremting and 
                    //looping backwards, array[j] is not overwritten
                }
            }
        }
        array[i]=value;//this is here because in case the first integer is being inserted
        //the if clause up top will be skipped but it also allows the array[i] 
        //to be equal to value(number I am going to insert) after i was adjusted 
        n++;//amount of integers I care about now is one more after inserting one number
    }
    public void display(){
        if (n<1){
            System.out.println("Empty");
        }
        else{
            for (int i=0; i<n;i++){
                System.out.println(array[i]);
            }
        }
    }
}