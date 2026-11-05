
# Create and manipulate a small dataset in NumPy 
# • First, create a 4x5 matrix with integers from 1 to 20 (random). 
# • Add 10 to each element in the matrix.
# • Calculate the dot product of the matrix with itself (transposed). 
# • Reshape the matrix to 2x10 and 1x20.
# • Finally, sort each column of the matrix in ascending order.

import numpy as np

random_int_arr = np.random.randint (1,20, (4,5))
print (random_int_arr)

addition_random_int_arr= random_int_arr + 10
print(addition_random_int_arr)

transpose= np.dot (random_int_arr,random_int_arr.T)
print(transpose)

arr_reshaped=random_int_arr.reshape (2,10)
print(arr_reshaped)

sorted_arr= np.sort (random_int_arr, axis=0) # an balw axis=1 sortarei kata sthles
print(sorted_arr)

