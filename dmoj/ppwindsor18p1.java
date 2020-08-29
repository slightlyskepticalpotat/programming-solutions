import java.util.Scanner;

public class ppwindsor18p1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), s = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                s += i;
            }
        }
        System.out.println(s);
    }
}