#include <gtest/gtest.h>

int Sum(int a, int b)
{
    return a + b;
}

// Demonstrate some basic assertions.
TEST(SumTest, Sum)
{
    EXPECT_EQ(Sum(1, 1), 2);   // 1
    EXPECT_EQ(Sum(1, 1), 3);   // 2
}
