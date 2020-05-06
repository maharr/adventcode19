data = open("sample.txt", "r")
planets1 = data.read().splitlines()
for i,planet in enumerate(planets1):
    planets1[i] = planet.split(")")

counter = 0


def resolve(planets):
    orbits = []
    for planet in planets:
        for plan in planets:
            if planet[0] == plan[-1]:
                orbits.append([plan, planet])
                
                #print(orbits)
                #print(plan[0], plan[1], planet[0], planet[1])
            
    for orbit in
    return orbits


orbits = resolve(planets1)
orbits = resolve(orbits)
print(orbits)




