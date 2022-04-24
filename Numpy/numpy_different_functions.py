import numpy as np;

# a simple array using list
print(np.array([1,2,3]));

# a simple array with data type mentioned
print(np.array([1,2,3],int));

# 2-D array using list
print(np.array([[1,2,3,4],[1,2,3,4]]));

# 1-D array filled with ones
print(np.ones(8,int));

# 2-D array filled with zeros
print(np.zeros((2,3),int));

# empty 4x4 array
print(np.empty((4,3),int));

# array with a range of numbers
print(np.arange(0,11,2,int));

# sort an array
print(np.sort(np.array([2,3,1,5,4])));

#shape of an array
a=np.zeros((2,3));
print(a.shape);

#dimension of an array
a=np.zeros((2,3));
print(a.ndim);

#size of the array
a=np.zeros((4,5));
print(a.size);
