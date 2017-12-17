#! /usr/bin/env python

def cleanup_input():
    with open('input.txt') as f:
        sequence = [int(jump) for jump in f]
    return sequence


def jump_sequence(sequence, part2=False):
    """
    >>> jump_sequence([0, 3, 0, 1, -3])
    5
    >>> jump_sequence([0, 3, 0, 1, -3], True)
    10
    >>> jump_sequence([0, -3, 0, 1, -3])
    3
    >>> jump_sequence([2, -3, 0, 1, -3])
    6
    """
    steps = 0
    position = 0
    while position >= 0 and position < len(sequence):
        try:
            value = sequence[position]
        except IndexError:
            break
        if part2 and value >= 3:
            sequence[position] -= 1
        else:
            sequence[position] += 1
        position += value
        steps += 1
    return steps


def solve_puzzle(part2=False):
    sequence = cleanup_input()
    exit = jump_sequence(sequence, part2)
    return exit


if __name__ == '__main__':
    print('The puzzle exit is:', solve_puzzle())
    print('The part 2 puzzle exit is:', solve_puzzle(True))
