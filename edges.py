import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
import cv2
import time

st = time.time()
image_array = plt.imread("./images/building1.jpg")
# Convert to grayscale if the image is in color
if len(image_array.shape) == 3:
    image_array = image_array.mean(axis=2)

# Calculate scale factor to resize image
target_size = 4096
scale = int(target_size / max(image_array.shape[:2]))

# Resize image
new_width = image_array.shape[1] * scale
new_height = image_array.shape[0] * scale
image_array = cv2.resize(image_array, (new_width, new_height))
image_array = scipy.ndimage.gaussian_filter(image_array, sigma=5)

big_vert_sobel = np.array([[1, 2, 0, -2, -1], [4, 8, 0, -8, -4], [6, 12, 0, -12, -6], [4, 8, 0, -8, -4], [1, 2, 0, -2, -1]])
convo_out_vert = scipy.signal.convolve2d(image_array, big_vert_sobel)
big_horz_sobel = big_vert_sobel.T
convo_out_horiz = scipy.signal.convolve2d(image_array, big_horz_sobel)

conv_out_mag = (convo_out_vert**2 + convo_out_horiz**2) ** 0.5
conv_out_mag_norm = conv_out_mag / (255 * 2)
conv_dir = np.arctan2(convo_out_vert, convo_out_horiz)
conv_dir_norm = (conv_dir + np.pi) / (np.pi * 2)
rgb_image = matplotlib.colors.hsv_to_rgb(np.dstack((conv_dir_norm, np.ones_like(conv_dir_norm), conv_out_mag_norm)))

print(f"Proccessing done in {st - time.time()} secs")
plt.imshow(rgb_image)
plt.show()