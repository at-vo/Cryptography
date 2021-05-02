import random

ins = [ [32416187567, 100, 300, 4926003430, 24870962866],
        [32416188191, 54, 456, 4979256242, 12312669996],
        [32416188113, 19, 33, 19262187694, 12958025965],
        [32416189987, 1004, 9998, 22858809622, 16175884785],
        [32416188689, 103245, 992349, 17766069433, 14705693667],
        [32416189081, 325, 233496, 12258808116, 11275809752] ]

big = 100000000000000

def generate() :

    pars = random.choice(ins).copy()

    return(pars)


def generate_input(s) :

    s = int(str(s))
    random.seed(s)

    ns = random.sample(range(1,big),10)

    res = [ generate() for i in range(10) ]

    for i in range(10) :
        res[i].append(ns[i])

    return(res)
