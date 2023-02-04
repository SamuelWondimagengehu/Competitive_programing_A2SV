class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int x = 0, y = 0;

        for(String token : tokens) {
            if(!token.equals("+") && !token.equals("*") 
            && !token.equals("-") && !token.equals("/")) {
                stack.push(Integer.parseInt(token));
            } else {
                x = stack.pop();
                y = stack.pop();

                if(token.equals("*")) {
                    stack.push(y * x);
                } else if(token.equals("/")) {
                    stack.push(y / x);
                } else if(token.equals("+")) {
                    stack.push(y + x);
                } else {
                    stack.push(y - x);
                }
            }
        }
        
        return stack.pop();
    }
}
