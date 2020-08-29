import java.util.Scanner;

public class bts17p2 {
	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);
		int g = scan.nextInt();
		double probability = 1;
		for (int i = 0; i < g; i++) {
			int e = scan.nextInt(), p = scan.nextInt();
			probability *= ((double) (p - e) / (double) p);
		}
		System.out.println(probability);
	}
}