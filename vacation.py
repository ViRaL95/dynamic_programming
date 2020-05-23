from typing import List


def get_max_points(vacations: List[List[int]]):
    """
                                        0
                   10                   40             70
            20     50     80       20   50  80      20 50 80






    :param vacations:
    :return:
    """
    dp_matrix = [[0] * len(vacations[0]) for row in vacations]
    dp_matrix[0], dp_matrix[1], dp_matrix[2] = vacations[0], vacations[1], vacations[2]
    print(dp_matrix)

    for row_index in range(1, len(dp_matrix)):
        for column_index in range(len(dp_matrix[0])):
            if column_index == 0:
                dp_matrix[row_index][column_index] = max(dp_matrix[row_index - 1][1], dp_matrix[row_index - 1][2]) + vacations[row_index][column_index]
            elif column_index == 1:
                dp_matrix[row_index][column_index] = max(dp_matrix[row_index - 1][0], dp_matrix[row_index - 1][2]) + vacations[row_index][column_index]
            else:
                dp_matrix[row_index][column_index] = max(dp_matrix[row_index - 1][0], dp_matrix[row_index - 1][1]) + vacations[row_index][column_index]

    return max(dp_matrix[-1])


if __name__ == '__main__':
    vacations = [
        [6, 7, 8],
        [8, 8, 3],
        [2, 5, 2],
        [7, 8, 6],
        [4, 6, 8],
        [2, 3, 4],
        [7, 5, 1],
    ]

    print(get_max_points(vacations))