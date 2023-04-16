# python3
import numpy as np
# 221RDB224 Agate Šarna 6.grupa
def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    source= input()
    if source[0] == 'I':
        return (input().rstrip(), input().rstrip())
    elif source[0] == 'F':
        file_name = input()
        if "a" in file_name:
            return
        file_name = 'test/' + file_name
        with open(file_name, 'r') as f:
            return (f.readline().rstrip(), f.readline().rstrip())
    else:
        return
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
    #for i in output:
       # print(i, end=' ')
    #print()

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    d = 10
    q = 997
    pattern_l = len(pattern)
    text_l = len(text)
    m = 0
    n = 0
    h = 1
    occurrences = []
    for i in range(pattern_l-1):
        h = (h * d) % q
    for i in range(pattern_l):
       m = (d*m + ord(pattern[i])) % q
       n = (d*n + ord(text[i])) % q
    for i in range(text_l - pattern_l + 1):
        if m == n and text[i:i+pattern_l] == pattern:
          occurrences.append(i)
        if i < text_l - pattern_l:
          n = (d*(n - ord(text[i])*h) + ord(text[i+pattern_l])) % q

        if n < 0:
            n += q
    return occurrences
# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

