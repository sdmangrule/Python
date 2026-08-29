def create():
    data = [1,2,3]

    def inner():
        data.pop()
        return data
    
    return inner

a = create()

# print(a())
# print(a())
# print(a())


import numpy as np
print(np.__version__)


table = np.array([
       [5, 3, 7, 1],
      [2, 6, 7 ,9],
      [1, 1, 1, 1],
    [4, 3, 2, 0],
  ])

print(table.max())
#Out[3]: 9

print(table.max(axis=0))
#Out[4]: array([5, 6, 7, 9])

print(table.max(axis=1))
#Out[5]: array([7, 9, 1, 4])



# Using reshape() method
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.shape)
reshaped_arr = arr.reshape(2, 2)
print(reshaped_arr)
print(reshaped_arr.shape)