class MinStack {

private:
        stack<int> stack1;
        stack<int> minStack;
        
public:
    MinStack() {
    }
    
    void push(int val) {
        stack1.push(val);
        val = minStack.empty()? val : min(val, minStack.top());
        minStack.push(val);
    }
    
    void pop() {
        stack1.pop();
        minStack.pop();
    }
    
    int top() {
        return stack1.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */