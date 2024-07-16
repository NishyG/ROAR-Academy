import numpy as np
arr = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35], [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55]])

pink_slice = arr[1, 2:4]
print("Pink Slice:\n", pink_slice)

blue_slice = arr[0:6, 1]
print("Blue Slice:\n", blue_slice)

green_slice = arr[2:4, 4:]
print("Green slice:\n", green_slice)

orange_slice = arr[2:5:2, ::2]
print("Orange Slice:\n", orange_slice)