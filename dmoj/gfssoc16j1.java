import java.util.Scanner;

public class gfssoc16j1 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int c = scan.nextInt(), n = scan.nextInt(), r = 0;
        String course = "course";
        for (int i = 0; i < c; i++) {
            course = scan.nextLine();
            if (course.equals("Math")) {
                r += 4;
            } else if (course.equals("Science")) {
                r += 3;
            } else if (course.equals("English")) {
                r += 2;
            } else {
                r += 1;
            }
            if (r > n) {
                System.out.println("Go to Metro");
                System.out.println(i);
                System.exit(0);
            }
        }
        System.out.println("YEA BOI");
    }
}