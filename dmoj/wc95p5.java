import java.math.BigDecimal;
import java.util.Scanner;

public class wc95p5 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            int n = scan.nextInt();
            BigDecimal x = BigDecimal.ONE;
            for (int j = 1; j <= n; j++) {
                x = x.multiply(new BigDecimal (j));
            }
            int y = x.toString().length();
            System.out.printf("The length of %d! is %d\n", n, y);
        }
    }
}