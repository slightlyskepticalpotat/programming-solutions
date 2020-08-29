import java.util.Scanner;

public class nccc1j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int i = n + 1;
        while (String.valueOf(i).contains("0")) {
            i++;
        }
        System.out.println(i);
    }
}