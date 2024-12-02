

eg = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

class Report:
    levels: list = []
    safe: bool = False

    def __repr__(self):
        return f"safe: {self.safe}, levels: {self.levels}"

def safe(levels):
    ascending = True
    for i in range(0, len(levels)-1):
        a = levels[i]
        b = levels[i+1]
        if i == 0:
            ascending = a < b
        if (a > b and ascending) or (a < b and not ascending):
            return False
        gap = abs(a - b)
        if gap > 3 or gap < 1:
            return False
    return True

def one(source):
    reports = []
    num_safe = 0
    for line in source.splitlines():
        levels = line.split()
        if len(levels) == 0:
            continue
        report = Report()
        report.levels = [int(l) for l in levels]
        report.safe = safe(report.levels)        
        reports.append(report)
        if report.safe:
            num_safe += 1
    print(f"total safe: {num_safe}")

print("example")
one(eg)
print("---")
print("one")
with open("two.txt", "r") as file:
    one(file.read())
    
def two(source):
    reports = []
    num_safe = 0
    for line in source.splitlines():
        levels = line.split()
        if len(levels) == 0:
            continue
        report = Report()
        report.levels = [int(l) for l in levels]
        if safe(report.levels):
            num_safe += 1
            report.safe = True
            reports.append(report)
            #print(report)
            continue
        for i in range(0, len(report.levels)):
            levels = report.levels.copy()
            del levels[i]
            if safe(levels):
                num_safe += 1
                report.safe = True
                break
        reports.append(report)
        #print(report)
    print(f"total safe: {num_safe}")


print("---")
print("example")
two(eg)
print("---")
print("two")
with open("two.txt", "r") as file:
    two(file.read())