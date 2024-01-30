import sys
import math

line = sys.stdin.readline()

while(line != ".\n"):
    stack= []
    ret = 1
    for str in line:
        if str == '(':
            stack.append(str)
        elif str == ')':
            if len(stack)<1:
                ret = 0
                break
            else:
                if stack.pop() !='(':
                    ret = 0
                    break
                else: pass
        elif str == '[':
            stack.append(str)
        elif str == ']':
            if len(stack)<1:
                ret = 0
                break
            else:
                if stack.pop() !='[':
                    ret = 0
                    break
                else: pass

    if len(stack)>0 :
        ret = 0
    print('yes') if ret else print('no')

    line = sys.stdin.readline()

    