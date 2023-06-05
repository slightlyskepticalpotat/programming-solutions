public Digits(int num) {
    digitList = new ArrayList<Integer>();
    if (num == 0) {
        digitList.add(0);
    }
    while (num > 0) {
        digitList.add(0, num % 10);
        num /= 10;
    }
}

public boolean isStrictlyIncreasing() {
    boolean ans = true;
    for (int i = 1; i < digitList.size(); i++) {
        if (not digitList.get(i) > digitList.get(i - 1)) {
            ans = false;
        }
    }
    return ans;
}

public interface StudyPractice
{
    String getProblem();
    void nextProblem();
}

public class MultPractice implements StudyPractice
{
    private int firstInteger;
    private int secondInteger;

    public MultPractice(int first, int second) {
        firstInteger = first;
        secondInteger = second;
    }

    public String getProblem() {
        return firstInteger + " TIMES " + secondInteger;
    }

    public void nextProblem() {
        secondInteger += 1;
    }
}

public void replaceNthOccurrence(String str, int n, String repl) {
    int index = findNthOccurrence(str, n);
    if (index != -1) {
        currentPhrase = currentPhrase.substring(0, index) + repl + currentPhrase.substring(index + str.length());
    }
}

public int findLastOccurrence(String str) {
    int index = 1;
    while (findNthOccurrence(str, index + 1) != -1) {
        index += 1;
    }
    return findNthOccurrence(str, index);
}

public static Position findPosition(int num, int[][] intArr) {
    for (int i = 0; i < intArr.size(); i++) { // should use length here
        for (int j = 0; j < intArr[0].size(); j++) {
            if (intArr[i][j] == num) {
                return new Position(i, j);
            }
        }
    }
    return null;
}

public static Position[][] getSucessorArray(int[][] intArr) {
    Position[][] newArr = new Position[intArr.size()][intArr[0].size()];
    for (int i = 0; i < intArr.size(); i++) {
        for (int j = 0; j < intArr[0].size(); j++) {
            newArr[i][j] = findPosition(intArr[i][j] + 1, intArr);
        }
    }
    return newArr;
}
