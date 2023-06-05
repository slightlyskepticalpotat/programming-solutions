import java.util.Scanner;
public class TryCatch {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num;
        while (true) {
            try {
                System.out.println("Number: ");
                num = in.nextInt();
                System.out.println(num);
                break;
            } catch (Exception e) {
                System.out.println(e);
                System.out.println("Continuing...");
                in.next();
            }
        }
        in.close();
    }
}
