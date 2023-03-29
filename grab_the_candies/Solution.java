import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		while(n-- > 0) {
			int b = sc.nextInt();

			int x = 0, even = 0, odd = 0;

			for(int k = 0; k < b; k++) {
				x = sc.nextInt();

				if(x%2==0) even += x;
				else odd += x;
			}
			
			if(even > odd) System.out.println("YES");
			else System.out.println("NO");
		}
	}
}
