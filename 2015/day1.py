

if __name__ == "__main__":
    # execute only if run as a script
    with open('day1.txt') as f:
        read_data = f.readline()
    print(read_data)
    floor = 0
    for i, symbol in enumerate(read_data):
        if i == 0:
            print(i)
        if symbol == '(':
            floor = floor + 1
        if symbol == ')':
            floor = floor - 1
        if floor == -1:
            print(i)
    print(floor)
    
