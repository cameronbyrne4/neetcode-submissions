class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size();
        if (n  > s2.size()) return false;
        unordered_map<char,int> cm1; // "char map"
        unordered_map<char,int> cm2;

        // Put s1 into map for comparisons
        for (const auto& c : s1) {
            cm1[c]++;
        }

        // Iterate over s2 in a fixed window
        for (int i = 0; i < n; i++) { // fill up with first chars up to n size
            cm2[s2[i]]++;
        }
        if (cm1 == cm2) return true;
        
        for (int i = n; i < s2.size(); i++) {
            // Shift everything over one DEFO BETTER TO USE l and r THOUGH RIGHT SOMEHOW?
            cm2[s2[i]]++;
            cm2[s2[i-n]]--;
            if (cm2[s2[i-n]] == 0) cm2.erase(s2[i-n]);
            // print current segment
            for (const auto& pair : cm2) {
                cout << pair.first << pair.second << ' ';
            }
            cout << endl;
            if (cm1 == cm2) return true;
        }

        // If that doesn't work
        return false;

    }
};
/*
One possible idea is to sort s1, then also sort the substr of s2 of that length

I will try to check freq with a hash table that updates properly

if maps are the same, return true!
otherwise we add the current term to hash and remove the i-n term
*/