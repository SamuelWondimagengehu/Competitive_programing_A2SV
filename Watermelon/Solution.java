import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int value = input.nextInt();

		if(value != 2 && value % 2 == 0) System.out.println("YES");
		else System.out.println("NO");
	}
}
