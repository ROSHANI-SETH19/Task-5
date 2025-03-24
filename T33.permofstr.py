def get_permutations(string):
    # Base case: if the string is empty or has only one character
    if len(string) <= 1:
        return [string]

    # Initialize an empty list to store the permutations
    permutations = []

    # Choose each character in the string as the first character
    for i, char in enumerate(string):
        # Get the remaining characters
        remaining_chars = string[:i] + string[i+1:]

        # Generate permutations for the remaining characters
        for perm in get_permutations(remaining_chars):
            # Add the chosen character to the beginning of each permutation
            permutations.append(char + perm)

    return permutations

# Example usage:
input_string = "abc"
permutations = get_permutations(input_string)
print(permutations)

import itertools

def get_permutations(string):
    return [''.join(perm) for perm in itertools.permutations(string)]

# Example usage:
input_string = "abc"
permutations = get_permutations(input_string)
print(permutations)