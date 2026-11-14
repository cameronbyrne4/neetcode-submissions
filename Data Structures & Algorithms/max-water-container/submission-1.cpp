class Solution {
public:
    int maxArea(vector<int>& heights) {
        
        int l = 0, r = heights.size()-1;
        int area = min(heights[l], heights[r]) * (r-l);
        int maxWater = area;
        while (l<r) {
            int area = min(heights[l], heights[r]) * (r-l);
            maxWater = max(maxWater,area);
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxWater;
    }
};
