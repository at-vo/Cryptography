'''Input #1
Private key (N,d) = (1152925125267120091,1152925123119633071)
Ciphertext c = 928626267595081870'''

'''Input #2
Private key (N,d) = (1152923499619716509,1152923497472231003)
Ciphertext c = 662043600824269185'''

'''Input #3
Private key (N,d) = (1152923237626490797,1152923235479005535)
Ciphertext c = 1036098972817061600'''


container = {
            (1152925125267120091, 1152925123119633071, 928626267595081870),  # input 1
            (1152923499619716509, 1152923497472231003, 662043600824269185),  # input 2
            (1152923237626490797, 1152923235479005535, 1036098972817061600)  # input 3
            }

# test cases
# container = {
#             (1152924549740517683 ,1152924547593031199 ,386126487832000948),     # 111000111110011100000110100011
#             (1152923261248820939 ,1152923259101335655 ,598837185728077836),     # 110110001111000101101010110110
#             (1152921753714962639 ,1152921751567478759 ,612969880391394694)      # 000101011011101000101011110010
#             }

def solve(N,d,c):
    # convert to binary 
    rxor = f'{pow(c,d,N):060b}'
    # split into two components
    r,xor = rxor[:len(rxor)//2], rxor[len(rxor)//2:]
    # check if same digits and return string
    return ''.join(['1' if r[digit]==xor[digit] else '0' for digit in range(len(xor)) ])


for i in container:
    N = i[0]
    d = i[1]
    c = i[2]
    print("decrypted message m =", solve(N,d,c))