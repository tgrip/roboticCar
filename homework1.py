__author__ = 'Theo'

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT


def sense(p, Z):
    q=[]
    lineSum = []
    for i in range(len(p)):
        line = []
        for j in range(len(p[0])):
            hit = (Z == colors[i] [j])
            line.append(p[i][j] * (hit * sensor_right + (1-hit) * (1 - sensor_right)))
        q.append(line)
        lineSum.append(sum(line))
    s = sum(lineSum)
    for i in range(len(q)):
        for j in range(len(p[0])):
            q[i][j] = q[i][j] / s
    return q

def move(p, U):
    q = []
    y = len(p[0])
    for i in range(len(p)):
        line = []
        for j in range(y):
            s = p_move * p[(i-U[0]) % len(p)][j - U[1] % y]
            s += (1 - p_move) * p[i][j]
            line.append(s)
        q.append(line)
    return q

def init():
    x = len(colors)
    y = len(colors[0])
    initialVal = 1.0 / (x * y)
    q = []
    for i in range(x):
        line = []
        for j in range(y):
            line.append(initialVal)
        q.append(line)
    return q

p = init()

for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])



#Your probability array must be printed
#with the following code.

show(p)
  