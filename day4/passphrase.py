#! /usr/bin/env python

from IPython import embed

def cleanup_input():
    cleaned = []
    with open('input.txt') as f:
        for line in f:
            clean_line = [ item for item in line.split() ]
            cleaned.append(clean_line)
    return cleaned


def duplicate_check(passphrases):
    good_passphrases = []
    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            good_passphrases.append(passphrase)
    return good_passphrases


def anagram_check(valid_passphrases):
    good_passphrases = []
    for passphrase in valid_passphrases:
        alphabetized = [ ''.join(sorted(phrase)) for phrase in passphrase ]
        if len(alphabetized) == len(set(alphabetized)):
            good_passphrases.append(passphrase)
    return good_passphrases

def validate_passphrases(with_anagram=False):
    passphrases = cleanup_input()
    valid_passphrases = duplicate_check(passphrases)
    if with_anagram:
        valid_passphrases = anagram_check(valid_passphrases)
    return len(valid_passphrases)

if __name__ == '__main__':
    print('The number of valid passphrases is', validate_passphrases())
    print('The number of valid passphrases for part 2 is:', validate_passphrases(with_anagram=True))
