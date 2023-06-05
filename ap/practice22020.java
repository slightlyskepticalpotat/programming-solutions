public static int countA(WordSet s) {
    int a = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s.findkth(i + 1).substring(0, 1).equals("A")) {
            a += 1;
        }
    }
    return a;
}

public static void removeA(WordSet s) {
    int a = countA(s);
    for (int i = 0; i < a; i++) {
        s.remove(s.findkth(1));
    }
}

public class Outfit extends ClothingItem
{
    private Shoes shoes;
    private Pants pants;
    private Top top;

    public Outfit(Shoes s, Pants p, Top t) {
        shoes = s;
        pants = p;
        top = t;
    }

    public String getDescription() {
        return shoes.getDescription() + "/" + pants.getDescription() + "/" + top.getDescription() + " outfit";
    }

    public double getPrice() {
        double total = shoes.getPrice() + pants.getPrice() + top.getPrice();
        if ((total - shoes.getPrice() >= 100 or total - pants.getPrice() >= 100) or total - top.getPrice() >= 100) {
            return 0.75 * total;
        } else {
            return 0.9 * total;
        }
    }
}

public void printNotes() {
    int i = 1;
    for (Note note: noteList) {
        System.out.println(i + ". " + note.getNote());
        i += 1;
    }
}

public void removeNotes(String str) {
    int i = 0;
    while (i < noteList.size()) {
        if (noteList.get(i).getNote().indexOf(str) != -1) {
            noteList.remove(i);
        } else {
            i += 1;
        }
    }
}

public boolean twoTogether() {
    for (int i = 0; i < NUM_ROWS; i++) {
        for (int j = 0; j < SEATS_PER_ROW - 1; j++) {
            if (seats[i][j] == 0 and seats[i][j + 1] == 0) {
                seats[i][j] = 1;
                seats[i][j + 1] = 1;
                return true;
            }
        }
    }
    return false;
}

public int findAdjacent(int row, int seatsNeeded) {
    int start = -1;
    int current = 0;
    for (int i = 0; i < SEATS_PER_ROW; i++) {
        if (seats[row][i] == 0) {
            if (start == -1) {
                start = i;
            }
            current += 1;
        } else {
            start = -1;
            current = 0;
        }
    }
    if (current == seatsNeeded) {
        return start;
    }
    return -1;
}
