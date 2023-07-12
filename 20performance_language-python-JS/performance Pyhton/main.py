import time

""" elsa_des_bois
exercice individuel : performance des languages - version JavaScript"""

"""Ipporting things"""

"""Declaring things here"""

from datetime import datetime

# getting time in miliseconds (int)
def now():
    return int(time.time() * 1000)


def add(a, b) :
    return a+b


def add_array(array, int_to_add) :
    new_array = []
    for i in array :
        new_array.append(i + int_to_add)
    print(new_array)
    return new_array


def fact(n):
    if n == 0:
        return 1
    else:
        return n  * fact(n-1)


""" We run things here """
if __name__ == '__main__':
    initial_time = now()
    print(initial_time)

    '''...execution du code...'''
    print(add(3,4))
    print(add_array([3, 4, 1, 10], 1))
    print(fact(5))

    """ calcul de performance en milisecondes """
    final_time = now()
    print(final_time)
    time_to_process =  final_time - initial_time
    print(f"L'éxécution a duré {time_to_process} miliseconds")