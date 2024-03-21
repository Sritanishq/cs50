import numpy as np
arr=np.zeros((30,5), dtype=int)
for x in range(0,5):
    y=pow(x+1,2)
    arr[y][x]=y
print(arr)
