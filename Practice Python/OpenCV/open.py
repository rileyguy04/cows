import cv2
import numpy as np
import matplotlib.pyplot as plt

# Image Setup #
img_path = r'C:\Users\riley\Desktop\Cows\Practive Python\OpenCV\7232RR_POST.jpg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


# POLYGON #
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 5)

# TEXT #
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'DickBalls', (0,130), font, 2, (200,255,255), 1, cv2.LINE_AA)


# CV2 DRAW #
cv2.imshow('ShitBrains', img)
cv2.waitKey(0)
cv2.destroyAllWindows()