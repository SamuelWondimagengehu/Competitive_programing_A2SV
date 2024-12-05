function isPowerOfTwo(n: number): boolean {
    if(n == 1) return true;
    else if(Math.floor(n) == 0) return false; 
    
    return isPowerOfTwo(n/2);
};