from pprint import pprint


def recurse(n, number_of_heads, minimum_num_heads, current_probability, probability_list, current_index):
    if current_index == n:
        if number_of_heads >= minimum_num_heads:
            recurse.total_probability += current_probability
        return

    for coin in ['H', 'T']:
        if coin == 'H':
            recurse(n, number_of_heads + 1, minimum_num_heads, current_probability * probability_list[current_index], probability_list, current_index + 1)
        else:
            recurse(n, number_of_heads, minimum_num_heads, current_probability * (1 - probability_list[current_index]), probability_list, current_index + 1)


def dp(n, probability_list):
    dp_matrix = [[0] * (n + 1) for row in range(n + 1)]


    for row_index in range(len(dp_matrix)):
        for column_index in range(len(dp_matrix[0])):
            pprint(dp_matrix)
            if row_index == 0:
                if column_index == 0:
                    dp_matrix[row_index][column_index] = 1
                break

            if column_index == 0:
                dp_matrix[row_index][column_index] = dp_matrix[row_index - 1][column_index] *\
                                                     (1 - probability_list[row_index - 1])

            else:
                dp_matrix[row_index][column_index] = dp_matrix[row_index - 1][column_index] * \
                                                     (1 - probability_list[row_index - 1]) + \
                                                     dp_matrix[row_index - 1][column_index - 1] * \
                                                     probability_list[row_index - 1]


    minimum_heads = n //2 + 1
    total_probability = 0
    for index in range(minimum_heads, len(dp_matrix)):
        total_probability += dp_matrix[-1][index]

    return total_probability


if __name__ == '__main__':
    N = 5
    print(dp(N, [0.42, 0.01, 0.42, 0.99, 0.42]))
    recurse.total_probability = 0
    recurse(N, 0, N//2 + 1, 1, [0.42, 0.01, 0.42, 0.99, 0.42], 0)
