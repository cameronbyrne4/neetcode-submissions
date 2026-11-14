class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // find which vector to work in
        // we only need l and r to calculate the median, so save that for once i fonud the vector
        // Preliminary round l and r
        // Runtime is LogM + logN = LogMN
        int l = 0;
        int r = matrix.size()-1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (matrix[mid][0] <= target && matrix[mid][matrix[mid].size()-1] >= target) {
                // working inside the right matrix
                l = 0;
                r = matrix[mid].size()-1;
                while (l <= r) {
                    int m = (l + r) / 2;
                    if (matrix[mid][m] == target) return true;
                    if (matrix[mid][m] > target) {
                        r = m - 1;
                    } else {
                        l = m + 1;
                    }

                }
                return false;
            }
            if (matrix[mid][0] > target){
                r = mid-1;
            } else {
                l = mid+1;
            }
        }
        return false;

        // idea: convert the matrix into a single array then do bin search: runtime is like O (M+N+logx) but space is ass

    }
};
