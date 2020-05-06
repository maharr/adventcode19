from itertools import permutations

#code_input = [3,8,1001,8,10,8,105,1,0,0,21,30,55,80,101,118,199,280,361,442,99999,3,9,101,4,9,9,4,9,99,3,9,101,4,9,9,1002,9,4,9,101,4,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,5,9,9,1002,9,2,9,101,3,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]

#code_input  = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

#code_input =[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#code_input = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

code_input = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

print(code_input)

code = [] * 5

#perm = permutations([0,1,2,3,4])
perm = permutations([5,6,7,8,9])

orderPerm = []
output = [0]

for i,p in enumerate(perm):
    orderPerm.append(list(p))

#print(orderPerm)

#orderPerm = orderPerm[0:1]




def run(n,input, pos):
    print(input)
    global output, code
    print(code)
    op = code[n]// 1 % 100
    
    print("Op code " + str(op))
    if op == 99:
        return
    
    p1 = 0   
    if code[n] // 100 %10 == 1:
        p1 = n+1
    else:
        p1 = code[n+1]
        
    # print("p1 " + str(p1))
    
    if op == 3: 
        code[p1] = input[0]
        run(n+2, input[1:])
        return
    if op == 4:
        output.append(code[p1])
        #print("output " + str(output))
        run(n+2, input)
        return
    
    
    p2 = 0
    if code[n] // 1000 %10 == 1:
        p2 = n+2
    else:
        p2 = code[n+2]
    #print("p2 " + str(p2))
    if op == 5:
        if code[p1] != 0:
            #code[n] = code[p2]
            run(code[p2], input)
            return
        else:
            run(n+3, input)
            return
    if op == 6:
        if code[p1] == 0:
            #code[n] = code[p2]
            run(code[p2], input)
            return
        else:
            run(n+3, input)
            return
    
    p3 = 0
    if code[n] // 10000 %10 == 1:
        p3 = n+3
    else:
        p3 = code[n+3]
    # print("p3 "+str(p3))
    
    if op == 1:
        code[p3] = code[p1] + code[p2]
        run(n+4, input)
        return
    if op == 2:
        code[p3] = code[p1] * code[p2]
        run(n+4, input)
        return
    if op == 7:
        if code[p1] < code[p2]:
            code[p3] = 1
        else:
            code[p3] = 0
        run(n+4, input)
        return
    if op == 8:
        if code[p1] == code[p2]:
            code[p3] = 1
        else:
            code[p3] = 0
        run(n+4,input)
        return

outputs = []
  
for order in orderPerm:
    #print(order)
    output = [0]
    for i,o in enumerate(order):
        code = code_input
        run(0,[o,output[-1]])
    outputs.append(output[-1])

outputs.sort(reverse=True)              
#run(0,[20, 50])
print(outputs[0])
