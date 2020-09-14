import java.util.Arrays;
import java.util.Scanner;

public class a4b1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scan.nextInt();
        }
        Arrays.sort(numbers);
        for (int i = 0; i < n; i ++) {
            System.out.println(numbers[i]);
        }
    }
}