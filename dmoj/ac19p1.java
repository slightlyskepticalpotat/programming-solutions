import java.util.Scanner;

public class ac19p1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        for (int i = 0; i < t; i++) {
            long n = scan.nextLong(), a = scan.nextLong(), b = scan.nextLong(), c = scan.nextLong();
            if (c >= n) {
                System.out.printf("0 0 %d\n", n); // like cpp
            } else if (b + c >= n) {
                System.out.printf("0 %d %d\n", (n - c), c);
            } else if (a + b + c >= n) {
                System.out.printf("%d %d %d\n", (n - b - c), b, c);
            } else {
                System.out.printf("-1\n");
            }
        }
    }
}