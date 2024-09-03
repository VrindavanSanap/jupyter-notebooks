import matplotlib.pyplot as plt
import numpy as np

image = plt.imread("./images/building.jpg")
image_array = np.array(image, dtype=float)
plt.imshow(image_array, cmap="gray")
plt.show()


def convo2d(input, kernel):
  H, W = input.shape
  M, N = kernel.shape
  out = np.zeros((H - M + 1, W - N + 1), dtype=float)
  kernel = np.flip(kernel)
  for i in range(H - M + 1):
    for j in range(W - N + 1):
      out[i, j] = np.sum(input[i : i + M, j : j + N] * kernel)
  return out


ker = np.zeros((3, 3), dtype=float)
ker[:, 0] = -1.0
ker[:, 2] = 1.0
print(ker)

convo_out = convo2d(image_array, ker)
plt.imshow(convo_out, cmap="gray")
plt.show()

ker = np.zeros((3, 3), dtype=float)
ker[0, :] = -1.0
ker[2, :] = 1.0
print(ker)

convo_out = convo2d(image_array, ker)
plt.imshow(convo_out, cmap="gray")
plt.show()
