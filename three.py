import re

eg = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def one(source):
    muls = re.findall("mul\((\d+),(\d+)\)", source)

    total = 0
    for m in muls:
        total += int(m[0]) * int(m[1])

    print(total)

one(eg)
print("---")
with open("three.txt", "r") as file:
    one(file.read())
print("---")

def two(source):
    total = 0
    matches = re.finditer("do\(\)|don't\(\)|mul\((\d+),(\d+)\)", source)
    enabled = True
    for m in matches:
        if m[0] == "don\'t()":
            enabled = False
            continue
        elif m[0] == "do()":
            enabled = True
            continue
        elif enabled:
            g = m.groups()
            total += int(m.groups()[0]) * int(m.groups()[1])

    print(total)

eg = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

two(eg)
print("---")
with open("three.txt", "r") as file:
    two(file.read())