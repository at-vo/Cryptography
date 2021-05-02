import os
import re
from generate_input import generate_input
from done import solve
import time

MY_NUMS = '323'

if __name__ == '__main__':
    input_lists = generate_input(MY_NUMS)
    correct = 0
    total = 0

    for input_list in input_lists:
        # convert to tuple
        input_tuple = tuple(input_list)

        # get result from solve
        time_start = time.time() * 1000
        local_result = solve(*input_tuple)
        time_end =  time.time() * 1000
        time_dur = round(time_end - time_start, 4)

        # print local result
        print(f"solve{input_tuple}")
        print(f"    = {local_result}")
        print(f"        Computation took {time_dur}ms")

        # ask sage what the answer should be
        print('    Checking against Sage....')
        stream = os.popen(f'sage -c "E = EllipticCurve(GF({input_tuple[0]}), [{input_tuple[1]}, {input_tuple[2]}]); P = E.point([{input_tuple[3]}, {input_tuple[4]}]); R = {input_tuple[5]} * P; print((R[0], R[1]))"')
        output = stream.read().rstrip()

        # extract numbers from regex
        if output == '':
            sage_result = None
        else:
            regex_result = re.search('\((\d+), (\d+)\)', output)
            sage_result = (int(regex_result.group(1)), int(regex_result.group(2)))
        
        # print match or fail
        total += 1
        if sage_result is None:
            print('        Unable to check against Sage, verify that sage executable is on PATH')
        elif sage_result == local_result:
            correct += 1
            print('        Sage match OK')
        else:
            print(f'       Sage match FAIL, Sage expected {sage_result}')

    print('=======================================')
    print(f'Test complete: {correct}/{total} correct.')
    print('=======================================')
