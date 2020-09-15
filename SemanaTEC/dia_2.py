dia_2.py

import cv2
import numpy as np

img = "perro.png"
im = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
a = [ [ -1.0, 0.0, 1.0 ],
      [ -1.0, 0.0, 1.0 ],
      [ -1.0, 0.0, 1.0 ] ]
kernel = np.asarray(a)
dst = cv2.filter2D(im, -1, kernel)
print(dst.min(), dst.max())
