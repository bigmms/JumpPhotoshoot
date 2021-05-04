import cv2
import copy

class Camera:
    def __init__(self):
        GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=(string)NV12, framerate=5/1 ! nvvidconv flip-method=2 ! video/x-raw, width=3264, height=2464, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink wait-on-eos=false max-buffers=1 drop=True'
        self.webcam = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)

    def release(self):
        self.webcam.release()
    def __del__(self):
        self.webcam.release()

    def getFrame(self):
        ret, frame = self.webcam.read()
        return frame

    def shoot(self, shootNum, yolo,saveDir):
        captureList = []
        heights = []
        averages = []
        
        for i in range(shootNum):
            image = self.getFrame()
            cv2.imwrite(saveDir+'/'+str(i)+".jpg",image)
            newImage = copy.deepcopy(image)
            captureList.append(image)
            imageDec,boxHeight, avgY = yolo.detect(newImage)
            
            if i == 0:
                first_Y = avgY
                
            real_height = (170 / (boxHeight+0.000001)) * (avgY-first_Y)
            #cv2.putText(imageDec, str(real_height), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

            heights.append(boxHeight)
            averages.append(avgY)
            
            # cv2.imshow("preview", image)
            # cv2.waitKey(1)
        return captureList, heights, averages
