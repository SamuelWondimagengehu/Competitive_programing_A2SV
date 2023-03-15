class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack();
        int[] answer = new int[temperatures.length];
        
        for(int i = 0; i < temperatures.length; i++) {
            while(!stack.isEmpty() && 
            temperatures[stack.peek()] < temperatures[i]) {
                Integer topIndex = stack.pop();
                int indexDiff = i - topIndex;
                answer[topIndex] = indexDiff; 
            }
            stack.push(i);
        }

        while(!stack.isEmpty()) {
            Integer topIndex = stack.pop();
            answer[topIndex] = 0;
        }

        return answer;
    }
}
