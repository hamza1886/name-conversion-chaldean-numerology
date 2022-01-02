alphabet_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                'F': 8, 'G': 3, 'H': 5,
                'I': 1, 'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
                'O': 7, 'P': 9,
                'Q': 1, 'R': 2, 'S': 3, 'T': 4,
                'U': 6, 'V': 6, 'W': 6,
                'X': 5, 'Y': 1, 'Z': 7}


def reduce_number_to_single_digit(num: int) -> int:
    return num if num <= 9 else reduce_number_to_single_digit(num - 9)


def map_name_to_number(names: list) -> dict:
    global alphabet_map
    name_num_map = {}

    for name in names:
        name_num_map[name] = reduce_number_to_single_digit(sum([alphabet_map[c] for c in name.upper()]))

    return name_num_map


if __name__ == '__main__':
    while True:
        try:
            user_input = input('\nEnter name (space separated): ')
            user_input_list = user_input.split()
            name_number_map = map_name_to_number(user_input_list)

            for key in name_number_map:
                # if name_number_map[key] == 1 or name_number_map[key] == 9:
                print(f'{key} = {name_number_map[key]}')
        except KeyboardInterrupt:
            exit()
