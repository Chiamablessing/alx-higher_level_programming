#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    uniq_num = 0

    for i in uniq_list:
        uniq_num += i

    return (uniq_num)
