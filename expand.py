__author__ = 'Theo'

# -----------
# User Instructions:
#
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------

# ----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. NOTE: the 'v' should be
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]

delta = [[-1, 0], # go up
    [0, -1], # go left
    [1, 0], # go down
    [0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    roadTaken = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            roadTaken[x2][y2] = delta_name[i]

#    for i in range(len(roadTaken)):
#        print roadTaken[i]

    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    expandX = goal[0]
    expandY = goal[1]
    expand[expandX][expandY] = '*'
    while expandX != init[0] or expandY != init[1]:
        wayTaken = roadTaken[expandX][expandY]
        wayIndex = delta_name.index(wayTaken)
        deltaCord = delta[wayIndex]
        expandX -= deltaCord[0]
        expandY -= deltaCord[1]
        expand[expandX][expandY] = roadTaken[expandX][expandY]
    for i in range(len(expand)):
        print expand[i]
    return # make sure you return the shortest path.

# ----------------------------------------
# modify code below
# ----------------------------------------

cost = 1


search()

  