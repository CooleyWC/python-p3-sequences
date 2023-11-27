#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
         print([])
         return []
    elif length == 1:
         print([0])
         return 0
    elif length == 2:
         print([0,1])
         return [0,1]
    fib_list = [0,1]
    i = 0
    j = 1
    for num in range(length -2):
         fib_list.append(fib_list[i] + fib_list[j])
         i += 1
         j += 1
    print(fib_list)
         
