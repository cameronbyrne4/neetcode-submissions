#include <algorithm> 
#include <vector>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> poo;
        // Load nums into a hash map (nums[i] -> arbitrary counter)
        for (int i = 0; i< nums.size(); i++) {
            poo[nums[i]] = i; 
        }
        for (int i = 0; i < nums.size(); i++) {
            int diff = target-nums[i]; // want this diff to be somewhere in the table
            // can return i first without problem if we assume nums is sorted
            if (poo.find(diff) != poo.end()) {// found
                // poo.find(diff) = nums[j]
                int j = poo.find(diff)->second;
                if (i!=j) return {i, j};
            }
        }
    }
};

// O(n) is the solution!! I wanted to do .find() for every thing but i guess not
// Note; there are only 2 ints in the answer!
// Hint 1: use math. nums[j] = target - nums[i]

/*
hashmap of all elements
iterate thru nums
    calc the target - nums[i]
    FIND inside hashmap

IDEA: Do math then find instead of math for every element
 */