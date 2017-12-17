#!usr/bin/env python

def get_sum(a,b):
    '''任意两整数的和'''
    sum = 0
    if a > b:
        for i in range(a, b - 1, -1):
            sum += i
    elif a < b:
        for i in range(a, b+1):
            sum += i
    else:
        sum = a
    return sum

if __name__=='__main__':
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    print(get_sum(a,b))







