from copy import deepcopy

def first_challenge(formatted_input):

    # List that will contain the sums of each "column".
    # Initialized with 0 at every position.
    number_of_bits = len(formatted_input[0])
    sums = [0] * number_of_bits

    # TODO: change to list comprehension as in challenge 2
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


def second_challenge(formatted_input):

    number_of_bits = len(formatted_input[0])
    original_data = deepcopy(formatted_input)       # Deepcopying due to modifications on the input later on

    oxygen_rating, co2_rating = None, None

    # Iterate over all bits first
    for rating in ['oxygen', 'co2']:
        formatted_input = deepcopy(original_data)

        for i in range(number_of_bits):
            if len(formatted_input) == 1:
                break

            bit_sum = sum(int(entry[i]) for entry in formatted_input)       # Sum of the current bit column

            most_common_bit = 1 if bit_sum >= (len(formatted_input) / 2) else 0             # Most common bit of that particular bit column

            formatted_input = [binary for binary in formatted_input if (int(binary[i]) != most_common_bit and rating == 'co2') or (int(binary[i]) == most_common_bit and rating == 'oxygen')]

        if rating == 'oxygen':
            oxygen_rating = formatted_input[0]
            print(f'Oxygen rating   binary: {oxygen_rating}, decimal: {int(oxygen_rating, 2)}')
        else:
            co2_rating = formatted_input[0]
            print(f'CO2 rating      binary: {co2_rating}, decimal: {int(co2_rating, 2)}')

    print('oxygen_rating * co2_rating:', int(oxygen_rating, 2) * int(co2_rating, 2))


if __name__ == '__main__':
    # Read input as strings, not as integers.
    # This makes it easier to read off the bits.
    with open('input.txt') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    print('-' * 50)
    first_challenge(lines)
    print('-' * 50)
    second_challenge(lines)
    print('-' * 50)