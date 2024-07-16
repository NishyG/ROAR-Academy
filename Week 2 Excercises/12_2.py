import numpy as np
#Product 1
matrix_1 = np.array([[6, -9, 1], [4, 24, 8]])
print("Product 1: \n", 2 * matrix_1)


#Product 2
matrix_2 = np.array([[1, 0], [0, 1]])
matrix_3 = np.array([[6, -9, 1], [4, 24, 8]])
dot_product_1 = np.dot(matrix_2, matrix_3)
print("Product 2: \n", dot_product_1)

#Product 3
matrix_4 = np.array([[4, 3], [3, 2]])
matrix_5 = np.array([[-2, 3], [3, -4]])
dot_product_2 = np.dot(matrix_4, matrix_5)
print("Product 3:\n", dot_product_2)