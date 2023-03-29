import java.util.Scanner;

public class Solution {
	public static int count(String line, char a) {
		int count = 0;
		for(char c : line.toCharArray()) {
			if(c==a) count++;
		}
		return count;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		
		while(n-- > 0) {
			String line = sc.next();
			int[] arr = new int[line.length()];

			for(int i = 0; i < line.length(); i++) {
				arr[i] = count(line,line.charAt(i));
			}

			java.util.Arrays.sort(arr);

			if(arr[line.length()-1]==1)System.out.println(4);
			else if(arr[line.length()-1]==2) System.out.println(4);
			else if(arr[line.length()-1]==3) System.out.println(6);
			else System.out.println(-1);
	}
	}
}
