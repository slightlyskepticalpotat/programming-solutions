import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    char[] string = in.nextLine().replace("-", "").toCharArray();
    if (Integer.parseInt(String.valueOf(string[0])) + Integer.parseInt(String.valueOf(string[1])) + Integer.parseInt(String.valueOf(string[2])) == Integer.parseInt(String.valueOf(string[3])) + Integer.parseInt(String.valueOf(string[4])) + Integer.parseInt(String.valueOf(string[5]))) {
      if (Integer.parseInt(String.valueOf(string[3])) + Integer.parseInt(String.valueOf(string[4])) + Integer.parseInt(String.valueOf(string[5])) == Integer.parseInt(String.valueOf(string[6])) + Integer.parseInt(String.valueOf(string[7])) + Integer.parseInt(String.valueOf(string[8])) + Integer.parseInt(String.valueOf(string[9]))) {
        System.out.println("Goony!");
        System.exit(0);
      }
    }
    System.out.println("Pick up the phone!");
    in.close();
  }
}