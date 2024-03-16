import numpy as np
arr=np.zeros((30,6))
for x in range(1,6):
    y=pow(x,2)
    arr[y][x]=y
print(arr)