#! /usr/bin/env python

def cleanup_input():
    cleaned = []
    with open('input.txt') as f:
        for line in f:
            clean_line = [ int(item) for item in line.split('\t') ]
            cleaned.append(clean_line)
    return cleaned


def generate_difference(line):
    return max(line) - min(line)


def generate_divisible(line):
    while len(line):
        item = line.pop()
        for remaining in line:
            if item % remaining == 0:
                return int(item / remaining)
            elif remaining % item == 0:
                return int(remaining / item)


def generate_checksum(checksum_type):
    checksum = 0
    cleaned_input = cleanup_input()
    for line in cleaned_input:
        if checksum_type == 'difference':
            line_check =  generate_difference(line)
        elif checksum_type == 'divisible':
            line_check = generate_divisible(line)
        else:
            print('checksum_type', checksum_type, 'is not supported!')
        checksum = checksum + line_check
    return checksum

print('The difference checksum is:', generate_checksum(checksum_type='difference'))
print('The divisible checksum is:', generate_checksum(checksum_type='divisible'))
