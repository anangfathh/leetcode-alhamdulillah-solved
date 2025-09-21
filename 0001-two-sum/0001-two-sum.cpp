class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prevMap;
        int n = nums.size();

        for (int i = 0; i < n; i++){
            int diff = target - nums[i];
            if (prevMap.find(diff) != prevMap.end()){
                return {prevMap[diff], i};
            }
            prevMap[nums[i]] = i;
        }
        return {};
    }
};