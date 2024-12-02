import collections
import io

def one(source):
    left = []
    right = []
    for line in source.splitlines():
        words = line.split()
        if len(words) != 2:
            continue
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    left.sort()
    right.sort()

    if len(left) != len(right):
        print("lists are not same length")
        exit

    total = 0
    for i in range(0, len(left)):
        total += abs(left[i] - right[i])

    print(f"total: {total}")
    print("---")

eg = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

print("example")
one(eg)

print("one")
with open("one.txt", "r") as file:
    one(file.read())

def two(source):
    left = []
    right = []
    for line in source.splitlines():
        words = line.split()
        if len(words) != 2:
            continue
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    freq = collections.Counter(right)

    total = 0
    for i in left:
        f = freq[i]
        if f == 0:
            continue
        total += i * f

    print(f"total: {total}")
    print("---")

print("example")
two(eg)

print("two")

with open("one.txt", "r") as file:
    two(file.read())