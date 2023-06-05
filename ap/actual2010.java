public int getTotalBoxes() {
    int total = 0;
    for (CookieOrder order: orders) {
        total += order.getNumBoxes();
    }
    return total;
}

public int removeVariety(String cookieVar) {
    int total = 0;
    int index = 0;
    while (index < orders.size()) {
        if (orders.get(i).getVariety().equals(cookieVar)) {
            total += orders.get(i).getNumBoxes();
            orders.remove(i);
        } else {
            i += 1
        }
    }
    return total;
}

public class APLine
{
    private int A;
    private int B;
    private int C;

    public APLine(int a, int b, int c) {
        A = a;
        B = b;
        C = c;
    }

    public double getSlope() {
        return -a / (double) b;
    }

    public boolean isOnLine(int x, int y) {
        return A * x + B * y + C == 0;
    }
}

public boolean isLevelTrailSegment(int start, int end) {
    int maximum = markers[start];
    int minimum = markers[start];
    for (int i = start; i <= end; i++) {
        maximum = max(maximum, markers[i]);
        minimum = min(minimum, markers[i]);
    }
    return maximum - minimum <= 10;
}

public boolean isDifficult() {
    int changes = 0;
    for (int i = 0; i < markers.size() - 1; i++) {
        if (Math.abs(markers[i] - markers[i + 1]) >= 30) {
            changes += 1;
        }
    }
    return changes >= 3;
}

public Actor actorWithMostNeighbors() {
    if (gr.getOccupiedLocations().size() == 0) {
        return null;
    }
    Location maximum = gr.getOccupiedLocations().get(0);
    for (Location loc: gr.getOccupiedLocations()) {
        if (gr.getNeighbors(loc).size() > gr.getNeigbors(maximum).size()) {
            maximum = loc;
        }
    }
    return gr.get(maximum);
}

public List<Location> getOccupiedWithinTwo(Location loc) {
    List<Location> occupied = new ArrayList<Location>();
    for (Location neighbor: gr.getOccupiedLocations()) {
        if ((Math.abs(loc.getRow() - neighbor.getRow()) <= 2) and (Math.abs(loc.getCol() - neighbor.getCol()) <= 2) and (not neighbor.equals(loc)) {
            occupied.add(neighbor);
        }
    }
    return occupied;
}
