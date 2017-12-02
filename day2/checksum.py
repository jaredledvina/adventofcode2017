#! /usr/bin/env python

def cleanup_input():
    cleaned = []
    with open('input.txt') as f:
        for line in f:
            clean_line = [ int(item) for item in line.split('\t') ]
            cleaned.append(clean_line)
    return cleaned

def generate_difference(item):
    return max(item) - min(item)

def generate_checksum():
    checksum = 0
    cleaned_input = cleanup_input()
    for line in cleaned_input:
        difference =  generate_difference(line)
        checksum = checksum + difference
    return checksum

print('Checksum is:', generate_checksum())
