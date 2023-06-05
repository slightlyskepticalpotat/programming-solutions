public boolean simulate() {
    int pos = 0;
    int jumps = 0;
    while ((jumps < maxHops and pos < goalDistance) and pos >= 0) {
        pos += hopDistance();
        jumps += 1;
    }
    return pos > goalDistance;
}

public double runSimulations(int num) {
    int win = 0;
    for (int i = 0; i < num; i++) {
        if (simulate()) {
            win += 1;
        }
    }
    return (double) win / num;
}

public WordPairList(String[] words) {
    allPairs = new ArrayList<WordPair>();
    for (int i = 0; i < words.length; i++) {
        for (int j = i + 1; j < words.length; j++) {
            allPairs.add(new WordPair(words[i], words[j]));
        }
    }
}

public int numMatches() {
    int matches = 0;
    for (WordPair pair: allPairs) {
        if (pair.getFirst().equals(pair.getSecond())) {
            matches += 1;
        }
    }
    return matches;
}

public interface StringChecker
{
    boolean isValid(String str);
}

public class CodeWordChecker implements StringChecker
{
    private int minLength;
    private int maxLength;
    private String mustNot;

    public CodeWordChecker(int minLen, int maxLen, String must) {
        minLength = minLen;
        maxLength = maxLen;
        mustNot = must;
    }

    public CodeWordChecker(String must) {
        minLength = 6;
        maxLength = 20;
        mustNot = must;
    }

    public boolean isValid(String str) {
        if (str.length() >= minLengt and str.length() <= maxLength and str.indexOf(mustNot) == -1) {
            return true;
        }
        return false;
    }
}

public static int[] getColumn(int[][] arr2D, int c) {
    int[] column = new int[arr2D.length];
    for (int i = 0; i < arr2D.length; i++) {
        column[i] = arr2D[i][c];
    }
    return column;
}

public static boolean isLatin(int[][] square) {
    if (containsDuplicates(square[0])) {
        return false;
    }
    for (int i = 0; i < square.length; i++) {
        if (not hasAllValues(square[0], square[i])) {
            return false;
        }
    }
    for (int i = 0; i < square[0].length; i++) {
        if (not hasAllValues(square[0], getColumn(square, i))) {
            return false;
        }
    }
    return true;
}
