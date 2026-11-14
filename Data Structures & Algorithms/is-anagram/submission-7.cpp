using namespace std;
#include <map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        // IDEA: unordered map for freq see if they the same? O(n)
        // create unordered map for both. go thru them and see if same
        // BETTER. MAKE ONE UNORDERED MAP AND DO STACK OPERATIONS (+S/-T)
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char,int> goggin;
        // They are the same size:
        for (int i=0; i< s.size(); i++) {
            goggin[s[i]]++;
            goggin[t[i]]--;
        } // default val is 0?
        for (const auto &pair : goggin) {
            if (pair.second != 0) {
                return false;
            }
        }
        return true;
    }
};
