"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    frequency = 0
    length = len(items)
    for i in range(0, length):
        keyName = str(items[i])
        for i in range(0, len(items)):
            if str(items[i]) == keyName:
                frequency += 1
        frequencies[keyName] = frequency
    frequency = 0
    return frequencies