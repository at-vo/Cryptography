container = [   
                (8389057, 50354, 641736), 
                (8389099, 81194, 4611664), 
                (8391037, 68226, 7343254)
            ]

def solve(p,g,h):
    M = 1 + int(p ** (1/2))
    list1 = []
    list2 = []
    for i in range (M + 1):
        # store g^[0...M]
        list1.append(g ** i % p)
        
        # calculate fermat's little theorem
        # note: forced to use pow() instead of ** and % because of the 
        #       large amount of time needed to calculate using just operators
        s = pow(g, p-2, p)
        t = pow(s, M, p)
        u = pow(t, i, p)

        # store hg^[-iM]
        list2.append(h * u % p)
    
    # find matching entries in the lists
    # print(M,list1,list2)
    for i in list2:
        if i in list1:
            # calculate x then return
            return list1.index(i) + list2.index(i) * M
    # if solution not found
    return None

for i in container:
    p = i[0]
    g = i[1]
    h = i[2]
    solution = solve(p,g,h)
    if (solution != None):
        print("x = {} is a solution for p={}, g={}, h={}".format(solution,p,g,h))
    else:
        print("there is no solution")