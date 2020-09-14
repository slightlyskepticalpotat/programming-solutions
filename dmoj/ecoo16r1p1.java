import java.util.Scanner;

public class ecoo16r1p1 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n, wt, wa, wp, wq, passes;
        for (int i = 0; i < 10; i++) {
            wt = scan.nextInt();
            wa = scan.nextInt();
            wp = scan.nextInt();
            wq = scan.nextInt();
            passes = 0;
            n = scan.nextInt();
            for (int j = 0; j < n; j++) {
                if (scan.nextInt() * wt + scan.nextInt() * wa + scan.nextInt() * wp + scan.nextInt() * wq >= 5000) {
                    passes += 1;
                }
            }
            System.out.println(passes);
        }
    }
}