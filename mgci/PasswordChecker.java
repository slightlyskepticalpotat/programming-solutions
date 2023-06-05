import java.util.Scanner;

public class PasswordChecker {
    static Scanner in = new Scanner(System.in);

    public static String getPassword() {
        return in.nextLine();
    }

    public static boolean checkPassword(String password) {
        for (int i = 0; i < password.length() - 1; i++) {
            for (int j = i + 1; j < password.length(); j++) {
                if (password.charAt(i) == password.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println("password: ");
        String password = getPassword();
        if (checkPassword(password)) {
            System.out.println("good password");
        } else {
            System.out.println("bad password");
        }
    }
}