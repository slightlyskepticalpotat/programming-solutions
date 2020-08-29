import java.util.Arrays;
import java.util.Scanner;

public class vpex1p2 {
	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int cake[] = new int[n];
		for (int i = 0; i < n; i++) {
			cake[i] = scan.nextInt();
		}
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += cake[i];
		}
		sum /= n;
		int mistakes = 0;
		for (int i = 0; i < n; i++) {
			if (cake[i] != sum) {
				mistakes += 1;
			}
		}
		System.out.println(mistakes);
	}
}