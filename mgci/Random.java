import java.lang.Math;
import java.util.Scanner;

public class Random
{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Low: ");
        int l = scanner.nextInt();
        int temp, rand, n;
        System.out.println("High: ");
        int r = scanner.nextInt();
        if (l > r) {
            temp = r;
            r = l;
            l = temp;
        }
        System.out.println("Number: ");
        n = scanner.nextInt();
        scanner.close();
        for (int i = 0; i < n; i++) {
            rand = l + (int) (Math.random() * (r - l + 1));
            System.out.println(rand);
        }
    }
}
