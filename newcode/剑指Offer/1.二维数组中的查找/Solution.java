public class Solution {
    public boolean Find(int target, int [][] array) {
        int rows = array.length;
        if (rows == 0){
            return false;
        }
        int columns = array[0].length;
        if(columns == 0){
            return false;
        }
        
        int row = rows-1;
        int column = 0;
        
        while(row >= 0 && column <= columns -1){
            if(array[row][column] < target){
                column ++;
            } else if( array[row][column] > target){
                row --;
            } else{
                return true;
            }
        }
        return false;
    }
}