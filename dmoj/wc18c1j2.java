import java.util.Scanner;

public class wc18c1j2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String target = scan.nextLine(), check;
        for (int i = 0; i < 5; i++) {
            check = scan.nextLine();
            if (target.equals(check)) {
                System.out.println("Y");
                System.exit(0);
            }
        }
        System.out.println("N");
    }
}