import cv2

image = cv2.imread("loki")
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)
cv2.imshow("Black and White", grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
