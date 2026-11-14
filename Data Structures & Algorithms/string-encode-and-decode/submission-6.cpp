class Solution {
public:

    string encode(vector<string>& strs) {
        string result;
        for (const auto& s : strs) {
            int size = s.size(); // better than counting each character LOL
            result += to_string(size) + '#' + s;
        }
        return result;
    }
    

    //input: "5#hello7#cameron3#bye"
    vector<string> decode(string s) {
        vector<string> result;
        // int size = stoi(s[0]); ILLEGAL
        int i=0;
        while (i < s.size()) {
            int j=i; // use this to locate the #. 
            while (s[j] != '#') {
                j++;
            }
            int wordSize = stoi(s.substr(i, j-i));
         
            string word = s.substr(j+1, wordSize);
            cout << word << ' ' << wordSize << " is " << s.substr(i, j-i) << endl;
            result.push_back(word);
            i = j+1+ wordSize;
        }
        return result;
    }
        
};
// put into string separated by ' '

// Topic: substrings
// Must use substring of a certain length in order to ignore all 
// characters of the string, refusing to see them as symbols that fuck us up