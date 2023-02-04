    public static void insertionSort1(int n, List<Integer> arr) {
    // Write your code here
        int last = arr.get(n - 1), current;
        
        for(int i = n - 2; i >= 0; i--) {
            current = arr.get(i);
            if(last < current) {
                arr.set(i + 1, current);
                System.out.println(arr);
            } else{
                arr.set(i + 1, last);
                System.out.println(arr);
                break;
            }
            
            if(i == 0 && current > last) {
                arr.set(i, last);
                System.out.print(arr);
            }
        }
    }

}
