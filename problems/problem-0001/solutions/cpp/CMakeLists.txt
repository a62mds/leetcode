cmake_minimum_required(VERSION 3.10)

# set the project name and version
project(Problem-0001 VERSION 1.0)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# add the header-only library
add_library(Solution-0001 INTERFACE)

# add the test case executable
set(TEST_SOURCES
    Solution-0001.test.cpp
)
add_executable(Test-Solution-0001 "${TEST_SOURCES}")
target_include_directories(Test-Solution-0001 PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../../../../libs/cpp/external/doctest/doctest/")
target_link_libraries(Test-Solution-0001 PRIVATE Solution-0001)
