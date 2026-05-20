class Solution {
    public boolean isValidSudoku(char[][] board) {
      HashSet<Character>[] rows= new HashSet[9];
      HashSet<Character>[] cols = new HashSet[9];
      HashSet<Character>[] box = new HashSet[9];

      for(int i=0;i<9;i++){
        rows[i] = new HashSet<>();
        cols[i] = new HashSet<>();
        box[i] = new HashSet<>();
      }
      for(int i=0; i<9;i++){
        for(int j=0;j<9; j++){
            char n = board[i][j];
            if(n == '.') continue;
            if(rows[i].contains(n)) return false;
            rows[i].add(n);
            if(cols[j].contains(n)) return false;
            cols[j].add(n);
            int boxIndex = (i/3)*3 + j/3;
            if(box[boxIndex].contains(n)) return false;
            box[boxIndex].add(n);
        }
      }
      return true;
    }
}
