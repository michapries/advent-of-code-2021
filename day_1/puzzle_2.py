# Read input file
with open('input.txt') as f:
    lines = f.readlines()

# Remove newline character at the end of each entry in the list and convert them to int
lines = [int(line[:-1]) for line in lines]

# Sums of the sliding windows
sums = []

# Iterate over measurements
for i in range(len(lines)):
    if i < len(lines) - 2:
        sums.append(lines[i] + lines[i+1] + lines[i+2])

# Number of sliding window sums that are larger than the previous one
bigger_than_prev_count = 0

for j in range(len(sums)):
    if j == 0:
        print(sums[j], '(N/A - no previous sum)')
    elif sums[j] > sums[j - 1]:
        print(sums[j], '(increased)')
        bigger_than_prev_count += 1
    elif sums[j] < sums[j - 1]:
        print(sums[j], '(decreased)')
    else:
        print(sums[j], '(no change)')

print(bigger_than_prev_count, 'sums were larger than the previous one.')