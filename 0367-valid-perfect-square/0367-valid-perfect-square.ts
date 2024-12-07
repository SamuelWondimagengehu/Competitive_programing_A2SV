function isPerfectSquare(num: number): boolean {
    if(num == 1) return true;
    
    let rightPtr: number = Math.floor(num / 2);
    let leftPtr: number = 1;
    
    while(leftPtr <= rightPtr) {
        let mid: number = Math.floor((rightPtr + leftPtr) / 2);
        
        if(mid * mid == num) {
            return true;
        } else if(mid * mid > num) {
            rightPtr = mid - 1;
        } else {
            leftPtr = mid + 1;
        }
    }
    
    return false;
};