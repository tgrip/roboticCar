__author__ = 'Theo'

# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# Note that you do not need to use the tolerance parameter
# shown in the video.
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.0, weight_smooth = 0.1):

    # Make a deep copy of path into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]



    #### ENTER CODE BELOW THIS LINE ###
    for k in range(10):
        for i in range(1, len(newpath) - 1):
            p = newpath[i]
#            print 'old p', p
            nextP = newpath[i + 1]
            beforeP = newpath[i - 1]
            oldP = path[i]
            for j in range(0,2):
                p[j] = p[j] + weight_data * (oldP[j] - p[j])
                p[j] = p[j] + weight_smooth * (nextP[j] + beforeP[j] - 2 * p[j])

    return newpath # Leave this line for the grader!

# feel free to leave this and the following lines if you want to print.
newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'

  