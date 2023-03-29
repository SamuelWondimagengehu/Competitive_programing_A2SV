import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		while(n-- > 0) {
			int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
			
			if(a+b==c) System.out.println("+");
			else if(a-b==c) System.out.println("-");
		}
	}
}
