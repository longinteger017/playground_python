# DEBUGGING

import time
a_constant_number = 1


def print_date(one_element_from_for_loop, constant_number):
    print(constant_number)
    print(type(constant_number))
    print(constant_number == 1)
    # print(f"{one_element_from_for_loop}, date: {str(time.strftime('%Y-%m-%d %H:%M:%S'))}")
    # print("test")

for i in range(10):
    print_date(i, a_constant_number)
    time.sleep(2)
    print(a_constant_number)
