import java.util.Scanner;

public class wc18c1j3 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt(), b = scan.nextInt();
        String alice, bob;
        if (90 <= a && a <= 100) {
            alice = "A";
        } else if (80 <= a && a < 90) {
            alice = "B";
        } else if (70 <= a && a < 80) {
            alice = "C";
        } else if (60 <= a && a < 70) {
            alice = "D";
        } else {
            alice = "F";
        }
        if (90 <= b && b <= 100) {
            bob = "A";
        } else if (80 <= b && b < 90) {
            bob = "B";
        } else if (70 <= b && b < 80) {
            bob = "C";
        } else if (60 <= b && b < 70) {
            bob = "D";
        } else {
            bob = "F";
        }
        if (alice == bob) {
            System.out.println("Same");
        } else {
            System.out.println("Different");
        }
    }
}