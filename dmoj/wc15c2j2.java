import java.util.Scanner;

public class wc15c2j2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), m = scan.nextInt(), total = 0, rock = 0;
        for (int i = 0; i < n; i++) {
            rock = scan.nextInt();
            if (rock <= m) {
                total += rock;
            }
        }
        System.out.println(total);
    }
}