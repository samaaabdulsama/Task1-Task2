#to install numpy library => pip install numpy
import numpy as np

# Creating a 2D array (matrix)
OriginalMatrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array (Matrix):\n", OriginalMatrix)

# Array broadcasting (adding a scalar to all elements)
MatrixBroadcasting = OriginalMatrix + 10
print("\nArray after broadcasting (adding 10):\n", MatrixBroadcasting)

# multiplication of two arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
MatrixMultiplication = arr1 * arr2
print("\nElement-wise product of two arrays:\n", MatrixMultiplication)

# Matrix multiplication using dot()
matrix_product = np.dot(arr1, arr2)
print("\nMatrix product of two arrays:\n", matrix_product)

# Advanced indexing (selecting specific elements or sub-arrays)
# Selecting elements at specific indices
indices = np.array([0, 2])
selected_elements = OriginalMatrix[indices, 1] # Select elements from column 1 at (row 0 , row 2)
print("\nSelected elements using advanced indexing:", selected_elements)

# Slicing with steps
sliced_array = np.arange(10)[::2] # Every second element from 0 to 9
print("\nSliced array with step:", sliced_array)