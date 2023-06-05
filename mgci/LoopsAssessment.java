/**
* This program reads 3 decimal values and outputs them
* sorted, and can repeat until the user quits it.
*
* @author  Anthony Chen
* @version 1.0
* @since   2022-02-14
*/

import java.util.Arrays;
import java.util.Scanner;

public class LoopsAssessment {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int programStatus = 1; // status of the program, 2 means to quit
        double[] numbers = {0.0, 0.0, 0.0}; // this holds the three numbers
        while (programStatus == 1) { // the user enters the new programStatus at the end
            for (int i = 0; i < 3; i++) { // asks user for 3 numbers
                System.out.println("Enter num" + (i + 1) + ":");
                numbers[i] = in.nextDouble();
            }
            Arrays.sort(numbers); // sorts using builtin method
            System.out.println(" ");
            System.out.println("The numbers in order:");
            System.out.println(numbers[0] + ", " + numbers[1] + ", " + numbers[2]); // builds the output string, then prints it
            System.out.println(" ");
            System.out.println("Enter 1 to run again, 2 to quit:");
            programStatus = in.nextInt();
        }
        in.close();
    }
}
