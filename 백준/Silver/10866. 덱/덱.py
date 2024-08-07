# input().split()으로 입력받으면 시간초과 뜸
from collections import deque
import sys

d=deque()
N=int(input())

for i in range(N):
    command=sys.stdin.readline().split()
    if(command[0]=='push_back'):
        d.append(command[1])
    elif(command[0]=='push_front'):
        d.appendleft(command[1])
    elif(command[0]=='pop_front'):
        if(len(d)==0):
            print(-1)
        else:
            print(d.popleft())
    elif(command[0]=='pop_back'):
        if(len(d)==0):
            print(-1)
        else:
            print(d.pop())
    elif(command[0]=='size'):
        print(len(d))
    elif(command[0]=='empty'):
        if(len(d)==0):
            print(1)
        else:
            print(0)
    elif(command[0]=='front'):
        if(len(d)==0):
            print(-1)
        else:
            print(d[0])
    elif(command[0]=='back'):
        if(len(d)==0):
            print(-1)
        else:
            print(d[len(d)-1])
