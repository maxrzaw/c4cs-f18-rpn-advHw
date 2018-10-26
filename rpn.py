#!/usr/bin/env python3

import operator
import numpy as np
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,

}

def calculate(args):
    #stack for calculator
    stack = list()
    #tokenize input
    tokens = args.split()
    # process tokens
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if len(token) == 1:
                func = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = func(arg1, arg2)
            else:
                # sin cos tan should end up here
                func = operators[token]
                arg = stack.pop() * np.pi / 180
                result = round(func(arg), 3)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError("too many parameters")
    return stack.pop()

def main():
    args = input('rpn calc> ')
    while args != 'quit' and args != 'exit' and args != 'q':
        result = calculate(args)
        print("Result:", result)
        args = input('rpn calc> ')

if __name__ == '__main__':
    main()
