

def first_challenge(formatted_input):
    x = 0       # Initial horizontal position
    depth = 0   # Initial depth

    # Iterate over all commands and values in the input and
    # adjust the horizontal position and depth accordingly.
    for command, value in formatted_input:
        value = int(value)
        if command == 'forward':
            x += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value

    print('First challenge:')
    print('Final horizontal position:', x)
    print('Final depth:', depth)
    print('horizontal position * depth =', x * depth)


def second_challenge(formatted_input):
    x = 0       # Initial horizontal position
    depth = 0   # Initial depth
    aim = 0     # Initial aim

    # Iterate over all commands and values in the input and
    # adjust the horizontal position, aim and depth accordingly.
    for command, value in formatted_input:
        value = int(value)
        if command == 'forward':
            x += value
            depth += (aim * value)
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value

    print('Second challenge:')
    print('Final horizontal position:', x)
    print('Final depth:', depth)
    print('Final aim:', aim)
    print('horizontal position * depth =', x * depth)

if __name__ == '__main__':
    # Read input file
    with open('input.txt') as f:
        lines = [line.strip('\n').split() for line in f.readlines()]

    print('---------------------------------------')
    first_challenge(lines)
    print('---------------------------------------')
    second_challenge(lines)
    print('---------------------------------------')