public class RandomStringChooser
{
    private List<String> words;

    public RandomStringChooser(String[] strings) {
        words = new ArrayList<String>();
        for (String word: strings) {
            words.add(word);
        }
    }

    public String getNext() {
        if (words.size() > 0) {
            return words.remove((int) (Math.random() * words.size()));
        } else {
            return "NONE";
        }
    }
}

public RandomLetterChooser(String str) {
    super(getSingleLetters(str));
}

public LogMessage(String message) {
    int index = message.indexOf(":");
    machineId = message.substring(0, index);
    description = message.substring(index + 1);
}

public boolean containsWord(String keyword) {
    int index = description.indexOf(keyword);
    if (index != -1) {
        if (index == 0 || description.charAt(index - 1).equals(" ")) {
            if (index + keyword.length() == description.length() - 1 || description.charAt(index + keyword.length()).equals(" ")) {
                return true;
            }
        }
    }
    return false;
}

public List<LogMessage> removeMessages(String keyword) {
    List<LogMessage> messages = new ArrayList<LogMessage>();
    for (int i = 0; i < messageList.size(); i++) {
        if (messageList.get(i).containsWord(keyword)) {
            messages.add(messageList.remove(i));
            i -= 1;
        }
    }
    return messages;
}

private boolean toBeLabeled(int r, int c, boolean[][] blackSquares) {
    if (not blackSquares[r][c]) {
        if ((r == 0 || blackSquares[r - 1][c]) || (c == 0 || blackSquares[r][c - 1])) {
            return true;
        }
    }
    return false;
}

public Crossword(boolean[][] blackSquares) {
    int index = 1;
    puzzle = new Square[blackSquares.size()][blackSquares[0].size()];
    for (int i = 0; i < blackSquares.size(); i++) {
        for (int j = 0; j < blackSquares[0].size(); j++) {
            if (blackSquares[i][j]) {
                puzzle[i][j] = Square(true, 0);
            } else if (toBeLabelled(i, j, blackSquares)) {
                puzzle[i][j] = Square(false, index);
                index += 1;
            } else {
                puzzle[i][j] = Square(false, 0);
            }
        }
    }
}

public static int totalLetters(List<String> wordList) {
    int total = 0;
    for (String word: wordList) {
        total += word.length();
    }
    return total;
}

public static int basicGapWidth(List<String> wordList, int formattedLen) {
    return (formattedLen - totalLetters(wordList)) / (wordList.length() - 1);
}

public static String format(List<String> wordList, int formattedLen) {
    int base = basicGapWidth(wordList, formattedLen);
    int left = leftoverSpaces(wordList, formattedLen);
    String result = "";
    for (int i = 0; i < wordList.size(); i++) {
        result += wordList.get(i);
        if (i != wordList.size() - 1) {
            for (int j = 0; j < base; j++) {
                result += " ";
            }
            if (i < left) {
                result += " ";
            }
        }
    }
    return result;
}
