import math
res = 0.0953
i = 0
for i in range (0, 25):
    i = i + 1
    res = 1/i - 0.1*res
print (res)
