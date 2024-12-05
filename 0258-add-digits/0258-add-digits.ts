function addDigits(num: number): number {
    if(String(num).length == 1) return num;
    
    return addDigits(Array.from(String(num)).map(Number).reduce((s, n) => n+s, 0));
};