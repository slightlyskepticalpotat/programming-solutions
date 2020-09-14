import java.math.BigInteger;
import java.util.Scanner;

public class acsl1p3 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        BigInteger factorial = new BigInteger("1");
        for (int i = 2; i <= n; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }
        String factorial_string = factorial.toString();
        System.out.println(factorial_string.length() - factorial_string.replace("0", "").length());
    }
}