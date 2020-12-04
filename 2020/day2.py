
def check_password(password):
    spacesplit = password.split()
    limits = [int(x) for x in spacesplit[0].split('-')] 
    letter = spacesplit[1][0]
    password = spacesplit[2]
    count = password.count(letter)
    # is_valid = count in range(limits[0], limits[1] + 1)
    first_valid = (letter == password[limits[0]-1])
    second_valid = (letter == password[limits[1]-1])
    is_valid = False
    if (first_valid and second_valid):
        is_valid = False
    elif (first_valid or second_valid):
        is_valid = True
    print(f"m/M:{limits}\tL:{letter}\tP:{password:20}\tC:{count}\tV:{is_valid}")
    return is_valid

if __name__ == "__main__":
    with open("day2.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        count = 0
        total = len(content)
        for password in content:
            if check_password(password):
                count += 1
    print(f"{count} of {total}")