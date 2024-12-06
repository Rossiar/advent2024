import re
from functools import cmp_to_key

eg = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def one(source):
    rules = {}
    count = 0
    is_rules = True
    for line in source.splitlines():
        if line == "":
            is_rules = False
            continue
        if is_rules:
            key = line.split('|')[1]
            rule = rules.get(key, [])
            rule.append(line.split('|')[0])
            rules[key] = rule
        else:
            valid = True
            update = line.split(",")
            for i in range(0, len(update)):
                item = update[i]
                for j in range(i, len(update)):
                    if item in rules and update[j] in rules[item]:
                        #print(f"{update} failed on {item}: {rules[item]}")
                        valid = False
                        break
            if valid:
                count += int(update[int(len(update)/2)])
    print(f"{count}")     

one(eg)
print("---")
with open("five.txt", "r") as file:
    one(file.read())
print("---")

def fix(update, rules):
    for i in range(0, len(update)):
        item = update[i]
        for j in range(i, len(update)):
            if item in rules and update[j] in rules[item]:
                update[j], update[i] = update[i], update[j]
                print(f"swapped {update[j]} and {update[i]}: {update}")

def cmp(a, b, rules):
    if a in rules and b in rules[a]:
        return 1
    if b in rules and a in rules[b]:
        return -1
    return 0

def two(source):
    rules = {}
    count = 0
    is_rules = True
    for line in source.splitlines():
        if line == "":
            is_rules = False
            continue
        if is_rules:
            key = line.split('|')[1]
            rule = rules.get(key, [])
            rule.append(line.split('|')[0])
            rules[key] = rule
        else:
            update = line.split(",")
            invalid = False
            for i in range(0, len(update)):
                item = update[i]
                for j in range(i, len(update)):
                    if item in rules and update[j] in rules[item]:
                        #print(f"{update} failed on {item}: {rules[item]}")
                        invalid = True
                        break
            if invalid:
                fixed = sorted(update, key=cmp_to_key(lambda a, b: cmp(a, b, rules)))
                #print(f"sorted: {fixed}")
                count += int(fixed[int(len(fixed)/2)])
    print(f"{count}")

two(eg)
print("---")
with open("five.txt", "r") as file:
    two(file.read())