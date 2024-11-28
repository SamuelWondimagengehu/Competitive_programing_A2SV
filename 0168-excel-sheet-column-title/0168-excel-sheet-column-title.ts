function convertToTitle(columnNumber: number): string {
    const alphabets: string[] = Array.from({length: 26}, (_, i) => String.fromCharCode(65 + i));
    let res: string = "";
    
    while(columnNumber > 0) {
        columnNumber -= 1;
        res = alphabets[columnNumber % 26] + res;
        
        columnNumber= Math.floor(columnNumber / 26);
    }
  
    return res;
};