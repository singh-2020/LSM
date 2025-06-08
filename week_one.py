# 1. py-if-else task

n = int(input())
if n % 3 != 0:
    print("Acceptable")
elif n in range(3, 15):
    print("Not acceptable")
else:
    print("Acceptable")


# 2.  Arithmetic-operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# 3. Compress string

from itertools import groupby

S = input()
result = [(len(list(g)), int(k)) for k, g in groupby(S)]

print(' '.join(str(t) for t in result))


# 4. Minion game

def minion_game(string):
    vowels = 'AEIOU'
    kevin = sum(len(string) - i for i in range(len(string)) if string[i] in vowels)
    stuart = len(string)*(len(string)+1)//2 - kevin
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


# 5. Leap Year

def is_leap(year):
    leap = False
    # Write your logic here
    if year%4 == 0 and year%100 != 0 :
        leap = True
    elif year%400 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))


#6. Word order

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    word = input()
    d[word] = d.get(word, 0) + 1
print(len(d))
print(*d.values())


# 7. Iterables and Iterators

from itertools import combinations
N = int(input())
S = input().split()
K = int(input())
comb = list(combinations(S, K))
count = sum('a' in c for c in comb)
print(count / len(comb))


# 8. Tuples (Hash)

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(integer_list))


# 9. Average Score

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")


# 10. String formating

def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:{width}d} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)