public class ComplexNumber
{
    private double real;
    private double imaginary;

    public ComplexNumber() {
        real = (double) 0;
        imaginary = (double) 0;
    }

    public ComplexNumber(double a, double b) {
        real = a;
        imaginary = b;
    }

    public double getReal() {
        return real;
    }

    public double getImaginary() {
        return imaginary;
    }

    public ComplexNumber addComplex(ComplexNumber a, ComplexNumber b) {
        return new ComplexNumber(a.getReal() + b.getReal(), a.getImaginary() + b.getImaginary());
    }

    public String toString() {
        return "(" + real + " + " + imaginary + "i)";
    }
}

public CoinCollectionTools(String country, int rows, int columns) {
    coinBox = new Coin[rows][columns];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            coinBox[i][j] = new Coin(country, 0, 0);
        }
    }
}

public Coin[][] fillCoinBox(ArrayList<Coin> myCoins) {
    int k = 0;
    for (int j = 0; j < coinBox[0].length; j++) {
        for (int i = 0; i < coinBox.length; i++) {
            if (k < myCoins.size()) {
                coinBox[i][j] = myCoins.get(k);
                k += 1;
            }
        }
    }
    return coinBox;
}

public ArrayList<Coin> fillCoinTypeList() {
    ArrayList<Coin> coins = new ArrayList<Coin>();
    for (int t = 1; t < 7; t++) {
        for (int j = 0; j < coinBox[0].length; j++) {
            for (int i = 0; i < coinBox.length; i++) {
                if (coinBox[i][j].getCoinType() == type) {
                    coins.add(coinBox[i][j]);
                }
            }
        }
    }
    return coins;
}

public class ComplexNumber
{
    private double a;
    private double b;

    public ComplexNumber() {
        a = 0.00;
        b = 0.00;
    }

    public ComplexNumber(double real, double imaginary) {
        a = real;
        b = imaginary;
    }

    public double getReal() {
        return a;
    }

    public double getImaginary() {
        return b;
    }

    public ComplexNumber add(ComplexNumber a, ComplexNumber b) {
        return new ComplexNumber(a.getReal() + b.getReal(), a.getImaginary() + b.getImaginary());
    }

    public String toString() {
        return "(" + a + " + " + b + "i)";
    }
}

public CoinCollectionTools(String country, int rows, int columns) {
    coinBox = new Coin[rows][columns];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            coinBox[i][j] = new Coin(country, 0, 0);
        }
    }
}

public Coin[][] fillCoinBox(ArrayList<Coin> myCoins) {
    int k = 0;
    for (int j = 0; j < coinBox[0].length; j++) {
        for (int i = 0; i < coinBox[0]; i++) {
            if (k < myCoins.size()) {
                coinBox[i][j] = myCoins.get(k);
                k += 1;
            }
        }
    }
}

public ArrayList<Coin> fillCoinTypeList() {
    ArrayList<Coin> coins = new ArrayList<Coin>();
    for (int k = 1; i < 7; i++) {
        for (int j = 0; j < coinBox[0].length; j++) {
            for (int i = 0; i < coinBox[0]; i++) {
                if (coinBox[i][j].getCoinType() == k) {
                    coins.add(coinBox[i][j]);
                }
            }
        }
    }
    return coins;
}
