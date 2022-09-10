from vpython import *

rod = cylinder(pos=vector(0,0,0), axis=vector(0,6,0), radius=1,
        color = color.yellow)

ring1 = ring(pos=vector(10,1,0),
        axis=vector(0,10,0),
        radius=5, thickness=1,
        color = color.red)

ring2 = ring(pos=vector(20,1,0),
        axis=vector(0,5,0),
        radius=3.5, thickness=1,
        color = color.green)

ring3 = ring(pos=vector(30,1,0),
        axis=vector(0,2,0),
        radius=2, thickness=1,
        color = color.red)



cone1 = cone(pos=vector(35,0,0),
        axis=vector(0,5,0),
        radius=1,
        color = color.yellow)

for i in range(17):
    ring1.pos.y += 1
    rate(5)

for i in range(10):
    ring1.pos.x -= 1
    rate(5)

for i in range(17):
    ring1.pos.y -= 1
    rate(5)


        
for i in range(17):
    ring2.pos.y += 1
    rate(10)
for i in range(20):
    ring2.pos.x -= 1
    rate(10)
for i in range(15):
    ring2.pos.y -= 1
    rate(10)

        
for i in range(17):
    ring3.pos.y += 1
    rate(10)
for i in range(30):
    ring3.pos.x -= 1
    rate(10)
for i in range(13):
    ring3.pos.y -= 1
    rate(10)


for i in range(17):
    cone1.pos.y += 1
    rate(10)
for i in range(35):
    cone1.pos.x -= 1
    rate(10)
for i in range(11):
    cone1.pos.y -= 1
    rate(10)










    
