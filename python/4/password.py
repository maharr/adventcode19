hint = [353096, 843212]

number = []

count = 0

for f in range(0,10):
        for e in range(f,10):
            for d in range(e,10):
                for c in range(d,10):
                    for b in range(c,10):
                        for a in range(b,10):
                            number = a + (b*10) +(c*100) + (d*1000) + (e*10000) + (f*100000)
                            if number >= hint[0] and number <= hint[1]:
                                if (a==b and b !=c) or (b==c and c!=d and a!=b) or (c==d and d!=e and b!=c) or (d==e and e!=f and c!=d) or (e==f and d!=e): # comment line for pt 1
                                    print(number)
                                    count+=1
                            
                            
                            
                            
                
print(count)
            
    

    
