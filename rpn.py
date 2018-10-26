#!/usr/bin/env python3

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
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 + arg2
            stack.append(result)
            return stack[0]

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print(result)

if __name__ == '__main__':
    main()
