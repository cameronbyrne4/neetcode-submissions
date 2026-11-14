class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size()-1;

        while (l <= r) {
            int m = (l+r)/2;
            if (nums[l] <= nums[m] && nums[m] <= nums[r]) {
                return nums[l];
            } else if (nums[m] <= nums[r]) {
                r = m; // no -1
            } else if (nums[l] <= nums[m]) {
                l = m+1;
            }
        }
        return -1;
    }
};

// we want l m r to be in order
// the smallest is at or below mid if mid and right are in order!
    // go left including mid
// cross halfway --> left and mid are in order!
    // go right excluding mid