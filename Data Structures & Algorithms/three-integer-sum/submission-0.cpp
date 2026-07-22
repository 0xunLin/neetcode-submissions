class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> result;

        for (int i = 0; i < nums.size(); i++) {
            unordered_map<int, int> seen;

            for (int j = i + 1; j < nums.size(); j++) {
                int third = -(nums[i] + nums[j]);

                
                if (seen.count(third)) {
                    vector<int> triplet = {nums[i], nums[j], third};
                    sort(triplet.begin(), triplet.end());
                    result.insert(triplet);
                }
                
                seen[nums[j]] = j; 
            }

        }

        return vector<vector<int>>(result.begin(), result.end());
    }
};
