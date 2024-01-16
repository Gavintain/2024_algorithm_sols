import sys
import math
line1= sys.stdin.readline().strip()
ABV = line1.split()
A=int(ABV[0])
B=int(ABV[1])
V=int(ABV[2])
X=(V-B)/(A-B)
print(math.ceil(X))
    
