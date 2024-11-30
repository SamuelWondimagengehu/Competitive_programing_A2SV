function addBinary(a: string, b: string): string {
    let i: number = a.length - 1;
    let j: number = b.length - 1;
    let carry: number = 0;
    let res: string = "";
    
    while(i >= 0 || j >= 0 || carry > 0) {
        const bitA = i >= 0 ? parseInt(a[i]) : 0;
        const bitB = j >= 0 ? parseInt(b[j]) : 0;
        
        const sum = bitA + bitB + carry;
        res = (sum % 2) + res;
        carry = Math.floor(sum / 2);
        
        i--;
        j--;
    }
    
    return res;
};