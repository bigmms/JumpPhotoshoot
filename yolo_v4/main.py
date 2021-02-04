import cv2
import yolo_image
import time
import threading
def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=800,
    display_height=600,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
webcam = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
captureList = []
mode = "preview"
count = 0
isPressQ = False
strTime = 0
CAPTURE_MAX = 30  
try:
  while True:
      # 從攝影機擷取一張影像
      ret, frame = webcam.read()
      # 顯示圖片
      cv2.imshow('frame', frame)

      # read command
      comd = cv2.waitKey(1)

      # "q" exit camera
      if comd == ord('q'):
          break
      # "p" take picture
      elif comd == ord('p'):
          count = 0
          strTime = time.time()
          isPressQ = True
          print("p")
      if isPressQ:
          #print(time.time() - strTime)
          #if (time.time() - strTime > 10):
          mode = "capture"
          isPressQ = False


      if mode == "capture":
          print("capture")
          if count == 0:
              captureList.clear()

          captureList.append(frame)

          if count == CAPTURE_MAX-1:
              mode = "preview"
              threads = threading.Thread(target = yolo_image.calculate(captureList))
              threads.start()

          count += 1
finally:
  threads.join()
  webcam.release()
