import java.util.Scanner;
import java.lang.Math;

public class Loops {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int totalMarks = 0, numberMarks = -1, latestMark = 0;
        while (latestMark != -1) {
            System.out.println("Mark: ");
            latestMark = in.nextInt();
            totalMarks += latestMark;
            numberMarks += 1;
        }
        System.out.println(Math.round((double) totalMarks / numberMarks));
        in.close();
    }
}
