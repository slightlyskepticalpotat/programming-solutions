import java.util.Scanner;

public class wc18c3j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int p = scan.nextInt(), b = scan.nextInt(), d = scan.nextInt();
        System.out.println((p / b) * d + p % b);
    }
}