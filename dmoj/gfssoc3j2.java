import java.lang.Math;
import java.util.Scanner;

public class gfssoc3j2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        double c = scan.nextDouble();
        for (int i = 0; i < n; i++) {
            c -= scan.nextDouble();
        }
        if (c >= 0.00) {
            System.out.println(String.format("%.2f", c));
        } else if (Math.abs(c) <= 0.00000001) { // rounding inaccuracies
            System.out.println("0.00");
        } else {
            System.out.println("Fardin's broke");
        }
    }
}