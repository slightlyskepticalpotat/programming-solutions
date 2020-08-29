import java.math.*; 
import java.util.Scanner; 

public class modinv {
	public static void main(String[] args) 
	{
		Scanner in = new Scanner(System.in);
		BigInteger n, m;
		n = in.nextBigInteger();
		m = in.nextBigInteger();
		System.out.println(n.modInverse(m));
	}
}