# student number 323
container = {
                (33555817, 3125, 9765625, 8, 23, 7523293, 28614582, 22256958, 3172621),             # input 1
                (33555751, 243, 30542048, 19, 14, 295845, 20826997, 14325870, 33485282),            #  .
                (33555553, 16807, 14030825, 8, 6, 11030354, 28131596, 11478229, 14555684),          #  .
                (33555493, 32, 32768, 10, 3, 11152483, 15342455, 29806492, 13155273),               #  .
                (33554699, 32, 32768, 14, 13, 2043221, 31335333, 2043221, 32352142), 
                (33554579, 32, 33554432, 31, 16, 24539544, 31870077, 24539544, 22718828), 
                (33555659, 32, 1048576, 17, 10, 1105213, 14101769, 18155557, 5893352), 
                (33555383, 16807, 11701571, 11, 20, 447397, 16228604, 28817193, 13965411), 
                (33555617, 243, 14348907, 10, 5, 13845724, 12977014, 30017090, 26275185), 
                (33555817, 3125, 9765625, 8, 23, 7523293, 28614582, 22256958, 3172621)              # input 10
            }



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def inverse(n: int, a: int):
    t, newt = 0, 1
    r, newr = n, a

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        raise ArithmeticError(f"{a} is not invertible mod {n}")
    if t < 0:
        t = t + n

    return t


def solve(p, g, A, D, Dp, S1, S2, S1p, S2p):
    if S1 != S1p:
        return "no"

    a = (S1 * (S2p - S2)) % (p - 1)
    b = ((S2p * D) - (S2 * Dp)) % (p - 1)
    d = gcd(a, p - 1)
    if d == 1:
        ans = (inverse(p - 1, a) * b) % (p - 1)
        if pow(g, ans, p) == A:
            return ans
        else:
            return "failed"
    else:
        a //= d
        b //= d
        m = (p - 1) // d
        ans = (inverse(m, a) * b) % m
        for i in range(d):
            if pow(g, ans, p) == A:
                return ans
            ans = (ans + m) % (p - 1)
        return "failed"


for x in container:
    p, g, A, D, D_p, s1, s2, s1_p, s2_p = x[0], x[1], x[2],x[3], x[4], x[5],x[6], x[7], x[8]
    print(">> solve({}, {}, {}, {}, {}, {}, {}, {}, {})".format(p, g, A, D, D_p, s1, s2, s1_p, s2_p))
    print(solve(p, g, A, D, D_p, s1, s2, s1_p, s2_p))