/*
Author: Anthony
Date: 10/09/2021
Unfortunately worth marks
*/

import java.util.Scanner;
import java.lang.Math;


public class WarmUp
{
    public static void main(String[] args) {
        // System.out.println("1");
        System.out.println("Hello World!");
        // System.out.println("2");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Name: ");
        String name = scanner.next();
        System.out.format("Hello, %s!\n", name);
        // System.out.println("3");
        System.out.println("Numbers: ");
        int x = scanner.nextInt(), y = scanner.nextInt();
        System.out.println((int) Math.pow(x, y));
        // System.out.println("4");
        System.out.println("Age: ");
        int age = scanner.nextInt();
        if (age >= 18) {
            System.out.println("Old enough");
        } else {
            System.out.println("Too young");
        }
        // System.out.println("5");
        int age2 = -1;
        while (age2 < 0) {
            System.out.println("Age: ");
            age2 = scanner.nextInt();
            if (0 <= age2 && age2 <= 17) {
                System.out.println("You are a minor");
            } else if (18 <= age2 && age2 <= 64 ) {
                System.out.println("You are the age of majority");
            } else if (65 < age2) {
                System.out.println("you are an elder");
            } else {
                System.out.println("invalid age");
            }
        }
        // System.out.println("6");
        int random = (int) (Math.random() * 10) + 1;
        int guess = -1;
        while (guess != random) {
            System.out.println("Guess: ");
            guess = scanner.nextInt();
            if (guess == random) {
                System.out.println("correct!");
            } else {
                System.out.println("try again!");
                if (guess > random) {
                    System.out.println("lower!");
                } else {
                    System.out.println("higher!");
                }
            }
        }
        scanner.close();
    }
}
