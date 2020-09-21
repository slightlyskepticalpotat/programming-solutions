import java.util.Scanner;

public class dwite09c2p2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int correct, a, b, c, d, e;
        for (int i = 0; i < 5; i++) {
            correct = 0;
            a = scan.nextInt() + scan.nextInt();
            b = scan.nextInt() + scan.nextInt();
            c = scan.nextInt() + scan.nextInt();
            d = scan.nextInt() + scan.nextInt();
            e = scan.nextInt() + scan.nextInt();
            if (scan.nextInt() == a) {
                correct += 1;
            }
            if (scan.nextInt() == b) {
                correct += 1;
            }
            if (scan.nextInt() == c) {
                correct += 1;
            }
            if (scan.nextInt() == d) {
                correct += 1;
            }
            if (scan.nextInt() == e) {
                correct += 1;
            }
            System.out.println(correct);
        }
    }
}