class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        // 0,1,2,3,4,5
        while (l <= r) {
            int mid = (l + r) / 2; // RECHECK THIS
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) {
                r = mid-1;
            } else {
                l = mid+1;
            }
        }
        return -1;
    }
};
