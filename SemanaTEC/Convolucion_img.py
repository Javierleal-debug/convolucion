Convolucion_img.py

import cv2
import numpy as np

ruta = "perro.jpg"
im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
a = [ [ -1.0, 0.0, 1.0 ],
      [ -1.0, 0.0, 1.0 ],
      [ -1.0, 0.0, 1.0 ] ]
kernel = np.asarray(a)
dst = cv2.filter2D(im, -1, kernel)
print(dst.min(), dst.max())