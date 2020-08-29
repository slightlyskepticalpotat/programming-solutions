import java.util.Scanner;

public class nccc3j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), total = 0;
        for (int i = 0; i < n; i++) {
            total += scan.nextInt();
        }
        System.out.println(total);
    }
}