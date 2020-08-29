import java.util.Scanner;
import java.lang.Math;

public class coci06c5p2 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		String[] line1 = scan.nextLine().split(":");
		int h1 = Integer.parseInt(line1[0]), m1 = Integer.parseInt(line1[1]), s1 = Integer.parseInt(line1[2]);
		String[] line2 = scan.nextLine().split(":");
		int h2 = Integer.parseInt(line2[0]), m2 = Integer.parseInt(line2[1]), s2 = Integer.parseInt(line2[2]);
		int time1 = 3600 * h1 + 60 * m1 + s1;
		int time2 = 3600 * h2 + 60 * m2 + s2;
		if (time2 == time1) { // same time
			System.out.println("24:00:00");
			System.exit(0);
		} else if (time2 < time1) { // next day
			time2 += 86400;
		}
		int difference = Math.abs(time1 - time2);
		System.out.println(String.format("%02d", difference / 3600) + ":" + String.format("%02d", (difference % 3600) / 60)+ ":" + String.format("%02d", (difference % 3600) % 60));
	}
}