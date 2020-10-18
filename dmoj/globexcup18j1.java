import java.util.Scanner;

public class globexcup18j1 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), up = 0, down = 0;
        double x;
        for (int i = 0; i < n; i++) {
            x = scan.nextDouble();
            if (x % 1 >= 0.5) {
                up += 1;
            } else {
                down += 1;
            }
        }
        System.out.println(up);
        System.out.println(down);
    }
}