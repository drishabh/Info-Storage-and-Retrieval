import java.util.Scanner;

public class Edit_Distance {
	public static void main(String args[]) {
		String s1, s2;
		Scanner console = new Scanner(System.in);
		System.out.print("Enter the first word: ");
		s1 = console.nextLine();
		s1 = s1.replace("\n", "");

		System.out.print("Enter the second word: ");
		s2 = console.nextLine();
		s2 = s2.replace("\n", "");
		
		int ROW = s1.length();
		int COLUMN = s2.length();
		
		int[][] arr = new int[ROW+1][COLUMN+1];
		int i=0;

		for (i=0; i<=ROW; i++) {
			arr[i][0] = i;
			arr[0][i] = i;
		}

		for (i=1; i<=ROW; i++) {
			for (int j=1; j<=COLUMN; j++) {
				if (s1.charAt(i-1) == s2.charAt(j-1)) {
					arr[i][j] = Math.min(Math.min(arr[i-1][j]+1, arr[i][j-1]+1), arr[i-1][j-1]);
				}
				else {
					arr[i][j] = Math.min(Math.min(arr[i-1][j]+1, arr[i][j-1]+1), arr[i-1][j-1]+1);
				}
			}
		}

		System.out.println("The edit distance is: "+ arr[ROW][COLUMN]);
	}
}
