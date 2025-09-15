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

# import numpy as np

# array = np.array([[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10]])

# print(np.sum(array)) # Sum of all elements. or do the sum of inside arrays like sum(array[0])
# print(np.mean(array)) # Average of all elements
# print(np.std(array)) # Measure of standard deviation
# print(np.var(array)) # Variance, Square of standard deviation
# print(np.min(array)) # Smallest value
# print(np.max(array)) # Largest value
# print(np.argmin(array)) # Position (flattened) of smallest
# print(np.argmax(array)) # Position (flattened) of largest

# print(np.sum(array, axis=0)) # sum column-wise (vertically)
# print(np.sum(array, axis=1)) # sum row-wise (horizontally)



# ---------------------------------------------------------------------------------------------------



# Filtering: refers to the process of selecting statements from an array that match a given condition

# import numpy as np

# ages=np.array([[21,17,19,20,16,30,18,65],
#                [39,22,15,99,18,19,20,21]])

# teenagers=ages[ages<18]
# adults=ages[(ages>=18) & (ages<90)]   # & -> AND,  | -> OR
# evens=ages[ages%2==0]

# print(teenagers)    # will be converted to 1-D
# print(adults)
# print(evens)

# print(ages)


# # To preserve the dimension after filtering, we have to use where

# adults1=np.where(ages>=18, ages, 0)   # we can also write np.nan insteasd of 0
# print(adults1)


# -----------------------------------------------------------------------------------------------------


# Random numbers
# Random numbers in NumPy are useful for simulations, modeling, applying random transformations, and testing purposes.

import numpy as np

rng=np.random.default_rng()

print(rng.integers(1,7))  # random no. from 1 to 6
print(rng.integers(1,100, size=(3,4)))   # basically it will give array of 3x4
print(rng.integers(low=1, high=100, size=(2,5)))   # can also give keyword arguments

# seed.  explore seed
rng1=np.random.default_rng(seed=1)   
print(rng1.integers(low=1, high=100, size=(2,2)))

# np.random.seed(seed=1)   if want to set the seed in uniform too. Explore uniform...
print(np.random.uniform(low=-1, high=1, size=(3, 2))) # floats between 2 values


# Shuffle
rng2=np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng2.shuffle(array)
print(array)


# Random Choice
rng3=np.random.default_rng()
fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
print(rng3.choice(fruits))
print(rng3.choice(fruits, size=(3, 3)))
