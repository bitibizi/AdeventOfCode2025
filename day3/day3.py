def get_input(file_path) -> list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
        new_list = [line.strip() for line in content]
        return new_list


def part1(lst):
    sum_num = 0
    for item in lst:
        num_lst = list(map(int, item))
        max_num = max(num_lst)
        max_num_index = num_lst.index(max_num)
        if max_num_index != len(num_lst) - 1:
            next_num = max(num_lst[max_num_index + 1:])
            result = max_num * 10 + next_num
        else:
            next_num = max(num_lst[:max_num_index])
            result = next_num * 10 + max_num
        sum_num += result
    return sum_num



if __name__ == "__main__":
    lines = get_input('test.txt')
    print("First star:", part1(lines))
    print("Second star:", part2(lines))