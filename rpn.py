#!/usr/bin/env python3

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
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
            func = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = func(arg1, arg2)
            stack.append(result)
        print(stack[0])
    if len(stack) != 1:
        raise TypeError("too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print("Result: ", result)

if __name__ == '__main__':
    main()
