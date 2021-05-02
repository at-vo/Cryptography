container = [
                #Input 1
                [32416188691, 103245, 992349, 8909974598, 12810966706, 17766069436, 28295926988, 16789908933, 20309635644],
                #Input 2
                [32416189987, 1004, 9998, 21776342460, 26884854746, 22858809622, 16175884785, 29713279001, 18366438538],
                #Input 3
                [32416188127, 19, 33, 16475848216, 5118271045, 19262187694, 2854205065, 13332545241, 9721955507]
            ]


container = [
                [32416187567 ,  100 ,  300 ,  27957624436 ,  9381314875 ,  4926003430 ,  24870962866 ,  17242042885 ,  3564697884],      # 4690041109
                [32416188191 ,  54 ,  456 ,  27828875679 ,  24709261957 ,  4979256242 ,  12312669996 ,  10269365243 ,  1308878353],      # 18039526984
                [32416188127 ,  19 ,  33 ,  16475848216 ,  5118271045 ,  19262187694 ,  2854205065 ,  13332545241 ,  18635505014]        # 16371031443   
            ]

def dblP(pX,pY,p):
    if(pY == 0):
        return 'inf'
    # lambda
    gL = (3 * pow(pX,2) + A) * pow(2 * pY, p-2, p)
    # Nue
    gN = pY - (gL * pX)
    # P coordinates
    x3 = pow(gL,2) - (2 * pX)
    y3 = (-gL * x3) - gN 
    return (x3 % p,y3 % p)

def dblAdd(pX,pY,qX,qY,p):
    if pX == qX and pY == (-qY % p):
        return 'inf'
    # lambda
    gL = (qY - pY) * pow(qX-pX,p-2,p)
    # Nue
    gN = pY - gL * pX
    # P coordinates
    x3 = pow(gL,2) - pX - qX
    y3 = (-gL * x3) - gN 
    return (x3 % p,y3 % p)

def nPAlgo(pX,pY,n,p):
    # convert e to binary and flip
    nBin = [int(d) for d in f'{n:b}']
    # create list of Ps and put rQ in
    Ps = (pX,pY)
    # add all Ps for each binary digit in n
    for i in range(1,len(nBin)):
        if nBin[i] == 1:
            dbl = dblP(Ps[0],Ps[1],p)
            Ps = dblAdd(pX,pY,dbl[0],dbl[1],p)
        else:
            Ps = dblP(Ps[0],Ps[1],p)
        if Ps == 'inf':
            return (-1,-1)
    return Ps

def solve(p, A, B, Px, Py, Qx, Qy, e, t1):
    if (4*A**3 + 27*B**2) % p == 0:
        return "invalid A,B"
    # calculate k
    k = (p - 3) // 4
    # calculate rQy^2
    rQysq = (pow(t1,3) + A * t1 + B) % p
    # find rQy using x = q^(k+1) mod p
    rQy = pow(rQysq, k + 1,p)
    # use double and add algorithm to find erQ 
    #   recall: t1 = rQx
    erQ = nPAlgo(t1,rQy,e,p)
    # s1 = x(erQ)
    s1 = erQ[0]
    # r = x(s1P)
    r = nPAlgo(Px,Py,s1,p)[0]
    # t2 = x(rQ)
    t2 = nPAlgo(Qx,Qy,r,p)[0]
    return t2

for i in container:
    p = i[0]
    A = i[1]
    B = i[2]
    Px = i[3]
    Py = i[4]
    Qx = i[5]
    Qy = i[6]
    e = i[7]
    t1 = i[8]
    print(">> solve({},{},{},{},{},{},{},{},{})\\\\".format(p, A, B, Px, Py, Qx, Qy, e, t1))
    print(solve(p, A, B, Px, Py, Qx, Qy, e, t1))