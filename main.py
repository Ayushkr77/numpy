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



import numpy as np

arr=np.array('A')
print(arr.ndim)   # ndim means number of dimensions
arr1=np.array(['a','b','c'])
print(arr1.ndim)
arr2=np.array([['a','b','c'],[1,2,3],['10','a','asd'],[97,183,70]])  # Since you mixed strings ('a','b','c') and numbers (1,2,3), NumPy will upcast everything to the most general type that can hold all values → in this case, string. If all were int, then int only will be printed.   And all must have same number of elements, otherwise error
print(arr2)

array = np.array([[['A', 'B'], ['D', 'E'], ['G', 'H']],
                [['J', 'K'], ['M', 'N'], ['P', 'Q']],
                [['S', 'T'], ['V', 'W'], ['Y', ' ']],
                [[1,2], [4,5], [7,9]]])
print(array.ndim) 
print(array.shape) #returns a tuple of integers that represent the shape.   Depth, no. of rows, no. of columns. (4 “blocks”, each 3×2).
# You have 4 blocks (outermost list). 
# Each block has 3 rows. 
# Each row has 2 elements. 
print(array)
print(array[0][0][0])   # known as chain indexing

# now multidimensional indexing which is faster than chain indexing
print(array[0,0,0])


# exercise
word=array[0,0,0]+array[1,0,1]+array[3,2,0]
print(word)