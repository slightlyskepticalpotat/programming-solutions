import java.util.Arrays;
import java.util.Scanner;

public class dmpg15b2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int trunk_1[] = new int[3], trunk_2[] = new int[3];
        trunk_1[0] = scan.nextInt();
        trunk_1[1] = scan.nextInt();
        trunk_1[2] = scan.nextInt();
        trunk_2[0] = scan.nextInt();
        trunk_2[1] = scan.nextInt();
        trunk_2[2] = scan.nextInt();
        Arrays.sort(trunk_1);
        Arrays.sort(trunk_2);
        if (trunk_1[0] <= trunk_2[0] && trunk_1[1] <= trunk_2[1] && trunk_1[2] <= trunk_2[2]) {
            System.out.println("Y");
        } else {
            System.out.println("N");
        }
    }
}