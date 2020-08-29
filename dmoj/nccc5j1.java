import java.util.Scanner;

public class nccc5j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String n = scan.next();
        if (n.contains("CCC")) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }
}