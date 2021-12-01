if __name__ == '__main__':
    # Read input file
    with open('input.txt') as f:
        lines = f.readlines()

    # Remove newline character at the end of each entry in the list and convert them to int
    lines = [int(line[:-1]) for line in lines]

    # Number of measurements that are larger than the previous one
    bigger_than_prev_count = 0

    for i in range(len(lines)):
        if i == 0:
            print(lines[i], '(N/A - no previous measurement)')
        else:
            if lines[i] > lines[i-1]:
                print(lines[i], '(increased)')
                bigger_than_prev_count += 1
            elif lines[i] < lines[i-1]:
                print(lines[i], '(decreased)')
            else:
                print(lines[i], '(no change)')

    print(bigger_than_prev_count, 'measurements were larger than the previous one.')
