def get_input(file_path)->list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
        newList = [line.rstrip() for line in content]

        return newList
        
def part1(lst):
    point = 50
    password = 0
    for item in lst:
        if point == 0:
            password += 1
        number = int(item[1:])
        if item[0] == "L":
            diff = point - number
            point = diff % 100
        else:
            add = point + number
            point = add % 100

    return password  

def part2(lst):
    point = 50
    password = 0
    for item in lst:
        number = int(item[1:])
        if item[0] == "L":
            diff = point - number
            if diff <= 0:
                if point != 0:
                    password += 1
                password += int(-diff/100)
            point = diff % 100
        else:
            add = point + number
            point = add % 100
            if add >= 100:
                password += int(add/100)
    return password
            

if __name__ == "__main__":
    lines = get_input('input.txt')
    print("First star:", part1(lines))
    print("Second star:", part2(lines))