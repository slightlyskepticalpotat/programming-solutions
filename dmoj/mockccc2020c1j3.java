import java.util.Scanner;

public class mockccc2020c1j3 {
	public static void main(String args[]) 
	{
		Scanner scan = new Scanner(System.in);
		long x = scan.nextLong(), y = scan.nextLong(), r = (x * y) % 4;
		if (r == 0) {
			System.out.println((x * y) / 4 + ".00");
		} else if (r == 1) {
			System.out.println((x * y) / 4 + ".25");
		} else if (r == 2) {
			System.out.println((x * y) / 4 + ".50");
		} else {
			System.out.println((x * y) / 4 + ".75");
		}
	}
}