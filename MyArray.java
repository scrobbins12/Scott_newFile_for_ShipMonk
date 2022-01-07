public class MyArray{//the MyArray class
    public int[] array;
//I must declare the type of variable each one is before I use them
    private int n;
    public MyArray(int size){
    //int size is just the length of the array
    //in java, the array size is fixed, so we should make it bigger and just change n
    //n is our pointer
        array=new int [size];
        n=0;
    }
        public void insert(int value){
            array[n]=value;//for n, where I want to insert, this
            // is where I put the integer in the array
            n++;
            //I add 1 to n each time because I just insert as given the order by the user
            //it is not sorted
        }
        public int findMax(){// find the max in this
            if (array.length==0){//if array is empty, return -1 to indicate there is no max
                return -1;}
            int max=array[0];//intitialize max to 0 and check each other integer in array
            //and keep on comparing to finally find the actual max
            //I have the max after comparing all of the values in the array to the max in each iteration
            for (int i=0; i<array.length;i++){
                if (array[i]>max){
                    max=array[i];
                }
            }
            return max;
        }
        public int findMin(){//same exact concept as findMax, but I am just finding to see the min
            //so I code to see the smallest value instead of the greatest one
            if (n==0){
                return -1;
            }
            int min=array[0];
            for (int i=0; i<n;i++){
                if (array[i]<min){
                    min=array[i];
                 }
            }
            return min;
        }
        public boolean find(int num){// not using binary search for this one although
            //I use it for ordArray
            //for this one, I just loop through each integer in the array and
            // return true if I find it in the iteration
            // once I return anything, the whole method breaks
            //so if the program doesn't break by the end of the program
            //I return false because I did not find it
            for (int i=0;i<n;i++){
                if (array[i]==num){
                    return true;}
            }
            return false;
        }
        public int total(){//simply loop through each integer in the array 
            //n is the amount of integers I want to count whenever I loop through
            //and add them up 
            int total=0;
            for (int i=0; i<n; i++){
                total=array[i]+total;
            }
            return total;
        }
        public int average(){//same thing as before but we just divide by
            // n (amount of integers used) to find average
            int avg=total()/n;
            return avg;
        }
        public void reverseArray(){//looping through half of integers in array I want to use/so n times
            //and swap each one with the one on the other side of the array, so this is why I only 
            //loop through half of the integers
            int orgnum;
            int len=array.length;
            for (int i=0; i<(len/2); i++){
                orgnum=array[i];
                array[i]=array[len-i-1];
                array[len-i-1]=orgnum;
            }
        }
        public boolean remove(int value){//for this, I loop through each and if I find the value
            //I want to remove in the array, I swap it with the last one and
            // decrease n (the number of integers I care about) by 1
            //this moves the original last integer I care about to the spot where the number 
            //was just removed
            int orgnum;
            if (find(value)==true) {
                for (int i=0; i<array.length;i++){
                    if (array[i]==value){
                        orgnum=array[i];
                        array[i]=array[n-1];
                        array[n-1]=-1;
                        n--;
                        return true;
                    }
                }
            }
            System.out.println("Error: the number is not in the array");
            return false;//after looping through every value, if the value is not found, 
            //return false and error message because the value someone wanted to 
            //remove was not in the array
        }
        public void removeMax(){
            int max=findMax();//we returned max, so we just set that from findMax to max
            remove(max);//use remove method to get rid of max
        }
        public void removeMin(){
            //same concpet as above, just for min this time
            int min=findMin();
            remove(min);}
        public boolean allDistinct(){
        //I use nested for loops beacuse if any value equals a value 
        //from the array except for the same spot, there are two of the same exact values
        //so they would not be distinct
            for (int i=0; i<n;i++){
                for (int j=0; j<n; j++){
                    if (array[i]==array[j] && i != j){
                         return false;
                    }
                }
            }
            return true;//after iterating through, if none are the same, the array is all distinct
        }
        public void display(){//simply displaying them
            if (n<1){
                System.out.println("empty");//if numbers I care about in array (n) is empty
            }
            for (int i=0; i<n; i++){//printining each variable in the array as I loop through through all one by one
                System.out.println(array[i]);
            }
        }
    }