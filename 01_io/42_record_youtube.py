import cv2
import pafy

# read youtube
url = "https://www.youtube.com/watch?v=IBeDtsL95XM"
video = pafy.new(url)
best = video.getbest(preftype = 'mp4')     # 'webm','3gp'
print("best resolution : {}".format(best.resolution))

cap = cv2.VideoCapture(best.url) 
 
# read frame Info
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
# capture frame
frameRate = int(cap.get(cv2.CAP_PROP_FPS))
 
frame_size = (frameWidth, frameHeight)
print('frame_size={}'.format(frame_size))
print('fps={}'.format(frameRate))
 
# cv2.VideoWriter_fourcc(*'codec')
# codec and recording related settings
# Set encoding method
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#fourcc = cv2.VideoWriter_fourcc(*'MPEG')
#fourcc = cv2.VideoWriter_fourcc(*'X264')
 
out1Path = 'data/recode1.mp4'
out2Path = 'data/recode2.mp4'
 
# Save video
# out1Path : File name
# fourcc : Settings for frame zip (encoding, codec, etc)
# frame_size : frame size(width, height)
# isColor : colour or black&white
out1 = cv2.VideoWriter(out1Path, fourcc, frameRate, frame_size)
out2 = cv2.VideoWriter(out2Path, fourcc, frameRate, frame_size)

# visualize video
print("visualize video & recoding... (wait 5min)")
while True:
    # Call single image
    # image -> frame
    # read successfully? -> retval
    retval, frame = cap.read()
    if not(retval):
        break  # if failed to read the frame information successfully break from the while loop
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# change colour to grey
    edges = cv2.Canny(gray, 100, 200)	# Canny function to detect the edge
    
    # Write on video file
    out1.write(frame)
    out2.write(edges)
    
    # print
    cv2.imshow('frame', frame)
    cv2.imshow('edges', edges)
    
    key = cv2.waitKey(frameRate)
    if key == 27:                   # esc == 27
        break
        
if cap.isOpened():
    cap.release()
    out1.release()
    out2.release()
    
cv2.destroyAllWindows()