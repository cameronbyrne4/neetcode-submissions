class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProf = 0;
        int l = 0; // The buying prices
        // Iterate thru the selling prices!
        for (int i=0; i < prices.size(); i++) {
            // Optimal l is the prices[l] that is the smallest, but is reset if prices[i] is smaller?
            if (prices[i] < prices[l]) {
                l = i;
            }
            maxProf = max(maxProf, prices[i]-prices[l]);
        }
        return maxProf;
    }
};

/*
    IDEA:
    1. buy low sell hi
*/
