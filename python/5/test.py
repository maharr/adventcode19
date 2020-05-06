# code = [1101,100,-1,4,0]
code = [3,225,1,225,6,6,1100,1,238,225,104,0,2,136,183,224,101,-5304,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1101,72,47,225,1101,59,55,225,1101,46,75,225,1101,49,15,224,101,-64,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,102,9,210,224,1001,224,-270,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,101,14,35,224,101,-86,224,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1102,40,74,224,1001,224,-2960,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,10,78,225,1001,39,90,224,1001,224,-149,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1002,217,50,224,1001,224,-1650,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1102,68,8,225,1,43,214,224,1001,224,-126,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,88,30,225,1102,18,80,225,1102,33,28,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,374,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,389,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,404,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,1107,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,494,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,539,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,569,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,614,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,629,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]

# code = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


print(code)

input = 5
output = 0

def run(n):
    # print(code)
    
    global output, input
    op = code[n]// 1 % 100
    
    # print("Op code " + str(op))
    if op == 99:
        return
    
    p1 = 0   
    if code[n] // 100 %10 == 1:
        p1 = n+1
    else:
        p1 = code[n+1]
        
    # print("p1 " + str(p1))
    
    if op == 3: 
        code[p1] = input
        run(n+2)
        return
    if op == 4:
        output = code[p1]
        print("output " + str(output))
        run(n+2)
        return
    
    
    p2 = 0
    if code[n] // 1000 %10 == 1:
        p2 = n+2
    else:
        p2 = code[n+2]
    # print("p2 " + str(p2))
    if op == 5:
        if code[p1] != 0:
            code[n] = code[p2]
            run(code[p2])
            return
        else:
            run(n+3)
            return
    if op == 6:
        if code[p1] == 0:
            code[n] = code[p2]
            run(code[p2])
            return
        else:
            run(n+3)
            return
    
    p3 = 0
    if code[n] // 10000 %10 == 1:
        p3 = n+3
    else:
        p3 = code[n+3]
    # print("p3 "+str(p3))
    
    if op == 1:
        code[p3] = code[p1] + code[p2]
        run(n+4)
        return
    if op == 2:
        code[p3] = code[p1] * code[p2]
        run(n+4)
        return
    if op == 7:
        if code[p1] < code[p2]:
            code[p3] = 1
        else:
            code[p3] = 0
        run(n+4)
        return
    if op == 8:
        if code[p1] == code[p2]:
            code[p3] = 1
        else:
            code[p3] = 0
        run(n+4)
        return
    
        
run(0)
print(code)
