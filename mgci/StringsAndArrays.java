/**
* This program reads in a string and then determines
* if it is a case-insensitive palindrome.
*
* @author  Anthony Chen
* @version 1.0
* @since   2022-03-01
**/

import java.util.Scanner;

public class StringsAndArrays {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); // initialise scanner from stdin
        System.out.println("Enter word:");
        String possiblePalindrome = in.nextLine(); // holds the word we need to check
        possiblePalindrome = possiblePalindrome.toUpperCase(); // making word uppercase with built-in method
        System.out.println(" ");
        if (possiblePalindrome.equals(new StringBuilder(possiblePalindrome).reverse().toString())) { // creates a new reversed version of the word
            System.out.println("This is a palindrome!");
        } else {
            System.out.println("This is not a palindrome!");
        }
        in.close();
    }
}
