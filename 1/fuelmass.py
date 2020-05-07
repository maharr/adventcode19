import os

f = open("mass.txt","r")
all=0
def fuel(m):
    global all
    f = (m//3)-2
    all = all + f
    
    if f > 6:
        fuel(f)
    return all
        

total = 0

for x in f:
    mass = int(x)
    f = fuel(mass)
    total = total + f
    all = 0

print(total)
f.close()




