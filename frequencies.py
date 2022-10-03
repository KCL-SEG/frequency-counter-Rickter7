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
                frequency += 1
        frequencies[keyName] = frequency
    return frequencies


