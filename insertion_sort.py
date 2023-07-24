def insertionSort1(n, arr):
    # Write your code here
    num = arr[n - 1]
    j = n - 2
    temp = arr[j]
      
    while temp >= num and j >= 0:
        arr[j + 1] = temp
        j -= 1
        temp = arr[j]
        print(*arr)
        
    arr[j + 1] = num    
    print(*arr)
