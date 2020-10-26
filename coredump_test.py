#!/usr/bin/env python3

import sys
import re


def test_split(input_file, search_regex):
    with open(input_file) as file:
        lines = []
        for line in file:
            splitline = line.split(' ')
            try:
                lines.append(splitline[7].strip('\n'))
            except IndexError:
                pass
        final = ''.join(lines)
        matched_string = re.search(search_regex, final)
        print(matched_string.group(1))


if __name__ == "__main__":
    input_file = sys.argv[1]
    search_regex = sys.argv[2]

    print(search_regex)
    test_split(input_file, search_regex)
