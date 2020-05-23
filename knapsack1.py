from typing import List
from pprint import pprint


def knapsack_1(max_weight, weight_to_value: List[List[int]]):
    dp_table = [[0] * (max_weight + 1) for item in range(len(weight_to_value))]

    for row_index in range(len(dp_table)):
        weight_of_item = weight_to_value[row_index][0]
        value_of_item = weight_to_value[row_index][1]

        for column_index in range(len(dp_table[0])):
            if weight_of_item > column_index:
                if row_index == 0:
                    dp_table[row_index][column_index] = 0
                else:
                    dp_table[row_index][column_index] = dp_table[row_index - 1][column_index]
            else:
                possible_answer = value_of_item
                if row_index == 0:
                    dp_table[row_index][column_index] = possible_answer
                else:
                    remaining_weight = column_index - weight_of_item
                    if row_index == 1 and column_index == 5:
                        print(f"weight of item is {weight_of_item} value is {value_of_item} remaining_weight is {remaining_weight} and {dp_table[row_index - 1][remaining_weight]}")
                    dp_table[row_index][column_index] = max(dp_table[row_index - 1][remaining_weight] + possible_answer, dp_table[row_index - 1][column_index])

    pprint(dp_table)
return dp_table[-1][-1]
if __name__ == '__main__':
    print(knapsack_1(15, [[6, 5], [5, 6], [6, 4], [6, 6], [3, 5], [7, 2]]))