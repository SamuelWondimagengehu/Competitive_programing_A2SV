class Solution {
    public class Pair {
        int position;
        int speed;

        public Pair(int position, int speed) {
            this.position = position;
            this.speed = speed;
        }
    }

    public int carFleet(int target, int[] position, int[] speed) {
        Pair[] pair_array = new Pair[position.length];
        Stack<Double> fleet = new Stack<>();

        for(int i = 0; i < position.length; i++) {
            pair_array[i] = new Pair(position[i],speed[i]);
        }

        Arrays.sort(pair_array, (a,b)-> a.position - b.position);

        for(int i = pair_array.length-1; i >= 0; i--) {
            double time = (double)(target - pair_array[i].position) 
                                            / pair_array[i].speed;

            if(!fleet.isEmpty() && time <= fleet.peek()) {
                continue;
            }
            fleet.push(time);
        }
        return fleet.size();
    }
}
