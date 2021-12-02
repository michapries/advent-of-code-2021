

def first_challenge(formatted_input):
    x = 0       # Initial horizontal position
    depth = 0   # Initial depth

    # Iterate over all directions and values in the input and
    # adjust the horizontal position and depth accordingly.
    for direction, value in formatted_input:
        value = int(value)
        if direction == 'forward':
            x += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value

    print('Final horizontal position:', x)
    print('Final depth:', depth)
    print('horizontal position * depth =', x * depth)

if __name__ == '__main__':
    # Read input file
    with open('input.txt') as f:
        lines = [line.strip('\n').split() for line in f.readlines()]

    first_challenge(lines)