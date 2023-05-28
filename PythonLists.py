if __name__ == '__main__':
    n = int(input())    
    
    arr = []
    lines = []
    
    for i in range(n):
        lines.append(input())
    
    for line in lines:
        s = line.split(" ")
        if s[0] == 'insert':
            arr.insert(int(s[1]),int(s[2]))
        elif s[0] == 'remove':
            arr.remove(int(s[1]))
        elif s[0] == 'append':
            arr.append(int(s[1]))
        elif s[0] == 'sort':
            arr.sort()
        elif s[0] == 'pop':
            arr.pop()
        elif s[0] == 'reverse':
            arr.reverse()    
        else:
            print(arr)
