def froggie(stone_heights):
    dp_list = [0] * len(stone_heights)
    dp_list[0], dp_list[1] = 0, abs(stone_heights[1]  - stone_heights[0])

    for index in range(2, len(stone_heights)):
        dp_list[index] = min(abs(stone_heights[index - 1] - stone_heights[index]) + dp_list[index - 1], abs(stone_heights[index - 2] - stone_heights[index]) + dp_list[index - 2])

    return dp_list[-1]


"""
heights = [10, 20, 30, 40, 20]
dp = [10, 10, 20, 30, 30]


dp[i] = min(abs(height[i] - height[i - 1]) + dp[i - 1], abs(height[i] - height[i - 2]) + dp[i - 2])

30 10 60 10 60 50

0 20 30 20 30 40 

"""


if __name__ == '__main__':
    stone_heights = [30, 10, 60, 10, 60, 50]
    stone_heights = [10, 30, 40, 20]
    print(froggie(stone_heights))

