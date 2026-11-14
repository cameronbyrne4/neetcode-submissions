class Solution {
public:
    int timeToEatPiles(vector<int>& piles, int k) {
        int time = 0;
        for (int i = 0; i < piles.size(); i++) {
            time += ((piles[i] + k - 1) / k);
        }
        return time;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        // IDEA: do a bin search where h is the upper calc :)
        // need to find the area where big one works and little one doesnt???
        // XXXXXOYYYYYYYYYYY
        int l = 1;
        int r = *max_element(piles.begin(), piles.end()); // should be the size of the largest pile
        // start at largest and eventually shrink it down
        int result = r;
        while (l <= r) {
            int mid = (l+r)/2;
            // CASE: this rate works --> we can look even smaller
            if (timeToEatPiles(piles, mid) <= h) {
                r = mid-1;
                result = mid;
            } else {
                // rate doesn't work and we need bigger bites
                l = mid+1;
            }
            
        }
        return result;
    }
    
};

// time in hours to eat a pile is piles[i] / k except with ceiling, aka round up
// (piles[i] + k - 1) / k
    // this only doesn't do anything if we are already at a multiple of k
