import java.util.Scanner;

public class mwc15c8p1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int total = (n * (n + 1)) / 2;
        for (int i = 0; i < (n - 1); i++) {
            total -= scan.nextInt();
        }
        System.out.println(total);
    }
}