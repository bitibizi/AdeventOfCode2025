def get_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
        content_lst = [line.strip('\n') for line in content]
        index = content_lst.index('')
        range_lst = [[int(num) for num in line.split('-')] for line in content_lst[0:index]]
        id_lst =[int(line) for line in content_lst[index+1:]]
        print(content_lst,id_lst)
        return range_lst, id_lst


def part1(range_lst, id_lst): 
    num = 0
    for i in id_lst:
        for j in range_lst:
            if j[0] <= i <= j[1]:
                num += 1
                break
    return num
    
if __name__ == "__main__":
    range_lst, id_lst = get_input('test.txt')
    print("First star:", part1(range_lst, id_lst))