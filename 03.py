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
