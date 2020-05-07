data = open("data.txt", "r")
planets = data.read().splitlines()
for i,planet in enumerate(planets):
    planets[i] = planet.split(")")

orbits = {}

for planet in planets:
    orbits[planet[1]] = planet[0]

#print(orbits)

counter = 0

san = {}
you = {}

for i,orbit in enumerate(orbits):
    counter += 1
    orbiting = orbits[orbit]
    #print("Line  " + str(i))
    if orbit == "SAN":
        san[orbits[orbit]] = orbit
    elif orbit == "YOU":
        you[orbits[orbit]] = orbit
    
    centre = False
    
    while not centre:
        if orbiting in orbits:
            if orbit == "SAN":
                san[orbits[orbiting]] = orbiting
            elif orbit == "YOU":
                you[orbits[orbiting]] = orbiting
            counter += 1
            orbiting = orbits[orbiting]
        else:
            centre = True
distance = 0
                        
for s in san:
    if s in you:
        continue
    else:
        distance += 1
for y in you:
    
    if y in san:
        continue
    else:
        distance += 1        
            
print("Total number of orbits " + str(counter))            
print("Distance between SAN and YOU " + str(distance))            

#print(orbits)

    




