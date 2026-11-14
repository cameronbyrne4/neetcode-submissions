#include <vector>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> hash;
        // anagram == same freq of chars (via vector of 26)
        for (int i = 0; i < strs.size(); i++) {
            vector<int> alphabet(26,0);
            for (auto& c : strs[i]) {
                alphabet[c-'a']++; // characters can be used as index, but must first be shifted
            }
            // Hidden tech: turn vector into a string real fast
            string key = to_string(alphabet[0]);
            for (int j=0; j < 26; j++) {
                key += '|' + to_string(alphabet[j]);
            }

            // increment this anagram's count in hash
            hash[key].push_back(strs[i]); // Is this okay???
        }

        // Strings now grouped by anagram
        // NOTE: iterate thru hash table using auto pairs!
        for (const auto& pair : hash) {
            result.push_back(pair.second); // pair.second is the vector of applicable strings
        }
        return result;
    }
};

// group vectors by anagram status
// IDEA: O(m*n)
    // vector of unordered map with freq for all thingos
    // then go thru it to match them

// Hint 1: cameron ur dumb, why group using

// instead of a vector of hash tables, we are making a hash table where arrays are the key!!!