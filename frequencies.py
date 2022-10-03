"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(0, len(items)):
        keyName = str(items[i])
        freqeuncy = 0
        for i in range(0, len(items)):
            if str(items[i]) == keyName:
                number = 0
                number += 1
        frequency = number
        number = 0
    frequencies[keyName] = frequency
    return frequencies


