import numpy as np

arr=np.array([[1,2,3,4,5],[1,2,3,4,5]])
 
print(arr[0:2,3:4])     # PRINTING WITH AN INDEX

print(np.shape(arr))    # PRINTING THE SHAPE OF THE ARRAY ( TOTAL NUMBER AND HOW IT PLACED )

print(np.size(arr))     # PRINTING THE SIZE OF THE ARRAY

print(np.ndim(arr))     # PRINTING THE DIMENTIONS OF THE ARRAY

print(arr.dtype)        # PRINTING THE DATA TYPE OF THE ARRAY

print(type(arr))        # PRINDING THE TYPE OF THE ARRAY

print(np.arange(1,6,2,dtype=float))  # PRINTING AN ARRAY AFTER IT GENERATED ( ARANGE IS WORKING ON arrange( [start] , [stop] , [step] , [dtype]) )
