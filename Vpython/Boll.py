from vpython import *
ball1 = sphere()
ball2 = sphere(pos = vec(5, 0,0), radius = 1.5, color = color.yellow)
ball3 = sphere(pos = vec(11, 0,0), radius = 2, color = color.red)
for i in range(300):
    ball3.pos.x += 0.1
    rate(24)
