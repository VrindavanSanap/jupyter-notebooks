from flask import Flask, request, jsonify, send_file
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
import cv2
import io

app = Flask(__name__)


@app.route("/process_image", methods=["POST"])
def process_image():
  file = request.files["image"]
  image_array = plt.imread(file)

  if len(image_array.shape) == 3:
    image_array = image_array.mean(axis=2)

  scale = int(4096 / max(image_array.shape))
  image_array = cv2.resize(image_array, (image_array.shape[1] * scale, image_array.shape[0] * scale))

  convo_out_blur = scipy.ndimage.gaussian_filter(image_array, sigma=5)

  big_vert_sobel = np.array([[1, 2, 0, -2, -1], [4, 8, 0, -8, -4], [6, 12, 0, -12, -6], [4, 8, 0, -8, -4], [1, 2, 0, -2, -1]])
  convo_out_vert = scipy.signal.convolve2d(convo_out_blur, big_vert_sobel)

  big_horz_sobel = big_vert_sobel.T
  convo_out_horiz = scipy.signal.convolve2d(convo_out_blur, big_horz_sobel)

  conv_out_mag = (convo_out_vert**2 + convo_out_horiz**2) ** 0.5
  conv_out_mag_norm = conv_out_mag / (255 * 2)

  conv_dir = np.arctan2(convo_out_vert, (convo_out_horiz))
  conv_dir_norm = (conv_dir + np.pi) / (np.pi * 2)
  rgb_image = matplotlib.colors.hsv_to_rgb(np.stack((conv_dir_norm, np.ones_like(conv_dir_norm), conv_out_mag_norm), axis=-1))

  plt.imshow(rgb_image)
  img_buf = io.BytesIO()
  plt.savefig(img_buf, format="png")
  img_buf.seek(0)

  return send_file(img_buf, mimetype="image/png")


if __name__ == "__main__":
  app.run(debug=False)
