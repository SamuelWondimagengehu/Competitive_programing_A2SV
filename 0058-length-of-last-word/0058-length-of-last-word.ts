function lengthOfLastWord(s: string): number {
    return s.split(" ").filter((val) => val.length > 0).pop().length
};