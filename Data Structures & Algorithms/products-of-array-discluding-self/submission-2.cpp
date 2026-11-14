class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> res(size);
        vector<int> left(size);
        vector<int> right(size);
        int leftProd = 1;
        for (int i=0; i < nums.size(); i++) {
            left[i] = leftProd;
            leftProd *= nums[i];
        } 
        int rightProd = 1;
        for (int i=nums.size()-1; i >= 0; i--) {
            right[i] = rightProd;
            rightProd *= nums[i];
        }

        for (int i=0; i < nums.size(); i++) {
            res[i] = left[i] * right[i];
        } 

        return res;
    }
};
