import java.util.Scanner;

public class Arrays {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int[] numbers = new int[10];
        int largest = Integer.MIN_VALUE;
        for (int i = 0; i < 10; i++) {
            numbers[i] = in.nextInt();
        }
        for (int i = 0; i < 10; i++) {
            largest = Math.max(largest, numbers[i]);
        }
        System.out.println(largest);
        in.close();
    }
}
