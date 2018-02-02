/**
 * @author: Rishabh Dalal
 * description: Levenshtein's distance calculation algorithm
 *
 */

import java.util.ArrayList;
import java.util.Scanner;

public class Edit_Distance {
	
    public static void main(String[] args) {
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
		
	Tile[][] arr = new Tile[ROW+1][COLUMN+1];
	int i=0, j=0;
		
	for(i=0; i<=ROW; i++) {
	    for (j=0; j<=COLUMN; j++) {
	        arr[i][j] = new Tile(i, j);
	    }
	}

	for (i=0; i<=ROW; i++) {
	    arr[i][0].setValue(i);
	    arr[0][i].setValue(i);
	    arr[i][0].setArrow(i-1, 0);
	    arr[0][i].setArrow(0, i-1);
	}

	int[] result = new int[3];
		
	for (i=1; i<=ROW; i++) {
	    for (j=1; j<=COLUMN; j++) {
	        if (s1.charAt(i-1) == s2.charAt(j-1)) {
	
    	            result = getMax(arr[i-1][j], arr[i][j-1], arr[i-1][j-1], true);
	        }
	        else {
	            result = getMax(arr[i-1][j], arr[i][j-1], arr[i-1][j-1], false);
	        }
	        arr[i][j].setValue(result[0]);
	        arr[i][j].setArrow(result[1], result[2]);
	    }
	}
		
	System.out.println();
		
	//Printing the intermediate table to reconfirm
	/*
	for(i=0; i<=ROW; i++) {
	    for (j=0; j<=COLUMN; j++) {
	        System.out.print(arr[i][j].getValue() + " ");
	    }
	    System.out.println();
	}
	*/
		
	System.out.println("Edit distance is:" + arr[ROW][COLUMN].getValue());
		
	// Printing the arrows to reconfirm
	/*
	for (i=0; i <= ROW; i++) {
	    for (j=0; j<= ROW; j++) {
	        int[] a = new int[2];
		a = arr[i][j].getFirstArrow();
		System.out.print(a[0] + "-" + a[1] + "  ");
	    }
	    System.out.println();
	}
	*/
		
	i=ROW;
	j=COLUMN;
	int newX, newY;
		
	String vertical = "";
	String horizontal = "";
		
	while (true) {
	    newX = arr[i][j].getFirstArrow()[0];
	    newY = arr[i][j].getFirstArrow()[1];
	    if ((newX <0) || (newY < 0)) {break;}
	    if (newX == i) {
	        vertical = "*" + vertical;
	        horizontal = s2.charAt(j-1) + horizontal;		
		}
	    else if(newY == j) {
		vertical = s1.charAt(i-1) + vertical;
		horizontal = "*" + horizontal;	
		}
	    else {
		vertical = s1.charAt(i-1) + vertical;
		horizontal = s2.charAt(j-1) + horizontal;
				
	    }
	    i = newX;
	    j = newY;
	    }
	    System.out.println("String1 : " + vertical + " \nString 2: " + horizontal);
	}
	
	private static int[] getMax(Tile a, Tile b, Tile c, boolean flag) {
	    // Doing comparisons and tracing the way back
		
	    int[] result = new int[3];
	    int add;
	    int aValue = a.getValue() + 1;
	    int bValue = b.getValue() + 1;
	    int cValue = c.getValue();
	    if (flag == true) {
			
	  	if ((aValue <= bValue) && (aValue <= cValue)){result[0] = aValue; add= 0;}
		else if ((bValue <= aValue) && (bValue <= cValue)){result[0] = bValue; add = 1;}
		else {result[0] = cValue; add=2;}
	    }
	    else {
	        cValue++;
		if ((aValue <= bValue) && (aValue <= cValue)){result[0] = aValue; add = 0;}
		    else if ((bValue <= aValue) && (bValue <= cValue)){result[0] = bValue; add = 1;}
		    else {result[0] = cValue; add = 2;}
		}
		
		if (add == 0) {
		    result[1] = a.getX();
		    result[2] = a.getY();
		}
		else if (add == 1) {
		    result[1] = b.getX();
		    result[2] = b.getY();
		}
		else {
		    result[1] = c.getX();
		    result[2] = c.getY();
		}
	    return result;
        }
}
