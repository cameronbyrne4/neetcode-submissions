class Solution {
public:
    bool isValid(string s) {
        stack<char> ms;
        for (const auto& c : s) {
            if ( c == ')' || c=='}' || c==']') {
                if (ms.empty()) {
                    return false; // There's no opening bracket for the closing one
                }
                if (c==')' &&  ms.top()=='(') {
                    ms.pop();
                } else if (c=='}' &&  ms.top()=='{') {
                    ms.pop();
                } else if (c==']' &&  ms.top()=='[') {
                    ms.pop();
                } else {
                    return false; // like ({)
                }
            } else {
                ms.push(c);
            }
            
        }
        if (ms.empty()) return true;
        return false;
    }
};
