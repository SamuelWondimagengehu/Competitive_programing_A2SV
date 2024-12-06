function nthUglyNumber(n: number): number {
  
    let uglyNums = new Set<number>();
    uglyNums.add(1);
    
    let uglyNum = 1;
    
    for(let i = 0; i < n; i++) {
        uglyNum = Math.min.apply(this, [...uglyNums]);
        uglyNums.delete(uglyNum);
        
        uglyNums.add(uglyNum * 2);
        uglyNums.add(uglyNum * 3);
        uglyNums.add(uglyNum * 5);
    }
    
    return uglyNum;
    
};