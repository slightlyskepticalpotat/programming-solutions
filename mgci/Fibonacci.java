import java.math.BigInteger;

public class Fibonacci {
    public static void main(String[] args) {
        BigInteger a = BigInteger.ZERO, b = BigInteger.ONE;
        for (int i = 0; i < Long.parseLong(args[0]); i++) {
            System.out.println(i);
            BigInteger c = a.add(b);
            a = b;
            b = c;
        }
        System.out.println(a);
    }
}
