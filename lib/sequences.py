#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib = [0, 1]
        while len(fib) < length:
            fib.append(fib[-1] + fib[-2])
        print(fib)
   