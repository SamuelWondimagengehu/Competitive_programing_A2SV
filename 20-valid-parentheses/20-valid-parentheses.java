class Solution {
    public char match(char r) {
		char c = 'r';
		switch(r) {
		case '(': c = ')';
			break;
		case '{': c = '}';
			break;
		case '[': c = ']';
			break;
		}
		return c;
	}
	
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if(c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } 
            else if(!stack.isEmpty()) {
                if(match(stack.peek()) == c) stack.pop();
                else return false;
            }
            else return false;
        }        

        return stack.isEmpty();
}
}