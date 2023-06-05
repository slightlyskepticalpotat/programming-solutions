public static int arraySum(int[] arr) {
    int total = 0;
    for (int i = 0; i < arr.size(); i++) { // magic iterator works here
        total += arr[i];
    }
    return total;
}

public static int[] rowSums(int[][] arr2D) {
    int[] sums = new int[arr2D.size()];
    for (int i = 0; i < arr2D.size(); i++) {
        sums[i] = arraySum(arr2D[i]);
    }
    return sums;
}

public static boolean isDiverse(int[][] arr2D) {
    int[] sums = rowSums(arr2D);
    for (int i = 0; i < sums.size(); i++) {
        for (int j = i + 1; j < sums.size(); j++) {
            if (sums[i] == sums[j]) {
                return false;
            }
        }
    }
    return true;
}

public class HiddenWord
{
    private String secret;

    public HiddenWord(String word) {
        secret = word;
    }

    public String getHint(String guess) {
        String result = "";
        for (int i = 0; i < guess.length(); i++) {
            if (guess.charAt(i) == secret.charAt(i)) {
                result += guess.charAt(i);
            } else if (secret.indexOf(guess.charAt(i)) != -1) {
                result += "+";
            } else {
                result += "*";
            }
        }
        return result;
    }
}

public int getValueAt(int row, int col) {
    for (SparseArrayEntry entry: entries) {
        if (entry.getRow() == row and entry.getCol() == col) {
            return entry.getValue();
        }
    }
    return 0;
}

public void removeColumn(int col) {
    int i = 0;
    while (i < entries.size()) {
        SparseArrayEntry entry = entries.get(i);
        if (entry.getCol() == col) {
            entries.remove(i);
        } else if (entry.getCol() > col) {
            entries.set(i, new SparseArrayEntry(entry.getRow(), entry.getCol() - 1, entry.getValue()));
            i += 1;
        } else {
            i += 1;
        }
    }
    numCols -= 1;
}

public interface NumberGroup
{
    boolean contains(int num);
}

public class Range implements NumberGroup
{
    int minValue;
    int maxValue;

    public Range(int min, int max) {
        minValue = min;
        maxValue = max;
    }

    public boolean contains(int num) {
        return minValue <= num and num <= maxValue;
    }
}

public boolean contains(int num) {
    for (int i = 0; i < groupList.size(); i++) {
        if (groupList.get(i).contains(num)) {
            return true;
        }
    }
    return false;
}
