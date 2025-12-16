def get_input(file_path)->list[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        newList = content.strip().split(",")
        print(newList)
        return newList

def part(lst):
    
    
if __name__ == "__main__":
    lines = get_input('input.txt')
    # print("First star:", part1(lines))
    # print("Second star:", part2(lines))