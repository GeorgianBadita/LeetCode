// https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/782/


class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        if(nums.empty()){
            if(lower == upper){
                return {to_string(lower)};
            }
            return {to_string(lower) + "->" + to_string(upper)};
        }
        vector<string> solution;
        if(nums[0] > lower){
            if(nums[0] - 1 == lower){
                solution.push_back(to_string(lower));
            } else {
                solution.push_back(to_string(lower) + "->" + to_string(nums[0]  - 1));
            }
        }
        for(int i = 0; i<nums.size() - 1; i++){
            if(nums[i] + 1 == nums[i + 1] - 1){
                solution.push_back(to_string(nums[i] + 1));
            }else if(nums[i + 1] - nums[i] > 1){
                string stringToAdd = to_string(nums[i] + 1) + "->" + to_string(nums[i + 1] - 1);
                solution.push_back(stringToAdd);
            }
        }
        if(nums[nums.size() - 1] < upper) {
            if(upper - 1 == nums[nums.size() - 1]) {
                solution.push_back(to_string(upper));
            }else{
                solution.push_back(to_string(nums[nums.size() - 1] + 1) + "->" + to_string(upper));
            }
        }

        return solution;
    }
};