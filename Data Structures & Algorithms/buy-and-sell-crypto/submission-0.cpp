class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProf = 0;
        int l = 0;
        // Note: buy low, sell high
        for (int i=0; i< prices.size(); i++) {
            if (prices[i] < prices[l]) {
                l = i;
            } else {
                maxProf = max(maxProf, prices[i] - prices[l]);
            }
        }


        return maxProf;
    }
};
