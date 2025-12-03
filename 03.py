#need to do 2 passes through each number. The first finds the max and its index
#if the max is in the last position, find the second highest, these two are the answer
#otherwise, find the max after the original max in the string

with open("inputs/03.txt") as f:
    lines = [x.strip() for x in f.readlines()]

output_joltages = []
for line in lines:
    bank = [int(x) for x in line] 
    #get the max and its index
    bank_max = max(bank)
    bank_max_idx = bank.index(bank_max)

    if bank_max_idx == len(bank) - 1:
        first_digit = max(bank[:-1])
        output_joltages.append((first_digit * 10) + bank_max)
    else:
        second_digit = max(bank[bank_max_idx+1:])
        output_joltages.append((bank_max * 10) + second_digit)

print(output_joltages)
print(sum(output_joltages))

memo = {}

def recursive_find_best(overall_str, desired_len):
    #base case: string is as long as desired
    if len(overall_str) == 0:
        return -1
    if desired_len == 1:
        return max([int(x) for x in overall_str])

    options = []
    for i, c in enumerate(overall_str):
        if overall_str[i+1:] in memo and desired_len in memo[overall_str[i+1:]]:
            next = memo[overall_str[i+1:]][desired_len]
        else:
            if not overall_str[i+1:] in memo:
                memo[overall_str[i+1:]] = {}
            next = recursive_find_best(overall_str[i+1:], desired_len - 1)
            memo[overall_str[i+1:]][desired_len] = next
        if next == -1:
            continue
        options.append(int(f'{c}{next}'))
    
    if len(options) == 0:
        return -1

    return max(options)

pt2_total = 0
for line in lines:
    memo = {}
    pt2_total += recursive_find_best(line, 12)

print(pt2_total)