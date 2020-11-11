import java.util.Scanner;

public class ecoo19r1p1 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n, m, d, total, washes;
        for (int i = 0; i < 10; i++) {
            n = scan.nextInt();
            m = scan.nextInt();
            d = scan.nextInt();
            total = n;
            washes = 0;
            int[] days = new int[d + 1];
            for (int j = 0; j < m; j++) {
                days[scan.nextInt()] += 1; // number of clean events each day
            }
            for (int j = 1; j <= d; j++) {
                if (n == 0) {
                    washes += 1;
                    n = total;
                }
                n += (days[j] - 1);
                total += days[j];
            }
            System.out.println(washes);
        }
    }
}