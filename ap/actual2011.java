public int limitAmplitude(int limit) {
    int changes = 0;
    for (int i = 0; i < samples.length; i++) {
        if (samples[i] > limit) {
            samples[i] = limit;
            changes += 1;
        } elif (samples[i] < -limit) {
            samples[i] = -limit;
            changes += 1;
        }
    }
    return changes;
}

public void trimSilenceFromBeginning() {
    List<Integer> temp = new List<Integer>();
    boolean sound = false;
    for (int i = 0; i < samples.length; i++) {
        if (sound) {
            temp.add(samples[i]);
        } else {
            if (samples[i] != 0) {
                temp.add(samples[i]);
                sound = true;
            }
        }
    }
    samples = new int[temp.size()];
    for (int i = 0; i < temp.size(); i++) {
        samples[i] = temp.get(i);
    }
}

public class AttracticeCritter extends Critter
{
    public ArrayList<Acctor> getActors() {
        ArrayList<Actor> actors = new ArrayList<Actor>();
        for (Location loc: getGrid().getOccupiedLocations()) {
            if (not loc.equals(this.getLocation())) {
                actors.add(getGrid().get(loc));
            }
        }
        return actors;
    }

    public void processActors(ArrayList<Actor> actors) {
        for (Actor act: actors) {
            int direction = act.getLocation().getDirectionToward(getLocation());
            Location move = act.getLocation().getAdjacentLocation(direction);
            if (getgrid().get(move) == null) {
                act.moveTo(move);
            }
        }
    }
}

public int nextTankToFill(int threshold) {
    int minIndex = filler.getCurrentIndex();
    for (int i = 0; i < tanks.size(); i++) {
        if (tanks.get(i).getFuelLevel() <= threshold and tanks.get(i).getFuelLevel() < tanks.get(minIndex).getFuelLevel()) {
            minIndex = i;
        }
    }
    return minIndex;
}

public void moveToLocation(int locIndex) {
    if (not filler.isFacingRight()) {
        filler.changeDirection();
    }
    if (locIndex < filler.getCurrentIndex()) {
        filler.changeDirection();
    }
    if (filler.getCurrentIndex() != locIndex) {
        filler.moveForward(abs(locIndex - filler.getCurrentIndex()));
    }
}

private void fillBlock(String arr) {
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            if (((i + 1) * numCols + (j + 1)) > arr.length) {
                arr[i][j] = "A";
            } else {
                arr[i][j] = arr.charAt((i + 1) * numCols + (j + 1) - 1);
            }
        }
    }
}

public String encryptMessage(String message) {
    String encrypted = "";
    int blockLength = numRows * numCols;
    while (message.length() > 0) {
        blockLength = max(blockLength, message.length());
        fillBlock(message);
        encrypted += encryptBlock();
        message = message.substring(blockLength);
    }
    return encrypted;
}
