import time
import glob

import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

CONFIDENCE_THRESHOLD = 0.3
NMS_THRESHOLD = 0.5

weights = glob.glob("yolo/*.weights")[0]
labels = glob.glob("yolo/*.txt")[0]
cfg = glob.glob("yolo/*.cfg")[0]

print("You are now using {} weights ,{} configs and {} labels.".format(weights, cfg, labels))

lbls = []
with open(labels, "r") as f:  # 讀label 進來
    lbls = [c.strip() for c in f.readlines()]

net = cv2.dnn.readNetFromDarknet(cfg, weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

layer = net.getLayerNames()
layer = [layer[i[0] - 1] for i in net.getUnconnectedOutLayers()]


def detect(image, nn, output_index):
    (H, W) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(image, 1 / 255, (416, 416), swapRB=True, crop=False)
    nn.setInput(blob)
    start_time = time.time()
    layer_outs = nn.forward(layer)
    end_time = time.time()

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

            if confidence > CONFIDENCE_THRESHOLD:
                if class_id != 0:
                    continue
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

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    # print(boxes)
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
    hei = []
    total_height = 0
    for index in indexes:
        box = boxes[index]
        reverse_height = ((box[1] + box[3]) - H / 2) * -1 + H / 2
        hei.append(reverse_height / H)
        # hei.append(reverse_height)
        total_height += reverse_height / len(boxes)
        (x, y) = (box[0], box[1])
        (w, h) = (box[2], box[3])
        colorRed = [0, 0, 255]
        cv2.rectangle(image, (x, y), (x + w, y + h), colorRed, 5)
        # text = "{}".format("person")
        # cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.putText(image, str(output_index), (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        label = "Inference Time: {:.2f} ms".format(end_time - start_time)
        # cv2.putText(image, label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    if len(hei) == 0:
        hei.append(0)
    
    if H < W:
        # cv2.imshow("image", (cv2.resize(image, (1000, 750), cv2.INTER_CUBIC)))
        cv2.imwrite('./output_' + str(output_index) + ".jpg", cv2.resize(image, (800, 600)))
    else:
        # cv2.imshow("image", (cv2.resize(image, (750, 1000), cv2.INTER_CUBIC)))
        cv2.imwrite('./output_' + str(output_index) + ".jpg", cv2.resize(image, (600, 800)))
   
    #cv2.waitKey(0)

    # image.resize(600, 800, 3)
    # image = cv2.resize(image, (1000, 750), cv2.INTER_CUBIC)  # resize to 800x600
    # cv2.imshow("image", image)
    # if args["output"] != "":
    #     cv2.imwrite(args["output"], image)
    return hei, total_height / H


def calculate(pictures):
    heights = []
    averages = []
    index = 1
    for picture in pictures:
        height, average = detect(picture, net, index)
        heights.append(height)
        averages.append(average)
        index += 1

    heights = np.array(heights)
    frame = range(1, len(heights) + 1)

    for height in heights.T:
        plt.plot(frame, height, 's-', color=(0, random.random(), 0), label="TSMC")
    plt.plot(frame, averages, 's-', color=(0, 0, 1), linestyle="-", label="TSMC")
    plt.axis([1, len(heights), 0,1])
    plt.xlabel('Frame')
    plt.ylabel('Height (in %)')
    plt.show()

    best = np.argmax(averages)
    # print(pictures[best])
    image = pictures[best]
    if image.shape[0] < image.shape[1]:
        cv2.imshow("output.jpg", (cv2.resize(image, (1000, 750), cv2.INTER_CUBIC)))
        #cv2.imwrite("output.jpg", cv2.resize(image, (1000, 750)))
    else:
        cv2.imshow("output.jpg", (cv2.resize(image, (750, 1000), cv2.INTER_CUBIC)))
        #cv2.imwrite("output.jpg", cv2.resize(image, (1000, 750)))
    #cv2.waitKey(0)
    print("-------------------------------------------------------")
