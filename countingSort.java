   public static List<Integer> countingSort(List<Integer> arr) {
    // Write your code here
        List<Integer> newList = new ArrayList<>(Collections.nCopies(100,0));
       
        for(Integer I : arr) {
            if(newList.get(I) != 0) {
                newList.set(I,newList.get(I) + 1);
            } else {
                newList.set(I,1);
            }
        }        
   
        return newList;
    }
