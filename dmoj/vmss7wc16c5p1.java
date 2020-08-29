import java.util.Scanner;

public class vmss7wc16c5p1 {
	public static void main (String args[])
	{
		Scanner scan = new Scanner(System.in);
		int l = scan.nextInt(), x = scan.nextInt(), s = 0;
		while (((double) s / x) + ((double) l / x) != l) { // buffered + extra
			s++;
		}
		System.out.println(s);
	}
}