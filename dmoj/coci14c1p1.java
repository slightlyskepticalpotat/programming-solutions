import java.util.Scanner;

public class coci14c1p1 {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt(), current = 0;
        int result_array[] = new int[n], original_array[] = new int[n];
        for (int i = 0; i < n; i++) {
            result_array[i] = scan.nextInt();
        }
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                original_array[i] = result_array[i];
            } else {
                original_array[i] = result_array[i] * (i + 1) - current;
            }
            current += original_array[i];
        }
        for (int i = 0; i < n; i++) {
            System.out.print(original_array[i] + " ");
        }
        System.out.print("\n");
    }
}