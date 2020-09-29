import java.util.Scanner;

public class dwite09c1p3 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int m, total;
        for (int i = 0; i < 5; i++) {
            m = scan.nextInt();
            total = 0;
            for (int j = 0; j < m; j++) {
                total += scan.nextInt();
            }
            System.out.println((m + 2) * (m + 1) / 2 - total);
        }
    }
}