class Solution {
    public String removeKdigits(String num, int k) {
        int size = num.length();
        
        Stack<Character> stack = new Stack<>();
        
        if(size == k) return "0";
        
        int counter = 0;

        while(counter < size) {
            while(k > 0 && !stack.isEmpty() && stack.peek() > num.charAt(counter)) {
                stack.pop();
                k--;
            }  
            
            stack.push(num.charAt(counter));
            counter++;
        }
        
        StringBuilder s = new StringBuilder();        
        
        while(k > 0) {
            stack.pop();
            k--;
        }
        
        while(!stack.isEmpty()) {
            char c = stack.pop();
            s.append(c);
        }

        s.reverse();
        
        while(s.length() > 1 && s.charAt(0) == '0') {
            s.deleteCharAt(0);
        }
        
        return s.toString();
    }
}