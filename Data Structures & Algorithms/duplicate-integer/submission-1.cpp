class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = 0;
        for (int i = n; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};