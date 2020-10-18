import java.lang.Math;
import java.util.Scanner;

public class p129ex3 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), i = 0;
        while (true) {
            if (Math.pow(2, i) >= n) {
                System.out.println(i);
                break;
            }
            i += 1;
        }
    }
}