def froggie(stone_heights, k ):
    """
    3 ^ stone_heights time complexity

    k = 3
            1
     2          3         4
 3   4  5   4  5  6    5  6  7

    dp[i] = min(abs(stone_height[i] - stone_height[i -1]) + dp[i - 1],
                abs(stone_height[i] - stone_height[i - 2]) + dp[i - 2],
                abs(stone_height[i] - stone_height[i - k]) + dp[i - k])


    :param stone_heights:
    :param k:
    :return:
    """
    dp_list = [float("+inf")] * len(stone_heights)
    dp_list[0] = 0

    for index in range(1, len(stone_heights)):
        for num_stones_back in range(1, k + 1):
            if index - num_stones_back < 0:
                break

            dp_list[index] = min(abs(stone_heights[index] - stone_heights[index - num_stones_back]) +\
                                 dp_list [index - num_stones_back], dp_list[index])


    print()

    return 0 if dp_list[-1] == float("+inf") else dp_list[-1]


if __name__ == '__main__':
    print(froggie([10, 30, 40, 50, 20], 3))
    print(froggie([10, 20, 10], 1))
    print(froggie([10, 10], 100))
    print(froggie([40, 10, 20, 70, 80, 10, 20, 70, 80, 60], 4))
