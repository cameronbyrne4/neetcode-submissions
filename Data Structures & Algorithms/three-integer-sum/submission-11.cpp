class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;

        // For each MIDDLE, find a L and R that will negate it
        // oops, actually iterate thru each Left
        for (int i=0; i < nums.size(); i++) {
            int l = i+1, r = nums.size()-1;
            if (i>0 && nums[i] == nums[i-1]) continue; // Don't want dupes
            while (l<r) {
                if (-nums[i] != nums[l] + nums[r]) {
                    if  (0 < nums[i] + nums[l] + nums[r]) {
                        r--;
                    } else {
                        l++;
                    }
                } else {
                    result.push_back({nums[l],nums[i],nums[r]});
                    l++;
                    while (nums[l] == nums[l-1] && l<r) l++;
                }
            }
        }
        return result;
    }
};
/*
    Luckily we can do O(n^2) which means use each value to decrement the sum

    # groups of 3:
        If 5 elements 0 1 2 3 4:    10
            012
            013
            014
            023
            024
            034

            123
            124
            134

            234    

    But no duplicate sets allowed...

    IDEA:
    sort
*/
