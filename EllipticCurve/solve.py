from generate_input import generate_input


container = [       ( 13 ,   2 ,   2 ,   2 ,   1 ,   2 ),           # (6,10)
                    ( 5 ,   1 ,   3 ,   4 ,   1 ,   2 ),            # (1,0)
                    ( 17 ,   4 ,   12 ,   5 ,   15 ,   3 )          # (-1,-1)
            ]


container = generate_input(323)

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


def solve(p,A,B,pX,pY,n):
    if 4 * pow(A,3) + 27 * pow(B,2) % p == 0:
        return "invalid A,B"
    # convert e to binary
    nBin = [int(d) for d in f'{n:b}']
    # create list of Ps and put rQ in
    Ps = (pX,pY)
    # add all Ps for each binary digit in n
    for i in range(1,len(nBin)):
        if nBin[i] == 1:
            dbl = twoPcalc(Ps[0],Ps[1],p)
            Ps = dblAdd(pX,pY,dbl[0],dbl[1],p)
        else:
            Ps = twoPcalc(Ps[0],Ps[1],p)
        if Ps == 'inf':
            return (-1,-1)
    return Ps
    



for i in container:
    p = i[0]
    A = i[1]
    B = i[2]
    pX = i[3]
    pY = i[4]
    n = i[5]
    print(">> solve({},{},{},{},{},{})\\\\".format(p,A,B,pX,pY,n))
    print(solve(p,A,B,pX,pY,n))
    #print(p,A,B,pX,pY,n)