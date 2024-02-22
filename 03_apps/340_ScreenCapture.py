import cv2
import numpy as np
from PIL import ImageGrab

screenshot = ImageGrab.grab()
screenshot = np.array(screenshot)                           # Since saved pil can't be used as opencv, convert to numpy
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)    # Since opencv saves as BRG, need to convert

cv2.imshow('Screen Capture',screenshot)

# waiting
print("- wait 2 sec")
cv2.waitKey(2000)   # waiting 2sec=2000ms
# cv2.waitKey(0)    # waiting unlimited..

cv2.destroyAllWindows()
