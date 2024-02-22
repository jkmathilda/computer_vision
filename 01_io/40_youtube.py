import cv2
import pafy

# read youtube
url = "https://www.youtube.com/watch?v=B5xckyNsWKw"
video = pafy.new(url)
best = video.getbest(preftype = 'mp4')     # 'webm','3gp'

capture = cv2.VideoCapture(best.url)
    
print("video title : {}".format(video.title))
print("video rating : {}".format(video.rating))
print("video viewcount : {}".format(video.viewcount))
print("video author : {}".format(video.author))
print("video length : {}".format(video.length))
print("video duration : {}".format(video.duration)) 
print("video likes : {}".format(video.likes))
print("video dislikes : {}".format(video.dislikes))
 
best = video.getbest(preftype='mp4')     # 'webm','3gp'
print("best resolution : {}".format(best.resolution))

cap = cv2.VideoCapture(best.url) 

# visualize video
print("visualize video...")
frameRate = 30

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(frameRate)    # show one frame for frameRate sec
    if key == 27:                   # esc == 27
        break
    
cap.release()
cv2.destroyAllWindows()

################################################################
# cv2.VideoCapture
# - Call video from camera
# - Read video files
# - Call video from youtube
# - Call video from web

# cv2.VideoCapture.get(option)
# - Return certain option the video has
################################################################
