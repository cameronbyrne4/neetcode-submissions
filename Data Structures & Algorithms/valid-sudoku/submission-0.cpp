class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check rows
        for (int i=0; i < 9; i++) {
            // Each row left to right:
            unordered_map<char,int> freqs;
            for (int j=0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                if (freqs.count(board[i][j]) == 1) { // already is in board
                    return false; 
                }
                freqs[board[i][j]]++;
            }
        }
        // Check columns
        for (int i=0; i < 9; i++) {
            // Each row left to right:
            unordered_map<char,int> freqs;
            for (int j=0; j < 9; j++) {
                if (board[j][i] == '.') continue;
                if (freqs.count(board[j][i]) == 1) { // already is in board
                    return false; 
                }
                freqs[board[j][i]]++;
            }
        }
        // Check squares
            // can either start in middle or at a corner (better), iteration is still iteration boy
        for (int i=0; i < 9; i+= 3) {
            // Each square via the top left
            for (int j=0; j < 9; j+=3) {
                unordered_map<char,int> freqs;
                for (int m = i; m < i+3; m++) {
                    for (int n = j; n < j+3; n++) {
                        if (board[m][n] == '.') continue;
                        if (freqs.count(board[m][n]) == 1) { // already is in board
                            return false; 
                        }
                        freqs[board[m][n]]++;
                    }
                }
            }
        }
        
        return true; // if nothing fails
    }
};
/*
    IDEA:
        - iterate thru every row, column, then the 9 boxes
            check via frequency table. anything not 0 or 1 is BAD
            if count is 1 and we wish to add, we KILL EVERYTHING
        - Should check O(n)
*/
