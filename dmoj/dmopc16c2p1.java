import java.util.Scanner;

public class dmopc16c2p1 {
	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt() * 60, k = scan.nextInt(), i = 0, t = 0;
		for (int j = 0; j < k; j++) {
			i = scan.nextInt();
			if (i == 1) {
				t += 30;
			} else if (i == 2) {
				t += 60;
			} else {
				t += 300;
			}
		}
		if (t <= n) {
			System.out.println("Continue");
		} else {
			System.out.println("Return");
		}
	}
}