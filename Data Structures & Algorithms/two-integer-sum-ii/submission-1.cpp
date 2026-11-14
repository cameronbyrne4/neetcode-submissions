class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int a = 0;
        int b = numbers.size()-1;

        while (numbers[a] + numbers[b] != target) {
            if (numbers[a] + numbers[b] < target) {
                a++;
            } else {
                b--;
            }
        }
        
        return {a+1,b+1};
        

        
    }
};

/*
    O(n^2) is easy but nah
    ex 12589, target = 7
        1 9
        1 8
        1 5
        2 5
    So if we are too big, R--, and too small L++???
*/
