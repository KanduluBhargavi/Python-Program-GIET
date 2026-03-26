import numpy as np
arr=np.array([1,2,3],dtype='int64')
print(arr.dtype)
arr=arr.astype("float64")
print("updated",arr.dtype)