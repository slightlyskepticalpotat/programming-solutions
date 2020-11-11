import java.util.Scanner;

public class dmopc17c2p1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), c = 0, v = 0;
        long total = 0;
        for (int i = 0; i < n; i++) {
            c = scan.nextInt();
            v = scan.nextInt();
            if (v > 0) {
                total += c;
            }
        }
        System.out.println(total);
    }
}