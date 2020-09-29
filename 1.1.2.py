import math
res = 0.0953
i = 25
for i in range (1, 25):
    res = 1/(10*i) - res/10
    i = i - 1
print (res)
