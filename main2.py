# Broadcasting

# Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions, so they match the larger array's shape.

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1.

# Little problem, see bro code video and chatgpt


# import numpy as np

# arr1=np.array([[1,2,3,4]])
# arr2=np.array([[1],[2],[3],[4]])

# print(arr1.shape)
# print(arr2.shape)

# print(arr1*arr2)


# # Exercise

# array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# # print(array1.shape)
# # print(array2.shape)

# print(array1*array2)
# print(array1+array2)



# -------------------------------------------------------------------------------------------------



# Aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print(np.sum(array)) # Sum of all elements. or do the sum of inside arrays like sum(array[0])
print(np.mean(array)) # Average of all elements
print(np.std(array)) # Measure of standard deviation
print(np.var(array)) # Variance, Square of standard deviation
print(np.min(array)) # Smallest value
print(np.max(array)) # Largest value
print(np.argmin(array)) # Position (flattened) of smallest
print(np.argmax(array)) # Position (flattened) of largest

print(np.sum(array, axis=0)) # sum column-wise (vertically)
print(np.sum(array, axis=1)) # sum row-wise (horizontally)



# ---------------------------------------------------------------------------------------------------


