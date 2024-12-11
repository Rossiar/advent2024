eg = "2333133121414131402"

def expand(fs):
    blocks = []
    j = 0
    for i in range(0, len(fs)):
        n = fs[i]
        if i % 2 == 0:
            blocks.extend([str(j)] * int(n))
            j += 1
        else:
            blocks.extend(['.'] * int(n))
    #print(''.join(blocks))
    return blocks

def checksum(blocks):
    total = 0
    for i in range(0, len(blocks)):
        n = blocks[i]
        if n == '.':
            break
        total += int(n) * i
    return total

def one(source):
    blocks = expand(source)
    i = 0
    j = len(blocks)-1
    while i < j:
        if blocks[j] == '.':
            j -= 1
            continue
        if blocks[i] != '.':
            i += 1
            continue
        blocks[i] = blocks[j]
        blocks[j] = '.'
        j -= 1
        i += 1
    #print(''.join(blocks))
    total = checksum(blocks)
    print(f"checksum: {total}")

one(eg)
print("---")
with open("nine.txt") as file:
    one(file.read())
print("---")

def two(source):
    blocks = expand(source)
    print("".join(blocks))
    handled = set()
    blocks = []
    j = len(source)-1
    k = 0
    for i in range(0, len(source)):
        n = int(source[i])
        if i % 2 == 0:
            if k in handled:
                blocks.extend(['.'] * n)
                k += 1
                continue
            blocks.extend([str(k)] * n)
            k += 1
        else:
            match = False
            while j > k:
                m = int(source[j])
                if m <= n:
                    before = "".join(blocks)
                    blocks.extend([str(int(j/2))] * m)
                    blocks.extend(['.'] * (n-m)) 
                    handled.add(int(j/2))
                    j -= 2
                    match = True
                    break
                j -= 2
            if not match:
                blocks.extend(['.'] * n) 
    print("".join(blocks))

two(eg)
print("---")
# 00992111777.44.333....5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..