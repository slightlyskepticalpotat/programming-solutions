import java.util.Scanner;

public class Main {
  public static void main(String[] args) 
  {
    Scanner in = new Scanner(System.in); // slow input
    for (int i = 0; i < 5; i++){
      double p = in.nextDouble();
      System.out.println((int) Math.ceil(p/693) * 1000);
    }
  }
}