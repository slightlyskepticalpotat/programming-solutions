import java.lang.Math;
import java.util.Scanner;

public class tle16c8p2 {
	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		for (int i = 0; i < t; i++) {
			String n = "", output = "";
			n = Integer.toBinaryString(scan.nextInt());
			for (int j = 0; j < n.length(); j++) { // iterate over characters
			 	char c = n.charAt(j);
				if (c == '0') {
					output += "meme ";
				} else {
					output += "dank ";
				}
			}
			System.out.println(output);
		}
	}
}