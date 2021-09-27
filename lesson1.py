import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./python.png', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image', img)

### Show image with pyplot
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([100, 200], [300, 350], 'r', linewidth=5)
plt.show()

###Save Image
cv2.imwrite('imgout.jpg', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
