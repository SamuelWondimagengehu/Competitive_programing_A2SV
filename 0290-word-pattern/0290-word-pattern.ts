function wordPattern(pattern: string, s: string): boolean {
    const words: string[] = s.split(" ");
    
    if(pattern.length != words.length) return false;
    
   
    const charToWord = new Map<string, string>();
    const wordToChar = new Map<string, string>();

    for (let i = 0; i < pattern.length; i++) {
        const char = pattern[i];
        const word = words[i];

        // Check character-to-word mapping
        if (charToWord.has(char)) {
            if (charToWord.get(char) !== word) {
                return false;
            }
        } else {
            charToWord.set(char, word);
        }

        // Check word-to-character mapping
        if (wordToChar.has(word)) {
            if (wordToChar.get(word) !== char) {
                return false;
            }
        } else {
            wordToChar.set(word, char);
        }
    }

    return true;
};