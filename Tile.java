/**
 *@author: Rishabh Dalal
 *description: Tile class to facilitate the edit-distance class
 *
*/

import java.util.ArrayList;

public class Tile{
		private int value;
		private ArrayList<int[]> arrow;
		private int x;
		private int y;
		
		Tile(int i, int j){
			arrow = new ArrayList();
			x = i;
			y = j;
		}
		
		int getValue() {
			return value;
		}
		
		int getX() {return x;}
		
		int getY() {return y;}
		
		void setValue(int aValue) {
			value = aValue;
		}
		
		boolean hasArrow() {
			if (arrow.size() > 0) return true;
			return false;
		}
		
		void setArrow(int x, int y) {
			int[] newArr = new int[2];
			newArr[0] = x;
			newArr[1] = y;
			arrow.add(newArr);
		}
		
		int[] getFirstArrow() throws Error{
			return arrow.get(0);
		}
	}
