class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // put in buckets of freq from 1 to size of nums
        vector<vector<int>> buckets(nums.size()+1); // add bucket for 0
        unordered_map<int,int> what; // num --> freq
        for (const auto& num: nums) { // fill in freq table
            what[num]++;
        }
        // instead of sorting we put into another table LOOOOL
        for (const auto& pair : what) {
            buckets[pair.second].push_back(pair.first);
        }
        int n = k;
        vector<int> result;
        for (int i = buckets.size() - 1; i >= 0 ; i--) {
            for (const int& num : buckets[i]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result;  // Stop once we have k elements
                }
            }
        }
        return result;

    }
};

/*
IDEA
    sort,
    interate backwords
        add unique numbers to output until k is depleted

IDEA 2:
    make simple hash of freq
    iterate thru THAT

HINT 3:
    wtf is a bucket sort algo

RULES:
    no sort because it has to be O(n) wahhhhh time to use another
    fucking hash
*/