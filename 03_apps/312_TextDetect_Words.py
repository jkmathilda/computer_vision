import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
from os import path

# https://www.youtube.com/watch?v=6DjFscX4I_c

if path.exists('/usr/local/bin/tesseract'):
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
elif path.exists('/opt/homebrew/bin/tesseract'):
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
else:
    print('check a tesseract binary')
    quit(1)

img = cv2.imread('data/textsimple.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

##############################################
##### Image to String   ######
##############################################
print(pytesseract.image_to_string(img))

##############################################
##### Detecting Words  ######
##############################################
# #[   0          1           2           3           4          5         6       7       8        9        10       11 ]
# #['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
boxes = pytesseract.image_to_data(img)
for a,b in enumerate(boxes.splitlines()):
    print(b)
    if a!=0:
        b = b.split()
        if len(b)==12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
            cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)

#############################################
#### View Image  ######
#############################################
cv2.imshow('Image', img)

# waiting
print("### if you want exit, press a 'ESC' key ###")
while(True):
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break

cv2.destroyAllWindows()


#############################################
# Install tesseract on MacOS
#############################################

# brew install imagemagick
# brew install tesseract
# brew install tesseract-lang
# tesseract --list-langs

# which tesseract
# --> /opt/homebrew/bin/tesseract

# pip install pytesseract
# pip install Pillow
