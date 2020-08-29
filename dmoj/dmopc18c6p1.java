import java.util.Scanner;

public class dmopc18c6p1
{
	public static void main(String args[])
	{
		Scanner scan = new Scanner(System.in);
		boolean dna = true, rna = false;
		int n = scan.nextInt();
		String genes = scan.next();
		if (genes.matches("^[CGATU]+$")){ // check if genes only have these bases
			if (genes.contains("U")){
				if (genes.contains("T")) { // contains both T and U
					System.out.println("neither");
				} else {
					System.out.println("RNA");
				}
			} else if (genes.contains("T")) {
				System.out.println("DNA");
			} else {
				System.out.println("both");
			}
		} else {
			System.out.println("neither");
		}
	}
}