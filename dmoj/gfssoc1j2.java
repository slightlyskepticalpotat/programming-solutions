import java.util.Scanner;

public class gfssoc1j2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int x = 0, y = 0, n = scan.nextInt();
        for (int i = 0; i < n; i++) {
            String direction = scan.next();
            if (direction.equals("North")) {
                y += scan.nextInt();
            } else if (direction.equals("East")) {
                x += scan.nextInt();
            } else if (direction.equals("South")) {
                y -= scan.nextInt();
            } else {
                x -= scan.nextInt();
            }
        }
        System.out.printf("%d %d\n", x, y);
    }
}