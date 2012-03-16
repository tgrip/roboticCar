
__author__ = 'Theo'

p=[0.2, 0.2, 0.2, 0.2, 0.2]
p1=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []

    for i in range(len(p)):
      factor = pMiss
      if (Z == world[i]):
        factor = pHit
      q.append(factor * p[i])

    #
    #ADD YOUR CODE HERE
	#
    return q

def move(p, U):
    q = list(p)
    sizeP = len(p)
    for i in range(sizeP):
        newIndex = i + U
        if (newIndex < 0):
            newIndex += sizeP
        elif (newIndex >= sizeP):
            newIndex -= sizeP
        q[newIndex] = p[i]
    return q

def move2(p, U):
    q = []
    for i in range(len(p)):
        exactValue = p[(i - U) % len(p)]
        overShootValue = p[(i - U + 1) % len(p)]
        underShootValue = p[(i - U - 1) % len(p)]
        value = pExact * exactValue + pOvershoot * overShootValue + pUndershoot * underShootValue
        q.append(value)
    return q


#print sense(p,Z)
print move2(p1, 1)
  