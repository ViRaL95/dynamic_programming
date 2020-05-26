def k_stones(stone_choices: list, number_of_stones: int):
    dp_array = [False] * (number_of_stones + 1)

    for stone_number in range(1, number_of_stones + 1):
        for stone_choice in stone_choices:
            if stone_number - stone_choice >= 0 and not dp_array[stone_number - stone_choice]:
                dp_array[stone_number] = True

    return 'First' if dp_array[-1] else 'Second'


if __name__ == '__main__':
    stone_choices = [1]
    number_of_stones = 1000
    print(k_stones(stone_choices, number_of_stones))