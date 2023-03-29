import java.util.Scanner;

public class Sol {	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	
		int n = sc.nextInt();
		int d = sc.nextInt();

		String line = sc.next();
		char[] arr = line.toCharArray();

		int a_ptr = d;
		int b_ptr = n-1;
		int steps = 0;

		while(b_ptr>= 0 && a_ptr>=1) {
			int i = b_ptr-a_ptr;

			if(i >= 0 && arr[i] == '1') {
				b_ptr = i;
				a_ptr = d;
				steps++;
			} else a_ptr--;
		}

		if(steps== 0) System.out.println("-1");
		else System.out.println(steps);		
	}
}

