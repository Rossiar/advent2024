

eg = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

class Guard:
    facing: str
    x: int
    y: int
    visited: set

    def __init__(self, facing, x, y):
        self.facing = facing
        self.x = x
        self.y = y
        self.visited = set()
        self.visited.add((y, x))
    
def walk(guard, grid, debug):
    if len(guard.visited) > 0 and debug:
        print(f"turning {guard.facing} at ({guard.y},{guard.x}) - visited {len(guard.visited)} spaces")
    if guard.facing == "up":
        for i in reversed(range(0, guard.y)):
            if grid[i][guard.x] == "#":
                guard.facing = "right"
                return walk(guard, grid, debug)
            else:
                guard.y = i
                guard.visited.add((i, guard.x))
    elif guard.facing == "down":
        for i in range(guard.y, len(grid)):
            if grid[i][guard.x] == "#":
                guard.facing = "left"
                return walk(guard, grid, debug)
            else:
                guard.y = i
                guard.visited.add((i, guard.x))
    elif guard.facing == "right":
        for i in range(guard.x, len(grid)):
            if grid[guard.y][i] == "#":
                guard.facing = "down"
                return walk(guard, grid, debug)
            else:
                guard.x = i
                guard.visited.add((guard.y, i))
    elif guard.facing == "left":
        for i in reversed(range(0, guard.x)):
            if grid[guard.y][i] == "#":
                guard.facing = "up"
                return walk(guard, grid, debug)
            else:
                guard.x = i
                guard.visited.add((guard.y, i))

def one(source, debug):
    lines = source.splitlines()
    blockers = []
    guard = (-1,-1)
    for y in range(0, len(lines)):
        line = lines[y]
        for x in range(0, len(line)):
            if line[x] == "^":
                guard = Guard(facing="up", x=x, y=y)
            elif line[x] == "#":
                blockers.append((y,x))
    if debug:
        print(blockers)
    walk(guard, lines, debug)
    print(f"guard at ({guard.y},{guard.x}) ({guard.facing}) has visited {len(guard.visited)} spaces")
        
one(eg, True)
print("---")
with open("six.txt", "r") as file:
    one(file.read(), False)
# 5177