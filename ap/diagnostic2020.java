public void reset() {
    if (arm.isFacingRight()) {
        arm.changeDirection();
    }
    arm.moveForward(arm.getCurrentPos());
    arm.changeDirection();
}

public int mostAcidic() {
    reset();
    int mostAcidicIndex = -1;
    int mostAcidic = 7;
    if (s0.getPH() < mostAcidic) {
        mostAcidic = s0.getPH();
        mostAcidicIndex = s0.getPos();;
    }
    if (s1.getPH() < mostAcidic) {
        mostAcidic = s1.getPH();
        mostAcidicIndex = s1.getPos();
    }
    if (s2.getPH() < mostAcidic) {
        mostAcidic = s2.getPH();
        mostAcidicIndex = s2.getPos();
    }
    if (mostAcidicIndex != -1) {
        arm.moveForward(mostAcidicIndex);
    }
    return mostAcidicIndex;
}

public class Cruise
{
    private int peopleSignedUp;
    private int currentPrice;

    public void Cruise(int people, int price) {
        peopleSignedUp = people;
        currentPrice = price;
    }

    public void setPrice(int price) {
        currentPrice = price;
    }

    public void checkResponse(String response) {
        if (response.indexOf("cruise") != -1) {
            peopleSignedUp += 1;
        }
    }

    public int calculateRevenue() {
        return peopleSignedUp * currentPrice;
        // read spec carefully next time, conditional pricing
    }
}

public ArrayList<Integer> getBlankPositions() {
    ArrayList<Integer> spaces = new ArrayList<Integer>();
    for (int i = 0; i < sentence.length(); i++) {
        if (sentence.substring(i, i + 1).equals(" ")) {
            spaces.add(i);
        }
    }
    return spaces;
}

public String[] getWords() {
    int n = countWords();
    String[] words = new String[n];
    ArrayList<Integer> spaces = getBlankPositions();
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            if (spaces.size() != 0) {
                words[i] = sentence.substring(0, spaces.get(0));
            } else {
                words[i] = sentence;
            }
        } else if (i == spaces.size()) {
            words[i] = sentence.substring(spaces.get(i - 1) + 1)
        } else {
            words[i] = sentence.substring(spaces.get(i - 1) + 1, spaces.get(i));
        }
    }
    return words;
}


public void reverseAllRows() {
    for (int[] row: mat) {
        ArrayUtil.reverseArray(row);
    }
}

public void reverseMatrix() {
    reverseAllRows();
    int[] temp;
    for (int i = 0; i < mat.length / 2; i++) {
        temp = mat[mat.length - i - 1];
        mat[mat.length - i - 1] = mat[i];
        mat[i] = mat[mat.length - i - 1];
    }
}
