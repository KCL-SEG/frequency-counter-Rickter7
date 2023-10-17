
"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    
    for i in range(len(items)):
        key = str(items[i])
        count = 0
        for i in range(len(items)):
            if str(items[i]) == key:
                count += 1
        if key not in frequencies:
            frequencies[key] = count
    return frequencies