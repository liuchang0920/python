# coding = utf-8

import re

def word_count(filepath):
    count = 0
    file = open(filepath, 'r')
    for line in file.readlines():
        words =  re.findall(r'[a-zA-Z0-9]+', line)
        count += len(words)

    return count

filepath = 'test.txt'
print word_count(filepath)

