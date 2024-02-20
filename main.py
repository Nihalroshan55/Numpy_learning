import numpy as np

arr=np.array([[1,2,3,4,5],[1,2,3,4,5]])
 
print(arr[0:2,3:4])     # PRINTING WITH AN INDEX    [[4][4]]

print(np.shape(arr))    # PRINTING THE SHAPE OF THE ARRAY ( TOTAL NUMBER AND HOW IT PLACED )    (2, 5)

print(np.size(arr))     # PRINTING THE SIZE OF THE ARRAY    10

print(np.ndim(arr))     # PRINTING THE DIMENTIONS OF THE ARRAY  2

print(arr.dtype)        # PRINTING THE DATA TYPE OF THE ARRAY   int64

print(type(arr))        # PRINDING THE TYPE OF THE ARRAY    <class 'numpy.ndarray'>


#   arange():
#   arange () function will generate the array with the given value 

print(np.arange(1,6,2,dtype=float))  # PRINTING AN ARRAY AFTER IT GENERATED ( ARANGE IS WORKING ON arrange( [start] , [stop] , [step] , [dtype]) )  [1. 3. 5.]

#   creating 2 numpy arrays using arange and adding it  
print(np.arange(1,6),"var1")    #   [1 2 3 4 5] var1
print(np.arange(1,6),"var2")    #   [1 2 3 4 5] var2
var1=np.arange(1,6)
var2=np.arange(1,6)
var3=var1+var2  # Here this two array will sum up the element with same index
print(var3)     # this is the out put  [ 2  4  6  8 10]


#   numpy.zeros():

#   numpy.zeros() function returns a new arrayof given shape and type with zero

print(np.zeros(2))   # [0. 0.]

#   the first value provides with the rows and the other provides withe the columns 
print(np.zeros((2,3))) #    [[0. 0. 0.]
                        #   [0. 0. 0.]]

#    default data type is float we can over ride with the dtype
print(np.zeros((2,3),dtype=int))    #   [[0 0 0]
                                    #   [0 0 0]]



#   ones():
#   The ones() function returns a new array of given shape and data type, where the element’s value is set to 1. This function is very similar to numpy zeros()

print(np.ones(1))   #   [1.]

#   the first value provides with the rows and the other provides withe the columns 
print(np.ones((2,3)))   #   [[1. 1. 1.]
                        #   [1. 1. 1.]]

#    default data type is float we can over ride with the dtype
print(np.ones((2,3),dtype=int))    #   [[1 1 1]
                                    #   [1 1 1]]


#   full():
#   numpy.full(shape,fill_value,dtype) return a new array with the same shape and type as a given array filled with a fill_value

#   first value have the count no.of row as shape and other will be the number that want to be filled 
print(np.full(3,4)) #   [4 4 4]

#   here we given the row and the column
print(np.full((2,3),8)) #   [[8 8 8]
                        #   [8 8 8]]

#    the default type is int
print(np.full((2,3),8,dtype=float)) #   [[8. 8. 8.]
                                    #   [8. 8. 8.]]