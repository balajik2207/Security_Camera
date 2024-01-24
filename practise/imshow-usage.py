import cv2

image = cv2.imread(r'../image.jpg')

window = 'image'

cv2.imshow(window, image)


cv2.waitKey(0)

cv2.destroyAllWindows() 