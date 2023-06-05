public void addClimb(String peakName, int climbTime) {
    climbList.add(new ClimbInfo(peakName, climbTime));
}

public void addClimb(String peakName, int climbTime) {
    for (int i = 0; i < climbList.size(); i++) {
        if (peakName.compareTo(climbList.get(i).getName()) <= 0) {
            climbList.add(i, new climbInfo(peakName, climbName));
            return;
        }
    }
    climbList.add(new ClimbInfo(peakName, climbTime));
}

// NO
// YES

public class RetroBug extends Bug
{
    Location prevLocation;
    int prevDirection;

    public void act() {
        prevLocation = getLocation();
        prevDirection = getDirection();
        super.act();
    }

    public void restore() {
        if (prevLocation != null) {
            setDirection(prevDirection);
            if (getGrid().get(prevLocation) == null or getGrid().get(prevLocation) instanceof Flower) {
                moveto(prevLocation);
            }
        }
    }
}

public int findHorseSpace(String name) {
    for (int i = 0; i < spaces.length; i++) {
        if (spaces[i] != null and name.equals(spaces[i].getName())) {
            return i;
        }
    }
    return -1;
}

public void consolidate() {
    Horse[] newBarn = new Horse[spaces.length];
    int index = 0;
    for (int i = 0; i < spaces.length; i++) {
        if (spaces[i] != null) {
            newBarn[index] = spaces[i];
            index += 1;
        }
    }
    spaces = newBarn;
}

public int countWhitePixels() {
    int whitePixels = 0;
    for (int[] row: pixelValues) {
        for (int pixel: row) {
            if (pixel == WHITE) {
                whitePixels += 1;
            }
        }
    }
    return whitePixels;
}

public void processImage() {
    for (int i = 0; i < pixelValues.length - 2; i++) {
        for (int j = 0; j < pixelValues[0].length - 2; j++) {
            pixelValues[i][j] -= pixelValues[i + 2][j + 2];
            if (pixelValues[i][j] < BLACK) {
                pixelValues[i][j] = max(pixelValues[i][j], BLACK);
            }
        }
    }
}
