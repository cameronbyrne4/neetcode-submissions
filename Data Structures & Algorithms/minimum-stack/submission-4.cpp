class MinStack {
public:

    vector<int> burg;
    MinStack() {
        // LEAVE EMPTY
    }
    
    void push(int val) {
        burg.push_back(val);
    }
    
    void pop() {

        burg.erase(burg.end()-1);
    }
    
    int top() {
        return burg[burg.size()-1];
    }
    
    int getMin() {
        int mini = INT_MAX;
        for (int i : burg) {
            mini = min(i, mini);
        }
        return mini;
    }
};
