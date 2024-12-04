

eg = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def north(word, i):
    return i >= (len(word)-1)

def south(word, i, x):
    return i + len(word) <= len(x)

def east(word, j, y):
    return j + len(word) <= len(y)

def west(word, j):
    return j - (len(word)-1) >= 0

def one(source):
    word = "XMAS"
    count = 0
    x = source.splitlines()
    for i in range(0, len(x)):
        y = x[i]
        for j in range(0, len(y)):
            if y[j] != 'X':
                continue
            # check east
            if east(word, j, y):
                match = True
                for k in range(0, len(word)):
                    if y[j+k] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found east at ({i},{j})")
                    count += 1
            # check west
            if west(word, j):
                match = True
                for k in range(0, len(word)):
                    if y[j-k] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found west at ({i},{j})")
                    count += 1
            # check north
            if north(word, i):
                match = True
                for k in range(0, len(word)):
                    if x[i-k][j] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found north at ({i},{j})")
                    count += 1
            # check south
            if south(word, i, x):
                match = True
                for k in range(0, len(word)):
                    if x[i+k][j] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found south at ({i},{j})")
                    count += 1
            # check north west
            if north(word, i) and west(word, j):
                match = True
                for k in range(0, len(word)):
                    if x[i-k][j-k] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found north west at ({i},{j})")
                    count += 1
            # check north east
            if north(word, i) and east(word, j, y):
                match = True
                for k in range(0, len(word)):
                    if x[i-k][j+k] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found north east at ({i},{j})")
                    count += 1
            # check south east
            if south(word, i, x) and east(word, j, y):
                match = True
                for k in range(0, len(word)):
                    if x[i+k][j+k] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found south east at ({i},{j})")
                    count += 1
            # check south west
            if south(word, i, x) and west(word, j):
                match = True
                for k in range(0, len(word)):
                    if x[i+k][j-k] != word[k]:
                        match = False
                        break
                if match:
                    #print(f"found south west at ({i},{j})")
                    count += 1
    print(f"found {count}")

one(eg)
print("---")
with open("four.txt", "r") as file:
    one(file.read())
print("---")

def two(source):
    word = "MAS"
    count = 0
    x = source.splitlines()
    for i in range(0, len(x)):
        y = x[i]
        for j in range(0, len(y)):
            if y[j] != 'A' or i == 0 or j == 0 or i == len(x)-1 or j == len(y)-1:
                continue
            nw = x[i-1][j-1] + x[i][j] + x[i+1][j+1]
            ne = x[i-1][j+1] + x[i][j] + x[i+1][j-1]
            sw = x[i+1][j-1] + x[i][j] + x[i-1][j+1]
            se = x[i+1][j+1] + x[i][j] + x[i-1][j-1]
            if [nw, ne, sw, se].count(word) == 2:
                #print(f"found X-MAS: {nw} {ne} {sw} {se}")
                count += 1
    print(f"found {count}")

two(eg)
print("---")
with open("four.txt", "r") as file:
    two(file.read())