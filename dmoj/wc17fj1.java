import java.util.Scanner;

public class wc17fj1 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), f = scan.nextInt(), cow;
        for (int i = 1; i <= n; i++) {
            cow = scan.nextInt();
            if ((cow % f != 0) || ((cow / f & (cow / f) - 1) != 0)) {
                System.out.println(i);
            }
        }
    }
}