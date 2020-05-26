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


if __name__ == '__main__':
    N = 5
    recurse.total_probability = 0
    recurse(N, 0, N//2 + 1, 1, [0.42, 0.01, 0.42, 0.99, 0.42], 0)
    print(recurse.total_probability)