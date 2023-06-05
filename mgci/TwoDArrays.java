/**
* This program generates random pixel data for an image,
* and then prints the flipped version of it with 2d arrays.
*
* @author  Anthony Chen
* @version 1.0
* @since   2022-03-29
*/

import java.util.Scanner;
import java.lang.Math;

public class TwoDArrays {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter side length for image: ");
        int imageSize = in.nextInt(); // the image is always square
        int[][] image = new int[imageSize][imageSize];
        int temp = 0; // temporary variable to swap data
        for (int i = 0; i < imageSize; i++) { // traverse and randomly init the pixel data
            for (int j = 0; j < imageSize; j++) {
                image[i][j] = (int) (Math.random() * 256);
            }
        }
        System.out.println(" ");
        System.out.println("Pixel Data for Image");
        for (int i = 0; i < imageSize; i++) { // traverse and print the array
            for (int j = 0; j < imageSize; j++) {
                System.out.print(image[i][j] + " ");
            }
            System.out.println(" ");
        }
        for (int i = 0; i < imageSize; i++) { // flip the array
            for (int j = 0; j < imageSize / 2; j++) {
                temp = image[i][j];
                image[i][j] = image[i][imageSize - j - 1];
                image[i][imageSize - j - 1] = temp;
            }
        }
        System.out.println(" ");
        System.out.println("Image flipped: ");
        for (int i = 0; i < imageSize; i++) { // traverse and print the array
            for (int j = 0; j < imageSize; j++) {
                System.out.print(image[i][j] + " ");
            }
            System.out.println(" ");
        }
        in.close();
    }
}
