function lengthOfLastWord(s: string): number {
    let l =  s.split(" ").filter((val) => val.length > 0)
    
    return l.pop().length
};