import java.util.Scanner;

public class saoj2 {
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        long n = scan.nextLong();
        System.out.printf("#include <bits/stdc++.h>\n");
        System.out.printf("using namespace std; int main(){printf(\"%%llu\\n\", %d);}\n", ((n) * (n + 1)) / 2);
    }
}