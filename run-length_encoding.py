""" From the "Daily Coding Problem" https://www.dailycodingproblem.com/

"Run-length encoding is a fast and simple method of encoding
strings. The basic idea is to represent repeated successive characters
as a single count and character. For example, the string
"AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string
to be encoded have no digits and consists solely of alphabetic
characters. You can assume the string to be decoded is valid."
"""

def encode(input_string):
    input_string = [char for char in input_string]
    sequence = []
    output = []

    while len(input_string) >= 1:
        if not sequence:
            sequence.append(input_string.pop(0))
        elif sequence[0] is input_string[0]:
            sequence.append(input_string.pop(0))
        else:
            output.append(str(len(sequence)) + sequence[0])
            sequence.clear()
    # Add the last sequence to the output.
    output.append(str(len(sequence)) + sequence[0])

    return ''.join(output)

    """
    ALTERNATIVE 2

    current_char_count = 1 # How many times current character appears in a row.
    input_string_len = len(input_string) - 1 # The length of the input string.

    for index, char in enumerate(input_string, 0):
        if index is not input_string_len: # Avoid "IndexError" if last char of the string
            if char is input_string[index + 1]:
                current_char_count += 1
            else:
                output.append(str(current_char_count) + char)
                current_char_count = 1
        else:
            output.append(str(current_char_count) + char)

    return ''.join(output)
    """

def decode(input_string):
    output = []
    for index, item in enumerate(input_string, 0):
        try:
            item_num = int(item)
        except TypeError:
            continue
        except ValueError:
            continue
        else:
            while item_num > 0:
                output.append(input_string[index + 1])
                item_num -= 1
    return ''.join(output)

def main():
    encoded_string = encode("AAAABBBCCDAAA")
    print(encoded_string)
    decoded_string = decode(encoded_string)
    print(decoded_string)

if __name__ == "__main__":
    main()
