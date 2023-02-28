class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int a = 0;
        int b = people.length - 1;
        int n = 0, remain = 0;
        
        while(a <= b) {
            remain = limit - people[b];
            n++;
            b--;
            if(a <= b && remain >= people[a]) a++;
        }

        return n;
    }
}
