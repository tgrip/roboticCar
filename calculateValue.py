__author__ = 'Theo'

# ----------
# User Instructions:
#
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal.
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right



delta_name = ['^', '<', 'v', '>']

# ----------------------------------------
# insert code below
# ----------------------------------------

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    goalX = goal[0]
    goalY = goal[1]
    distance = 0
    value[goalX][goalY] = distance
    visited = []
    visited.append([goalX, goalY])
    succ = successors(goalX, goalY, visited)
    while succ:
        newSucc = []
        distance += cost_step
        for point in succ:
            visited.append([point[2], point[3]])
            value[point[2]][point[3]] = value[point[0]][point[1]] + cost_step
            newSucc += successors(point[2], point[3], visited)
#        printArray(value)
        succ = newSucc
    return value #make sure your function returns a grid of values pas demonstrated in the previous video.

def successors(x, y, visited):
    result = []
    for mov in delta:
        newX = x - mov[0]
        newY = y - mov[1]
        if (isRightPoint(newX, newY, visited)):
            result.append([x, y, newX, newY])
    return result


def isRightPoint(x, y, visited):
    return  (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])) and (grid[x][y] == 0) and ([x, y] not in visited)



def printArray(value):
    for i in range(len(value)):
        print value[i]

value = compute_value()
printArray(value)
