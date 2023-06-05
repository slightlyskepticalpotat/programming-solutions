import java.util.Scanner;

public class ForLoop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int start = scanner.nextInt(), end = scanner.nextInt(), parity = scanner.nextInt(); // odd == odd, even == even
        scanner.close();
        for (int i = start; i <= end; i++) {
            if (i % 2 == parity % 2) {
                System.out.println(i);
            }
        }
    }
}
