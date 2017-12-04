#! /usr/bin/env python
from collections import defaultdict


def get_position(distance):
    """
    >>> get_position(1)
    (0, 0)
    >>> get_position(12)
    (2, 1)
    >>> get_position(23)
    (0, -2)
    """
    # Directions
    right = 0
    up = 1
    left = 2
    down = 3
    # Start
    x = 0
    y = 0
    direction = 0 # Start going right
    direction_change = 0
    steps = 0
    max_steps = 1

    for step in range(1, distance):
        if direction == right:
            x += 1
        elif direction == up:
            y += 1
        elif direction == left:
            x -= 1
        elif direction == down:
            y -= 1

        steps += 1
        if steps == max_steps:
            steps = 0
            direction_change += 1
            direction = (direction + 1) % 4
            # Max steps increases by one on evens
            if direction_change % 2 == 0:
                max_steps += 1
    return x, y


def check_distance(distance):
    """
    >>> check_distance(1)
    0
    >>> check_distance(12)
    3
    >>> check_distance(23)
    2
    >>> check_distance(1024)
    31
    """
    x, y = get_position(distance)
    return abs(x) + abs(y)


def squared_square(maximum):
    """
    >>> squared_square(4)
    2
    >>> squared_square(147)
    142
    >>> squared_square(806)
    747
    """
    # Directions
    right = 0
    up = 1
    left = 2
    down = 3
    # Start
    x = 0
    y = 0
    direction = 0 # Start going right
    direction_change = 0
    steps = 0
    max_steps = 1

    # State
    location_bits = {
        (0, 0): 1
    }

    previous_sum = 1
    while previous_sum < maximum:
        previous_location = (x, y)
        if direction == right:
            x += 1
        elif direction == up:
            y += 1
        elif direction == left:
            x -= 1
        elif direction == down:
            y -= 1

        steps += 1
        new_sum = 0
        new_sum += location_bits.get((x - 1, y), 0)
        new_sum += location_bits.get((x + 1, y), 0 )
        new_sum += location_bits.get((x , y - 1), 0)
        new_sum += location_bits.get((x , y + 1), 0)
        new_sum += location_bits.get((x + 1 , y + 1), 0)
        new_sum += location_bits.get((x + 1 , y - 1), 0)
        new_sum += location_bits.get((x - 1 , y + 1), 0)
        new_sum += location_bits.get((x - 1 , y - 1), 0)
        print('Sum for:', x, y, 'is', new_sum)
        location_bits[(x, y)] = new_sum
        previous_sum = location_bits[previous_location]
        if steps == max_steps:
            steps = 0
            direction_change += 1
            direction = (direction + 1) % 4
            # Max steps increases by one on evens
            if direction_change % 2 == 0:
                max_steps += 1
    return previous_sum



if __name__ == '__main__':
    print('The distance is:', check_distance(265149))
    print('The previous number was:', squared_square(265149))
