class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        
         // what about when length is 1? just return it?
        for (string t : tokens) {
            
            if (t == "+") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                st.push(a+b);
            } else if (t == "-") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                st.push(a-b);
            } else if (t == "*") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                st.push(a*b);
            } else if (t == "/") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();
                int div = a/b;
                // if theres a remainder
                
                st.push(div);
            } else { // adding a number
                st.push(stoi(t));
            }
        }
        return st.top();
    }
};
/*
Add numbers to the stack
When something happens we pop the top 2, then push the result on it
Division is weird
*/