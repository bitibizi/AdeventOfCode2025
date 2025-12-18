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
            
    
if __name__ == "__main__":
    lines = get_input('input.txt')
    print("First star:", part1(lines))
    # print("Second star:", part2(lines))