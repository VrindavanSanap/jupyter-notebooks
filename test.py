import numpy as np
import torch

numpy_array = np.array([1, 2, 3, 4, 5])
tensor_a = torch.from_numpy(numpy_array)
tensor_a *= 2
print(numpy_array)  # Output: [2, 4, 6, 8, 10]

numpy_array = np.array([1, 2, 3, 4, 5])
tensor_a = torch.tensor(numpy_array)
tensor_a *= 2
print(numpy_array)  # Output: [2, 4, 6, 8, 10]

