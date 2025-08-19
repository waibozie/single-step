cmake_minimum_required(VERSION 3.31)
project(step-faraway)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/v1.17.0.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
include(GoogleTest)
enable_testing()

add_executable(
        solution
        solution_sum.cc
)
target_link_libraries(
        solution
        GTest::gtest_main
)
gtest_discover_tests(solution)
