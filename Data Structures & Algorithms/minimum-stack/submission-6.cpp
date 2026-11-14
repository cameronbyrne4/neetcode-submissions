class MinStack {
public:
    stack<int> minburg;
    stack<int> burg;
    MinStack() {
        // LEAVE EMPTY
    }
    
    void push(int val) {
        burg.push(val);
        // We compare the current min (the top of minburg) to the newest val, unless minburg has no top
        minburg.push(min(val, !minburg.empty() ? minburg.top() : val));
    }
    
    void pop() {
        burg.pop();
        minburg.pop();
        
    }
    
    int top() {
        return burg.top();
    }
    
    int getMin() {
        return minburg.top();
    }
};
