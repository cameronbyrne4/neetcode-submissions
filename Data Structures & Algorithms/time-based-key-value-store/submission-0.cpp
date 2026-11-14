class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> map;

    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        map[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
        string result = ""; // default in case set was never called
        int l = 0;
        int r = map[key].size()-1; // size of vector
        
        // print the entire vector real quick
        
        // stops when l == r
        while (l <= r) {
            
            int m = (l+r)/2;
            if (timestamp >= map[key][m].first) {
                result = map[key][m].second;
                l = m+1;
            }
            else if (timestamp < map[key][m].first) {
                // our time is too high, go left
                
                r = m-1;
            } else {
                l = m+1;
                
            }
        }
        return result;
    }
};
// Solution
        // while (left <= right) {
        //     int mid = left + (right - left) / 2;
        //     if (values[mid].first <= timestamp) {
        //         result = values[mid].second;
        //         left = mid + 1;
        //     } else {
        //         right = mid - 1;
        //     }
        // }