function multiply(num1: string, num2: string): string {
    if(num1 == "0" || num2 == "0") {
        return "0"
    }
    
    let fl = num1.split("").reverse()
    let sl = num2.split("").reverse()
    
    let res = Array(num1.length + num2.length).fill(0)
    
    for(let i = 0; i < num1.length; i++) {
        for(let j = 0; j < num2.length; j++) {
            let digit = parseInt(fl[i]) * parseInt(sl[j])
            let sum = digit + res[i + j]
            res[i + j] = sum % 10
            res[i + j + 1] += Math.floor(sum / 10)
        }
    }
    let beg = 0
    while(res[res.length - 1] === 0) { res.pop() }
    
    return res.reverse().join("")
};