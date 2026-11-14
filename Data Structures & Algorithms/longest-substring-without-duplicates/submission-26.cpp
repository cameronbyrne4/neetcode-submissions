class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int lenLongest = 0;
        int l = 0;
        
        unordered_set<char> cs;
        // Move r over the string
        for (int i = 0; i < s.size(); i++) {
            // if dupe
            while (cs.find(s[i]) != cs.end()) {
                cs.erase(s[l]);
                l++;
            }
            cs.insert(s[i]);
            lenLongest = max(lenLongest, i-l+1);
        }
        return lenLongest;
    }
};
/*
Want to move right until we run into a duplicate. Check for duplicates using a hash table?
    at this point, compare r-l index to the longest length
    move left pointer to the right until there is no longer a duplicate
*/
