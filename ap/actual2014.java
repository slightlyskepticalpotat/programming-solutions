public static String scrambleWord(String word) {
    int i = 0;
    String result = "";
    while (i < word.length() - 1) {
        if (word.charAt(i).equals("A") and not word.charAt(i + 1).equals("A")) {
            result += word.charAt(i + 1) + word.charAt(i);
            i += 2;
        } else {
            result += word.charAt(i);
            i += 1;
        }
    }
    if (i < word.length()) {
        result += word.substring(i);
    }
    return result;
}

public static void scrambleOrRemove(List<String> wordList) {
    int i = 0;
    while (i < wordList.size()) {
        String test = wordList.get(i);
        if (test.equals(scrambleWord(test))) {
            wordList.remove(i);
        } else {
            wordList.set(i, scrambleWord(test));
            i += 1;
        }
    }
}

public class Director extends Rock
{
    public Director() {
        super(Color.RED);
    }

    public void act() {
        if (getColor().equals(Color.GREEN)) {
            ArrayList<Actor> adj = getGrid().getNeighbours(getLocation());
            for (Actor actor: adj) {
                actor.setDirection(actor.getDirection() + Location.RIGHT);
            }
            setColor(Color.RED);
        } else {
            setColor(Color.GREEN);
        }
    }
}

public SeatingChart(List<Student> studentList, int rows, int cols) {
    seats = Student[rows][cols];
    int seated = 0;
    for (int j = 0; j < cols; j++) {
        for (int i = 0; i < rows; i++) {
            if (seated < studentList.size()) {
                seats[i][j] = studentList.get(seated);
                seated += 1;
            }
        }
    }
}

public int removeAbsentStudents(int allowedAbsences) {
    int removed = 0
    for (int i = 0; i < seats.size(); i++) {
        for (int j = 0; j < seats[0].size(); j++) {
            if (not seats[i][j].equals(null) and seats[i][j].getAbsenceCount() > allowedAbsences) {
                seats[i][j] = null;
                removed += 1;
            }
        }
    }
    return removed;
}

public class Trio implements MenuItem
{
    private Sandwich t_sandwich;
    private Salad t_salad;
    private Drink t_drink;

    public Trio(Sandwich sandwich, Salad salad, Drink drink) {
        t_sandwich = sandwich;
        t_salad = salad;
        t_drink = drink;
    }

    public String getName() {
        return t_sandwich.getName() + "/" + t_salad.getName() + "/" + t_drink.getName() + " Trio";
    }

    public double getPrice() {
        return min(t_sandwich.getPrice() + t_salad.getPrice(), min(t_sandwich.getPrice() + t_drink.getPrice(), t_salad.getPrice() + t_drink.getPrice()));
    }
}
