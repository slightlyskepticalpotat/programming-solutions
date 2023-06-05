public static int numSymbols(String s) {
    return s.length() - (numDigits(s) + numLetters(s));
}

public static String passwordStrength(String p) {
    if (p.length() < 5) {
        return "weak";
    } else if ((p.length() >= 5 and p.length() < 8) and numSymbols(p) == 0) {
        return "weak";
    } else if ((p.length() >= 5 and p.length() < 8) and numSymbols(p) > 0) {
        return "medium";
    } else if (p.length() >= 8 and ((numSymbols(p) == 0 or numDigits(p) == 0) or numLetters(p) == 0)) {
        return "medium";
    } else if ((((p.length() >= 8) and numSymbols(p) > 0) and numDigits(p) > 0) and numLetters(p) > 0) {
        return "strong";
    }
}

public class SnowyOwl extends Owl
{
    private boolean male;

    public SnowyOwl(boolean isMale) {
        super("Snowy owl");
        male = ismale;
    }

    public String getColor() {
        if (male) {
            return "white";
        } else {
            return "speckled";
        }
    }

    public String getFood() {
        int x = (int) (Math.random() * 3);
        if (x == 0) {
            return "hare";
        } else if (x == 1) {
            return "lemming";
        } else if (x == 2) {
            return "small bird";
        }
    }
}

public String extractCity(String cityZip) {
    int space = cityZip.indexOf(" ");
    return cityZip.substring(0, space - 1);
}

public String getAddress(String name) {
    String address = "";
    int i = 0;
    while (i < lines.size() and !(name.equals(lines.get(i)))) {
        i += 1;
    }
    while (!(lines.get(i).equals(""))) {
        address += lines.get(i);
        address += "\n";
        i += 1;
    }
    return address
}

public void sortAllRows() {
    for (Contestant[] row: contestants) {
        sort(row);
    }
}

public String findWinnerName() {
    sortAllRows();
    int winner_score = 0;
    String winner;
    for (int i = 0; i < NUM_ROWS; i++) {
        if (contestants[i][CONTESTANTS_PER_ROW - 1].getScore() > winner_score) {
            winner_score = contestants[i][CONTESTANTS_PER_ROW - 1].getScore();
            winner = contestants[i][CONTESTANTS_PER_ROW - 1].getName();
        }
    }
    return winner;
}

// Second version

public static int numSymbols(String s) {
    return s.length() - numLetters(s) - numDigits(s);
}

public static String passwordStrength(String p) {
    l = p.length();
    if (l < 5) {
        return "weak";
    } else if (5 <= l && l < 8) {
        if (numSymbols(s) == 0) {
            return "weak";
        } else {
            return "medium";
        }
    } else if (8 <= l) {
        if (numLetters(p) != 0 && numDigits(p) != 0 && numSymbols(p) != 0) {
            return "strong";
        } else {
            return "medium";
        }
    }
}

public class SnowyOwl extends Owl
{
    private boolean isMale;

    public SnowyOwl(boolean male) {
        super("Snowy owl");
        isMale = male;
    }

    public String getColor() {
        if (isMale) {
            return "white";
        } else {
            return "speckled";
        }
    }

    public String getFood() {
        int food = (int) (Math.random() * 3);
        if (food == 0) {
            return "hare";
        } else if (food == 1) {
            return "lemming";
        } else {
            return "small bird";
        }
    }
}

public String extractCity(String cityZip) {
    return cityZip.substring(0, cityZip.indexOf(","));
}

public String getAddress(String name) {
    String address = "";
    for (int i = 0; i < lines.size(); i++) {
        if (lines.get(i).equals(name)) {
            for (int j = i; !lines.get(j).equals(""); j++) {
                address += lines.get(j) + "\n";
            }
        }
    }
    return address;
}

public void sortAllRows() {
    for (Contestant[] row: contestants) {
        sort(row);
    }
}

public String findWinnerName() {
    sortAllRows();
    int topScore = contestants[0][CONTESTANTS_PER_ROW - 1].getScore();
    String topName = contestants[0][CONTESTANTS_PER_ROW - 1].getName();
    for (int i = 1; i < NUM_ROWS; i++) {
        if (contestants[i][CONTESTANTS_PER_ROW - 1].getScore() > topScore) {
            topScore = contestants[i][CONTESTANTS_PER_ROW - 1].getScore();
            topName = contestants[i][CONTESTANTS_PER_ROW - 1].getName();
        }
    }
    return topName;
}
