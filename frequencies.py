"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(0, len(items)):
                   keyName = str(items[i])
                   frequencies[keyName] = items[i]
    return frequencies


