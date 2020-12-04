

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print(f"sum({partial})={target} *2={partial[0]*partial[1]}")
        if len(partial) == 3:
            print(f"*3={partial[0]*partial[1]*partial[2]}")
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    with open("day1.txt") as f:
        content = f.readlines()
        content = [int(x.strip()) for x in content] 
    print(content)
    subset_sum(content,2020)
