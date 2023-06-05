/**
* This program takes a list of grocery items with prices,
* and then sorts them with the selection sort algorithm.
*
* @author  Anthony Chen
* @version 1.0
* @since   2022-04-07
*/

import java.util.Scanner;

public class Sorting {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("How many items are you buying?");
        int number = Integer.parseInt(in.nextLine()); // take integer from line
        String[] items = new String[number]; // store every item and price as a string
        int minimum; // stores location of cheapest item
        String temp; // temp variable so we can move elements
        for (int i = 1; i <= number; i++) {
            System.out.println("Enter name and price of item " + i + ":");
            items[i - 1] = in.nextLine(); // since arrays start at 0
        }
        for (int i = 0; i < number; i++) {
            minimum = i;
            for (int j = i + 1; j < number; j++) {
                if (getPrice(items[j]) < getPrice(items[minimum])) { // compare price of two elements
                    minimum = j;
                }
            }
            temp = items[minimum]; // swap elements into proper positions
            items[minimum] = items[i];
            items[i] = temp;
        }
        System.out.println("Your ordered item list is:");
        for (int i = 0; i < number; i++) { // print sorted list
            System.out.println(items[i]);
        }
        in.close();
    }

    public static float getPrice(String name) {
        String[] parts = name.split("[$]"); // split the string on $
        return Float.parseFloat(parts[1]); // get price and return it
    }
}
