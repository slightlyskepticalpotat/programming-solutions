import java.util.Scanner; // thus begins the java

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // input is cancer
        double p = Math.ceil(scanner.nextInt() / (double) 3); // temp double for real division
        double c = Math.ceil(scanner.nextInt() / (double) 3);
        double v = Math.ceil(scanner.nextInt() / (double) 3);
        scanner.close(); // close input
        System.out.format("%.0f\n", p + c + v); // drop decimal places
    }
}