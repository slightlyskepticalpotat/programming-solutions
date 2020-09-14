import java.util.Scanner;

public class nccc2j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        String expression = scan.nextLine();
        int a = Integer.parseInt(String.valueOf(expression.charAt(0))), b = Integer.parseInt(String.valueOf(expression.charAt(4))), c = Integer.parseInt(String.valueOf(expression.charAt(8)));
        if (a + b == c) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }
    }
}