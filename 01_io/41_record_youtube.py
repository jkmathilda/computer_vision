import cv2
import pafy

# read youtube
url = "https://www.youtube.com/watch?v=IBeDtsL95XM"
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest(preftype = 'mp4')     # 'webm','3gp'
print("best resolution : {}".format(best.resolution))
 
cap = cv2.VideoCapture(best.url) 
 
# frame size
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)
 
# Set codec
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
 
# Create file to save an image
out1Path = 'data/recode1.mp4'
out2Path = 'data/recode2.mp4'

out1 = cv2.VideoWriter(out1Path, fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter(out2Path, fourcc, 20.0, frame_size, isColor=False)

# visualize video
print("visualize video & recoding... (wait 5min)")
print("### if you want exit, press a 'ESC' key ###")

while True:
    retval, frame = cap.read()  # Read each frames of the videos
    if not(retval):
        break
    out1.write(frame)	# Save in video file
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# change to black and white
    out2.write(gray)	# Save video in the file
    
    cv2.imshow('frame', frame)
    cv2.imshow('edges', gray)
    
    key = cv2.waitKey(30)
    if key == 27:   # ESC key
        break
         
if cap.isOpened():
    cap.release()
    out1.release()
    out2.release()
    
cv2.destroyAllWindows()