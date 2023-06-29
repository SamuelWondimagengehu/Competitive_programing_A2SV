def countSwaps(a):
    # Write your code here
    no_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                no_swaps += 1
    print("Array is sorted in", no_swaps, "swaps.\nFirst Element:", a[0],"\nLast Element:", a[len(a) - 1])
