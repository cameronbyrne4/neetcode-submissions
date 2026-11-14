class Solution {
public:
    bool isPalindrome(string s) {
        string alpha;
        for (const auto& c : s) {
            if (isalnum(c)) {
                alpha += tolower(c);
            }
        }

        int i = 0;
        while (i < alpha.size()/2) {
            if (alpha[i] != alpha[alpha.size() - 1 - i]) {
                return false;
            }
            i++;
        }
        return true;
            
    }
};
/*
    IDEA:
        take half of it and reverse sort it
        or read back and front at some time until idx is same
        O(n)
*/
