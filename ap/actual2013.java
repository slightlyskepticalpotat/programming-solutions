public DownloadInfo getDownloadInfo(String title) {
    for (DownloadInfo download: downloadList) {
        if (download.getTitle().equals(title)) {
            return download;
        }
    }
    return null;
}

public void updateDownloads(List<String> titles) {
    for (String title: titles) {
        if (getDownloadInfo(title) != null;) {
            getDownloadInfo(title).incrementTimesDownloaded();
        } else {
            downloadList.add(new DownloadInfo(title));
        }
    }
}

public TokenPass(int playerCount) {
    board = new int[playerCount];
    for (int i = 0; i < playerCount; i++) {
        board[i] = (int) (Math.random() * 10) + 1;
    }
    currentPlayer = (int) (Math.random() * playerCount);
}

public void distributeCurrentPlayerTokens() {
    int tokensLeft = board[currentPlayer];
    int index = currentPlayer + 1;
    board[currentPlayer] = 0;
    while (tokensLeft > 0) {
        index = (index + 1) % board.length;
        board[index] += 1;
        tokensLeft -= 1;
    }
}

public static ArrayList<Location> getEmptyLocations(Grid<Actor> grid) {
    ArrayList<Location> empty = new ArrayList<Location>();
    for (int i = 0; i < grid.getNumRows(); i++) {
        for (int j = 0; j < grid.getNumCols(); j++) {
            if (grid.get(new Location(i, j)) == null) {
                empty.add(new Location(i, j));
            }
        }
    }
    return empty;
}

public class JumpingCritter extends Critter
{
    public ArrayList<Location> getMoveLocations() {
        return GridWorldUtilities.getEmptyLocations(getGrid());
    }

    public Location selectMoveLocation(ArrayList<Location> locations) {
        if (locations.size() == 0) {
            return null;
        } else {
            Location newLocation = locations.get((int) (Math.random() * locations.size()));
            return newLocation;
        }
    }
}

public SkyView(int numRows, int numCols, double[] scanned) {
    view = new double[numRows][numCols];
    int index = 0;
    for (int i = 0; i < numRows; i++) {
        if (i % 2 == 0) {
            for (int j = 0; j < numCols; j++) {
                view[i][j] = scanned[index];
                index += 1;
            }
        } else {
            for (int j = numCols - 1; j >= 0; j--) {
                view[i][j] = scanned[index];
                index += 1;
        }
    }
}

public double getAverage(int startRow, int endRow, int startCol, int endCol) {
    double total = (double) 0;
    for (int i = startRow; i <= endRow; i++) {
        for (int j = startCol; j <= endCol; j++) {
            total += view[i][j];
        }
    }
    return total / ((endRow - startRow + 1) * (endCol - startCol + 1));
}
