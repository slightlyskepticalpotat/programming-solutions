import java.util.Scanner;

public class dwite12c1p2 {
	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);
		double houses[] = new double[5];
		for (int i = 0; i < 5; i++) {
			int a = scan.nextInt(), b = scan.nextInt();
			houses[i] = Math.floor((double) a / (a + b) * 10);
		}
		for (int i = 0; i < 5; i++) {
			System.out.println("*".repeat((int) houses[i]) + ".".repeat(10 - (int) houses[i]));
		}
	}
}