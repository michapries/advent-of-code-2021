def first_challenge(formatted_input):

    # List that will contain the sums of each "column".
    # Initialized with 0 at every position.
    number_of_bits = len(formatted_input[0])
    sums = [0] * number_of_bits

    for binary in formatted_input:
        for i in range(number_of_bits):     # Remark: All binary entries have the same number of bits.
            sums[i] += int(binary[i])


    # Initialize epsilon and gamma rate.
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(number_of_bits):
        gamma_rate += '1' if sums[i] > (len(formatted_input) / 2) else '0'
        epsilon_rate += '0' if sums[i] > (len(formatted_input) / 2) else '1'

    # Print gamma rate and epsilon rate.
    # Converting from binary to decimal works via int casting with base 2.
    print(f'Gamma rate      binary: {gamma_rate}, decimal: {int(gamma_rate, 2)}')
    print(f'Epsilon rate    binary: {epsilon_rate}, decimal: {int(epsilon_rate, 2)}')
    print(f'gamma_rate * epsilon_rate = {int(gamma_rate, 2) * int(epsilon_rate, 2)}')

if __name__ == '__main__':
    # Read input as strings, not as integers.
    # This makes it easier to read off the bits.
    with open('input.txt') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    first_challenge(lines)