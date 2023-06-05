public int getLetterValue(String letter) {
    return (int) Math.pow(2, letters.indexOf(letter));
}

public int getDecimalValue(String numeral) {
    int total = 0;
    for (int i = 0; i < numeral.length(); i++) {
        total += getLetterValue(numeral.charAt(i));
    }
    return total;
}

public String buildLocationNumeral(int value) {
    String numeral = "";
    for (int i = letters.length() - 1; i >= 0; i--) {
        if (getLetterValue(letters.charAt(i)) <= value) {
            numeral += letters.charAt(i);
            value -= getLetterValue(letters.charAt(i));
        }
    }
    return numeral;
}

public class Quadratic
{
    private double a;
    private double b;
    private double c;

    public Quadratic(double aVal, double bVal, double cVal) {
        a = aVal;
        b = bVal;
        c = cVal;
    }

    public double getDiscriminant() {
        return b * b - 4 * a * c;
    }

    public double getRoot1() {
        return (-b + Math.sqrt(getDiscriminant())) / (2 * a);
    }

    public double getRoot2() {
        return (-b - Math.sqrt(getDiscriminant())) / (2 * a);
    }
}

public PaperRoll replacePaper(PaperRoll pRoll) {
    PaperRoll oldPaper = paper;
    paper = pRoll;
    return oldPaper;
}

public void replacePaperRolls() {
    for (Machine mac: machines) {
        if (mac.getPaperRoll().getMeters() < 4) {
            usedRolls.add(mac.replacePaper(newRolls.remove(0));
        }
    }
}

public double getPaperUsed() {
    double total = 0.00;
    for (Machine mac: machines) {
        total += 1000 - mac.getPaperRoll().getMeters();
    }
    for (PaperRoll roll: usedRolls) {
        total += 1000 - roll.getMeters();
    }
    return total;
}

public int getGamePieceCount() {
    int pieces = 0;
    for (int i = 0; i < grid.length(); i++) {
        for (int j = 0; j < grid[0].length(); j++) {
            if (grid[i][j] != null) {
                pieces += 1;
            }
        }
    }
    return pieces;
}

public ArrayList<GamePiece> isAbove (int row, int col) {
    if (grid[row][col] == null) {
        return null;
    }
    ArrayList<GamePiece> pieces = new ArrayList<GamePiece>();
    for (int i = row - 1; i >= 0; i--) {
        if (grid[i][col] != null) {
            pieces.add(grid[i][col]);
        }
    }
    return pieces;
}

public boolean addRandom(int number) {
    if (grid.length() * grid[0].length() - getGamePieceCount() < number) {
        return false;
    }
    int left = number;
    int i;
    int j;
    while (left > 0) {
        i = (int) (Math.random(grid.length()));
        j = (int) (Math.random(grid[0].length()));
        if (grid[i][j] == null) {
            grid[i][j] = new GamePiece();
            left -= 1;
        }
    }
    return true;
}
