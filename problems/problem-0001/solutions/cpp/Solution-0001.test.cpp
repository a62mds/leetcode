#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"

#include "Solution-0001.h"


TEST_CASE("Test solution to problem 0001") {

    Solution solution;

    SUBCASE("Test indices of numbers that add to 9 in [2, 7, 11, 15] are [0, 1]") {
        vector<int> inputs{2, 7, 11, 15};
        int sum = 9;
        vector<int> outputs{0, 1};

        CHECK_EQ(solution.twoSum(inputs, sum), outputs);
    }

    SUBCASE("Test indices of numbers that add to 6 in [3, 2, 4] are [1, 2]") {
        vector<int> inputs{3, 2, 4};
        int sum = 6;
        vector<int> outputs{1, 2};

        CHECK_EQ(solution.twoSum(inputs, sum), outputs);
    }

    SUBCASE("Test indices of numbers that add to 6 in [3, 3] are [0, 1]") {
        vector<int> inputs{3, 3};
        int sum = 6;
        vector<int> outputs{0, 1};

        CHECK_EQ(solution.twoSum(inputs, sum), outputs);
    }

}
