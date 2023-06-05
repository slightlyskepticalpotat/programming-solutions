public boolean isValid(String password) {
    boolean up = false;
    boolean lo = false;
    boolean sym = false;
    for (int i = 0; i < password.length(); i++) {
        if (upper.indexOf(password.substring(i, i + 1)) != -1) {
            up = true;
        } else if (lower.indexOf(password.substring(i, i + 1)) != -1) {
            lo = true;
        } else if (symbols.indexOf(password.substring(i, i + 1)) != -1) {
            sym = true;
        }
    }
    return up && lo && sym && password.length() <= maxLength && password.length() >= minLength;
}

public String generatePassword() {
    String password = "";
    String choices = upper + lower + symbols;
    int i = 0;
    int l = 0;
    int p = 0;
    while (!isValid(password)) {
        password = "";
        l = (int) (Math.random() * (MaxLength - MinLength + 1)) + MinLength - 1;
        for (int j = 0; j < l; j++) {
            p = (int) (Math.random() * choices.length());
            password += choices.substring(p, p + 1);
        }
    }
    return password;
}

public class ISBN
{
    private int ISBN_num;

    public ISBN(int number) {
        ISBN_num = number;
    }

    public String calculateCheckDigit() {
        int n = ISBN_num;
        int check = 0;
        for (int i = 0; i < 9; i++) {
            check += (ISBN_num % 10) * (i + 2);
            ISBN_num /= 10;
        }
        check = 11 - (check % 11);
        if (check == 10) {
            return "X";
        }
        return check.toString();
    }

    public String generateNumber() {
        return ISBN_num + "-" + calculateCheckDigit();
    }
}

public double getTotalWeight() {
    double weight = 0.00;
    for (Double car: trainCars) {
        weight += car;
    }
    return weight;
}

public ArrayList<Double> removeExcessTrainCars() {
    ArrayList<Double> removedCars = new ArrayList<Double>();
    while (getTotalWeight() > maxWeight) {
        removedCars.add(trainCars.remove(trainCars.size() - 1););
    }
    return removedCars;
}

public Pixel[][] generatePixelArray(int[][] reds, int[][] greens, int[][] blues) {
    Pixel[][] grid = new Pixel[reds.length][reds[0].length];
    for (int i = 0; i < reds.length; i++) {
        for (int j = 0; j < reds[0].length; j++) {
            grid[i][j] = new Pixel(reds[i][j], greens[i][j], blues[i][j]);
        }
    }
    return grid;
}

public Pixel[][] flipImage(Pixel[][] image, boolean horiz) {
    Pixel flipped = new Pixel[image.length][image[0].length];
    if (horiz) {
        for (int i = 0; i < image.length; i++) {
            for (int j = 0; j < image[0].length; j++) {
                flipped[i][j] = image[image[0].length - j - 1][j];
            }
        }
    } else {
        for (int i = 0; i < image.length; i++) {
            for (int j = 0; j < image[0].length; j++) {
                flipped[i][j] = image[j][image.length - i - 1];
            }
        }
    }
    return flipped;
}
// Destruction of persistent data, incurs a penalty
