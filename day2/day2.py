def get_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        new_list = content.strip().split(",")
        second_list = [list(map(int, item.strip().split("-"))) for item in new_list]
    return second_list

def part1(lst):
    sum_num = 0
    for item in lst:
        x = range(item[0], item[-1] + 1)
        for number in x:
            if len(str(number)) % 2 == 1 :
                continue
            half = int(len(str(number)) / 2)
            num_lst = list(map(int, str(number)))
            first_part = num_lst[:half]
            second_part = num_lst[half:]
            if first_part == second_part:
                sum_num += number
    return sum_num

def part2(lst):
    sum_num = 0
    for item in lst:
        x = range(item[0], item[-1] + 1)
        for number in x:
            found_pattern = False
            str_num = str(number)
            length = len(str_num)
            max_size_pattern = int(len(str_num)/2)
            for i in range(1, max_size_pattern+1):
                if length % i == 0:
                    current_pattern_ok = True
                    for j in range(0, length):
                        if str_num[j] != str_num[j % i]:
                            current_pattern_ok = False
                            break
                    if current_pattern_ok:
                        found_pattern = True
                        break
            if found_pattern:
                sum_num += number

    return sum_num

def part2_optimized(lst):
    sum_num = 0
    for start, end in lst:
        for num in range(start, end + 1):
            s = str(num)
            length = len(s)
            half_len = length//2
            found_pattern = False
            for p in range(1, half_len + 1):
                if length % p != 0:
                    continue
                pattern = s[:p]
                if pattern * (length // p) == s:
                    found_pattern = True
                    break
            if found_pattern:
                sum_num += num
    return sum_num



if __name__ == "__main__":
    lines = get_input('input.txt')
    print("First star:", part1(lines))
    print("Second star:", part2_optimized(lines))