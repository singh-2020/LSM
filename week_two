# 1. Capital Word

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = 'output.txt'
def solve(s):
    words = s.split()
    capitalword = []

    for word in words:
        if word and word[0].isalpha():
            capitalword.append(word[0].upper() + word[1:])
        else:
            capitalword.append(word)
    
    return ' '.join(capitalword)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


# 2. Introduction to set

def average(arr):
    unique_values = set(arr)
    total  = sum(unique_values)
    average = total/len(unique_values)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# 3. Text Wrap

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# 4. Alphabet-rangoli

import string
def print_rangoli(n):
    alpha = string.ascii_lowercase

    # List to store each line of the rangoli
    lines = []

    # Construct the pattern from top to center
    for i in range(n):
        row = '-'.join(alpha[n-1:i:-1] + alpha[i:n])
        width = 4*n - 3         # total width of each line
        lines.append(row.center(width, '-'))

    # Mirror the top half to create the bottom half
    print('\n'.join(lines[::-1] + lines[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# 5. Merge the tools

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        val = string[i:i+k]
        unique_val = set()
        result = ''
        for v in val:
            if v not in unique_val:
                unique_val.add(v)
                result += v
        print(result)

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# 6. Collection counter

from collections import Counter

# Input: number of shoes in the shop
X = int(input())

# Input: list of shoe sizes available
shoe_sizes = list(map(int, input().split()))

# Create a stock inventory using Counter
inventory = Counter(shoe_sizes)

# Input: number of customers
N = int(input())

# Variable to keep track of earnings
earnings = 0

# Process each customer
for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price         # Add price to earnings
        inventory[size] -= 1      # Decrease the stock for that shoe size

# Output the total earnings
print(earnings)


# 7. Exceptions : implementing exception handling

# # Number Test cases
T = int(input())

for _ in range(T):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


# 8. Incorrect Regeex

import re

T = int(input())
for _ in range(T):
    pattern = input()
    # Manually check for invalid operator combinations
    if any(op in pattern for op in ['*+', '+*', '++', '**', '?+', '+?', '*?', '??']):
        print("False")
    else:
        try:
            re.compile(pattern)
            print("True")
        except re.error:
            print("False")


# 9. py-set-discard-remove-pop: task based on discard(),remove() & pop()

# Number of elements in set
n = int(input())
s = set(map(int, input().split()))

# Number of commands 
N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "discard":
        s.discard(int(command[1]))
    elif command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    
print(sum(s))
