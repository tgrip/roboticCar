__author__ = 'Theo'

# ----------
# User Instructions:
#
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    current = init
    length = 0
    open = []
    visited = []
    initVal = [length, init[0], init[1]]
    open.append(initVal)
    nextValue = initVal
    while current != goal:
        visited.append([current[0], current[1]])
        print 'visited ', visited
        next = successors(current, visited)
        print 'next ', next
#        print 'Before remove', open
#        print 'To remove', length, current[0], current[1]
        open.remove(nextValue)
#        print 'old length', length
        length += cost
        print 'new length ', length
        for node in next:
            if (not isAlreadyOpen(open, node)):
                open.append([length, node[0], node[1]])
        print 'New open', open
        nextValue = min(open)
        print 'next value', nextValue
        current = [nextValue[1], nextValue[2]]
        print 'New current', current
        print ''


def successors(current, visited):
    result = []
    for mov in delta:
        newX = current[0] + mov[0]
        newY = current[1] + mov[1]
        if (isRightPoint(newX, newY, visited)):
            result.append([newX, newY])
    return result

def isRightPoint(x, y, visited):
    return  (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])) and (grid[x][y] == 0) \
    and ([x, y] not in visited)

def isAlreadyOpen(open, current):
    for node in open:
        if (node[1] == current[0]) and (node[2] == current[1]):
            return True
    return False

search()