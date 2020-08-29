import java.util.Scanner;

public class coci07c5p1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt(), b = scan.nextInt(), c = scan.nextInt();
        if (a + b == c) {
            System.out.println(String.format("%d+%d=%d", a, b, c));
        } else if (a - b == c){
            System.out.println(String.format("%d-%d=%d", a, b, c));
        } else if (a * b == c) {
            System.out.println(String.format("%d*%d=%d", a, b, c));
        } else if ((double) a / b == c) {
            System.out.println(String.format("%d/%d=%d", a, b, c));
        } else if (a == b + c) {
            System.out.println(String.format("%d=%d+%d", a, b, c));
        } else if (a == b - c) {
            System.out.println(String.format("%d=%d-%d", a, b, c));
        } else if (a == b * c) {
            System.out.println(String.format("%d=%d*%d", a, b, c));
        } else {
            System.out.println(String.format("%d=%d/%d", a, b, c));
        }
    }
}