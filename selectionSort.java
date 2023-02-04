class Solution
{
	int  select(int arr[], int i)
	{
        // code here such that selectionSort() sorts arr[]
        int smallest = arr[i], temp = 0;
        
        for(int j = i; j < arr.length; j++) {
            if(smallest > arr[j]) {
                temp = smallest;
                smallest = arr[j];
                arr[j] = temp;
            } 
        }
        return smallest;
	}
	
	void selectionSort(int arr[], int n)
	{
	    //code here
	    int value = 0;
	    for(int i = 0 ; i < n; i++) {
	        value = select(arr,i);
	        arr[i] = value;
	    }
	}
}
