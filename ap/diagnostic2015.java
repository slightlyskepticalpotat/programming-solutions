public static void reverseArray(int[] arr)
{
    int[arr.length] arr2;
    for (int i = 0; i < arr.length; i++) {
        arr2[i] = arr[arr.length - 1 - i];
    }
    arr = arr2;
}

public void reverseAllRows()
{
    for (int i = 0; i < mat.length; i++) {
        reverseArray(mat[i])
    }
}

public void reverseMatrix()
{
    reverseAllRows();
    int[mat.length][mat[0].length] mat2;
    for (int i = 0; i < mat.length; i++) {
        mat2[i] = mat[mat.length - 1 - i];
    }
    mat = mat2;
}

public List<Integer> getBlankPositions()
{
    List<Integer> blank_positions = new ArrayList<Integer>();
    for (int i = 0; i < sentence.length(); i++) {
        if (sentence.substring(i, i + 1).equals(" ")) {
            blank_positions,add(i);
        }
    }
    return blank_positions;
}

public int countWords()
{
    return getBlankPositions().size() + 1;
}

public String[] getWords()
{ // forgot the first element here :()
    String[countWords()] final_words;
    List<Integer> blank_positions = getBlankPositions();
    for (int i = 0; i < countWords() - 1; i++) {
        final_words[i] = sentence.substring(blank_positions[i] + 1, blank_positions[i + 1]);
    }
    final_words[final_words.length() - 1] = sentence.substring(blank_positions[blank_positions.length() - 1] + 1);
    return final_words;
}

public Player requestSlot(String playerName)
{
    for (int i = 0; i < 100; i++) {
        if (slots[i] == null) {
            Player new_player = new Player(playerName, i);
            slots[i] = new_player
            return new_player;
        }
    }
    waitingList.add(playerName);
    return null;
}

public Player cancelAndReassignSlot(Player p)
{
    int ree = getPlayerNumber(p);
    slots[ree] = null;
    if (waitingList.size() > 0) {
        slots[ree] = new Player(waitingList[0], i);
        waitingList.remove(0);
    }
    return slots[i];
}

public void reset()
{
    if (arm.isFacingRight()) {
        arm.changeDirection();
    }
    arm.moveForward(arm.getCurrentIndex());
    arm.changeDirection();
}

public int mostAcidic() {
    int any_acidic = 0;
    int lowest_acidic = Integer.MAX_VALUE;
    int lowest_acidic_index = -1;
    for (int i = 0; i < solutions.length; i++) {
        if (solutions[i].getPH() < 7) {
            any_acidic = 1;
        }
        if (solutions[i].getPH() < lowest_acidic) {
            lowest_acidic = solutions[i].getPH();
            lowest_acidic_index = i;
        }
    }
    reset()
    if (any_acidic) {
        moveForward(lowest_acidic_index);
        return lowest_acidic_index;
    } else {
        return -1;
    }
}
