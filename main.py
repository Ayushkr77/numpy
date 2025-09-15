# import numpy as np

# # print(np.__version__)


# my_list=[1,2,3,4]
# print(my_list)
# my_list=my_list*2
# print(my_list)


# # using numpy array, like vector
# array=np.array([1,2,3,4])
# print(array)
# print(type(array))   # <class 'numpy.ndarray'>   nd means N-dimensional
# array*=2
# print(array)



# -----------------------------------------------------------------------------------------



# import numpy as np

# arr=np.array('A')
# print(arr.ndim)   # ndim means number of dimensions
# arr1=np.array(['a','b','c'])
# print(arr1.ndim)
# arr2=np.array([['a','b','c'],[1,2,3],['10','a','asd'],[97,183,70]])  # Since you mixed strings ('a','b','c') and numbers (1,2,3), NumPy will upcast everything to the most general type that can hold all values → in this case, string. If all were int, then int only will be printed.   And all must have same number of elements, otherwise error
# print(arr2)

# array = np.array([[['A', 'B'], ['D', 'E'], ['G', 'H']],
#                 [['J', 'K'], ['M', 'N'], ['P', 'Q']],
#                 [['S', 'T'], ['V', 'W'], ['Y', ' ']],
#                 [[1,2], [4,5], [7,9]]])
# print(array.ndim) 
# print(array.shape) #returns a tuple of integers that represent the shape.   Depth, no. of rows, no. of columns. (4 “blocks”, each 3×2).
# # You have 4 blocks (outermost list). 
# # Each block has 3 rows. 
# # Each row has 2 elements. 
# print(array)
# print(array[0][0][0])   # known as chain indexing

# # now multidimensional indexing which is faster than chain indexing
# print(array[0,0,0])


# # exercise
# word=array[0,0,0]+array[1,0,1]+array[3,2,0]
# print(word)



# -----------------------------------------------------------------------------------------


# # Slicing in numpy
# # Subscript operator([])

# # Row Slicing

# import numpy as np

# array = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])

# # array[start:end:step]

# print(array[0])
# print(array[-1])

# print(array[0:2])   # end index is exclusive
# print(array[1:])     # if we skip end index, it will take up to the end

# print(array[0:4:2])   

# print(array[:])

# print(array[::2])
# print(array[::-1])



# # Column Slicing

# print(array[0,0])   # [row, col]

# print(array[:,1])    # in the row part i.e., before ',' we wrote : it means that it is for all the rows
# print(array[:,-1])

# print(array[:,0:3])   # first 3 columns
# print(array[:,1:4])    # or array[:,1:]

# print(array[:, ::2])



# # Row and Col Slicing

# print(array[0:2,0:2])
# print(array[0:2,2:4])
# print(array[2:,0:2])



# -----------------------------------------------------------------------------------------


import numpy as np
# Arithmetic

# Scalar Arithmetic

arr=np.array([1,2,3])

# arr=arr+2
# arr*=2
# print(arr)

print(arr+2)
print(arr-1)
print(arr*2)
print(arr/4)
print(arr**5)
print(arr)

# Vectorized Math functions

arr1=np.array([1.01,2.5,3.99])

# arr1=np.sqrt(arr1)
# print(arr1)

print(np.sqrt(arr1))
print(np.round(arr1))
print(np.floor(arr1))
print(np.ceil(arr1))

print(np.pi)



# Exercise

radii=np.array([1,2,3])
print(f"Area: {np.pi*radii**2}")


# Element wise arithmetic

array1=np.array([1,2,3])
array2=np.array([4,5,6])

# array1=array1+array2
# print(array1)

print(array1+array2)
print(array2-array1)
print(array1*array2)
print(array1/array2)
print(array1**array2)




# Comparison Operators

scores=np.array([91,55,100,70,83])

print(scores==100)   # will return a boolean array
print(scores>=60)
print(scores<60)

# we can also use conditional assignment, say whoever scored below 60, assign them to 0
scores[scores<60]=0
print(scores)