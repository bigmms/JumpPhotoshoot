import cv2
import YOLO
import time
import Camera
import glob
import Timer
import LED
import os 
captureNum = 15
'''====================save================================='''
ROOT = "/home/nvidia/Documents/v8/images"
saveIndex = 0
'''====================yolo================================='''
weights = glob.glob("yolo/*.weights")[0]
labels = glob.glob("yolo/*.txt")[0]
cfg = glob.glob("yolo/*.cfg")[0]
'''====================led=================================='''
ledRed = LED.LED(LED.PIN_RED)
ledGre = LED.LED(LED.PIN_GRE)
ledYel = LED.LED(LED.PIN_YEL)
'''====================function============================='''
#create save dir
def createSaveDir():
    global saveIndex
    # if system start
    if saveIndex == 0:
        dirList = os.listdir(ROOT)
        # dir is not empty
        if len(dirList) != 0:
            dirList = [int(f) for f in dirList]
            saveIndex = max(dirList) 
        # dir is empty
        else:
            saveIndex = 0
    saveIndex += 1
    saveDir = os.path.join(ROOT,str(saveIndex))
    os.mkdir(saveDir)
    return saveDir

# 停留一秒:
# case1: [現在相片]的[平均y座標]與[一秒前相片]的[平均y座標]差距小於 1/50 兩張人像的平均高度
# case2: [現在相片]的[平均高度]與[一秒前相片]的[平均高度]差距小於 1/50 兩張人像的平均高度
def stay(yNow, yOneSecBef, boxHeightNow, boxHeightBef):
    if boxHeightBef != -1 and boxHeightNow != -1:
        yDis = abs(yNow - yOneSecBef)
        hDis = abs(boxHeightNow - boxHeightBef)
        boxHeightAvg = (boxHeightNow + boxHeightBef)/2

        con1 = yDis < (boxHeightAvg / 50)
        con2 = hDis < (boxHeightAvg / 50)
        if con1 and con2:
            return True
    return False

# 開始執行相機
def cameraStart(camera, yolo):
    timer = Timer.Timer()

    cameraTimer = Timer.Timer()
    analyzeTimer = Timer.Timer()

    jumpHeightBef = 1000000 # last jumping height
    boxHeightBef = 1000000 # last 
 
    nowtime = time.time()
    oldtime = time.time()
    # print("press q exit")
    while True:
        ledGre.off()
        frame = camera.getFrame()
        # time
        nowtime = time.time()
        #print(nowtime - oldtime)
        oldtime = nowtime
        # detect 
        decFrame, boxHeightNow, jumpHeightNow = yolo.detect(frame)
        # ledPreview
        ledRed.on()
        # detect people
        if boxHeightNow != 0:
           ledYel.on()
        else:
           ledYel.off()
        # update timer
        timer.update()
        # 隔一秒拍一張
        if timer.isOneSecond():
            conStay = stay(jumpHeightNow, jumpHeightBef, boxHeightNow, boxHeightBef)
            # 如果靜止1秒
            if conStay:
                # 倒數三秒
                timer.cntDown(camera)
                # create save dir
                saveDir = createSaveDir()
                # led shoot
                ledYel.on()
                # start cameraTimer
                cameraTimer.start()
                # 連拍 captureNum 張數
                captureList, heights, averages = camera.shoot(captureNum, yolo,saveDir)
                cameraTime = cameraTimer.stop()
                # led analyze
                ledYel.off()
                ledGre.on()
                # 輸入 yolo 進行分析
                analyzeTimer.start()
                bestIdx, worstIdx = yolo.analyze(heights, averages,saveDir)
                analyzeTime = analyzeTimer.stop()
                # 獲得最高的相片
                imageBst = captureList[bestIdx]
                # save 照片
                cv2.imwrite(saveDir+"/output.jpg", imageBst)
                # save index
                with open(saveDir+"/bestIdx.txt",'w') as f:
                   f.write(str(bestIdx))
                # save evlTime
                with open(saveDir+"/time.txt",'w') as f:
                   f.write("camera time: " + str(cameraTime)+'\n')
                   f.write("analyze time: "+str(analyzeTime)+'\n')
                   f.write("total time: "+str(cameraTime+analyzeTime)+'\n')

            boxHeightBef = boxHeightNow
            jumpHeightBef = jumpHeightNow
        # press q exit
        if cv2.waitKey(1) == ord('q'):
           break
        # cv2.imshow("preview", decFrame)


'''====================main==================================='''
if __name__ == '__main__':
    try:
        camera = Camera.Camera()
        yolo = YOLO.YOLO(weights, labels, cfg)
        cameraStart(camera, yolo)
    finally:
        camera.release()
    ledRed.off()
    ledGre.off()
    ledYel.off()
