#!/usr/bin/env python3


def string_bits(str):
    """Returns a new string made of every other char starting with the first"""
    number_of_letters = len(str)
    odd_str = ''
    for i in range(number_of_letters):
        if i % 2 == 0:
            odd_str = odd_str + str[i]
    return odd_str

if __name__ == "__main__":
    """Print successul message if function
    outputs the expected values for known string inputs
    """
    assert string_bits('Hello') == 'Hlo'
    assert string_bits('Hi') == 'H'
    assert string_bits('Heeololeo') == 'Hello'

    print("Tests Passed")
