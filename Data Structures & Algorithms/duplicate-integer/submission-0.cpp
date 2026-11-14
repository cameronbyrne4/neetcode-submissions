#include <map>;
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // O(n^2) solution is possible fuck they want O(n) space and time
        // O(n) is the put in frequency map then find one with 2?
        unordered_map<int,int> freq;
        for (int i=0; i< nums.size(); i++) {
            freq[nums[i]]++;
            if (freq[nums[i]] > 1) {
                return true;
            }
        }
        return false;
    }
};
