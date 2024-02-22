import os
import cv2

# read image
print("read image...")
img = cv2.imread(os.path.join('.', 'data', 'bear.jpg'))

# Binarization
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set threshold
# cv2.threshold(src, thresh, maxval, type, dst=None) -> retval, dst
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh2 = cv2.blur(thresh, (10, 10))
ret, thresh2 = cv2.threshold(thresh2, 80, 255, cv2.THRESH_BINARY)

# visualize image
print("visualize image...")
cv2.imshow('original', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh2', thresh2)

cv2.moveWindow('img_gray', 200,200) # change window placement
cv2.moveWindow('thresh', 400,400) # change window placement
cv2.moveWindow('thresh2', 600,600) 

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()