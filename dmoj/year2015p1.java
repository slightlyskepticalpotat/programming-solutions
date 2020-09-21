import java.util.Scanner;

public class year2015p1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String template = scan.nextLine();
        int n = scan.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.println(template.replace(">", scan.next()));
        }
    }
}