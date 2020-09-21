import java.util.Scanner;

public class wc17c4j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String c = scan.nextLine(), t = scan.nextLine();
        if (c.equals(t)) {
            System.out.println(c);
        } else {
            System.out.println("Undecided");
        }
    }
}