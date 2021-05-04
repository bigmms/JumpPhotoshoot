import cv2
import numpy as np
import matplotlib.pyplot as plt


class YOLO:
    def __init__(self, weights, labels, cfg):
        self.CONFIDENCE_THRESHOLD = 0.5
        self.NMS_THRESHOLD = 0.4

        print("You are now using {} weights ,{} configs and {} labels.".format(weights, cfg, labels))

        self.lbls = []
        with open(labels, "r") as f:  # 讀label 進來
            self.lbls = [c.strip() for c in f.readlines()]

        self.net = cv2.dnn.readNetFromDarknet(cfg, weights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        self.layer = self.net.getLayerNames()
        self.layer = [self.layer[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    # 對
    def analyze(self, heights, averages,Dir):
        print("analyze")
        heights = np.array(heights)
        frame = range(1, len(heights) + 1)
        # print(averages)
        '''plt.cla()
        plt.plot(frame, averages, 's-', color=(0, 0, 1), linestyle="-", label="TSMC")

        plt.axis([1, len(heights), 0, 0.5])
        plt.xlabel('Frame')
        plt.ylabel('Height (in %)')
        #plt.show()
        plt.savefig(Dir+"/analyze.jpg")'''

        best = np.argmax(averages)
        worst = np.argmin(averages)
        return best, worst

    # 對圖像進行偵測
    # 呼叫[人像偵測模組]與[動作分析模組]
    def detect(self, image):
        boxes, H, W, indexes = self.__peopleDetectModule(image)
        image, boxHeight, avgY = self.__motionAnalysisModule(image, indexes, boxes, H, W)

        return image, boxHeight / H, avgY / H

    # 人物偵測模組
    # 偵測[人]在何處
    def __peopleDetectModule(self, image):
        (H, W) = image.shape[:2]

        blob = cv2.dnn.blobFromImage(image, 1 / 255, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        layer_outs = self.net.forward(self.layer)

        boxes = []
        confidences = []
        class_ids = []

        biggest_people = [0, 0]
        for output in layer_outs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                if class_id != 0:  # 只選擇人
                    continue
                confidence = scores[class_id]

                if confidence > self.CONFIDENCE_THRESHOLD:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (center_x, center_y, width, height) = box.astype("int")

                    x = int(center_x - (width / 2))
                    y = int(center_y - (height / 2))
                    if int(width) > biggest_people[0] and int(height) > biggest_people[1]:
                        biggest_people = [int(width), int(height)]
                    if int(width) < biggest_people[0] / 1.5 or int(height) < biggest_people[1] / 1.5:
                        continue
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.CONFIDENCE_THRESHOLD, self.NMS_THRESHOLD)

        if len(idxs) > 0:
            tmp = []
            for i in idxs.flatten():
                tmp.append(boxes[i])
            boxes = tmp

        tmp = []
        for box in boxes:
            tmp.append(box[0])
        tmp = np.array(tmp)
        indexes = np.argsort(tmp)

        return boxes, H, W, indexes

    # 動作分析模組
    # 偵測[跳躍軌跡]
    def __motionAnalysisModule(self, image, indexes, boxes, H, W):
        hei = []
        jumpHeight = 0
        boxHeight = 0
        avgY = 0
        for index in indexes:
            box = boxes[index]
            reverse_height = ((box[1] + box[3]) - H / 2) * - 1 + H / 2
            hei.append(reverse_height / H)
            jumpHeight += reverse_height / len(boxes)
            (x, y) = (box[0], box[1])
            (w, h) = (box[2], box[3])

            colorRed = [0, 0, 255]
            #    jpg
            cv2.rectangle(image, (x, y), (x + w, y + h), colorRed, 5)
            # 平均高度
            avgY += y / len(boxes)
            boxHeight += h / len(boxes)

        if len(hei) == 0:
            hei.append(0)

        return image, boxHeight, jumpHeight
