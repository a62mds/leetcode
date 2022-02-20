// Solution-0001.h
#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        unordered_map<int, size_t> visited;
        for (size_t index=0; index < nums.size(); index++) {
            int current = nums[index];
            int required = target - current;
            if (visited.find(required) != visited.end()) {
                indices.push_back(visited[required]);
                indices.push_back(index);
                break;
            }
            else {
                visited[current] = index;
            }
        }
        return indices;
    }
};
