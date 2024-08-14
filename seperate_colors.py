import sys
import cv2
import numpy as np

np.set_printoptions(precision=2)

if __name__ == "__main__":
  if len(sys.argv) == 2:
    file_name = sys.argv[1]
  else:
    file_name = "./image.jpg"
  image = cv2.imread(file_name)
  # In opencv the order of color channels is
  # BGR (blue, green, red)

  red_image = image.copy()
  red_image[:, :, :2] = 0

  blue_image = image.copy()
  blue_image[:, :, 1:] = 0

  green_image = image.copy()
  green_image[:, :, 0] = 0
  green_image[:, :, 2] = 0

  blue_channel_avg = np.mean(image[:, :, 0])
  green_channel_avg = np.mean(image[:, :, 1])
  red_channel_avg = np.mean(image[:, :, 2])
  print(f"Channel averages are B-{blue_channel_avg:.2f}, G-{green_channel_avg:.2f}, R-{red_channel_avg:.2f}")
  # file_name = file_name.split('.')[0]
  cv2.imwrite(f"red_channel.jpg", red_image)
  cv2.imwrite(f"blue_channel.jpg", blue_image)
  cv2.imwrite(f"green_channel.jpg", green_image)
