import java.util.Scanner;

public class coci09c1p2 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.println(n * (n + 1) * (n + 2) / 2);
    }
}