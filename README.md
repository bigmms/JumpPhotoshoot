# JumpPhotoshoot

AI-Inspired Jump Photoshoot with Body Movement Dynamics
本作品基於人工智慧人體動作分析技術之跳躍照片產生系統，對每張Jetson Nano所拍攝的照片，利用人工智慧之人像偵測技術，偵測出每位拍攝對象的跳躍軌跡後，並對其做動作分析，即可達到自動化的捕捉全體拍攝對象於最高點之跳躍照片。

<p align="center">
  <img width=500 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/yolo_jump.gif" alt="JumpPhotoshoot">
</p>

## 特色
本作品兼具自動化、精準、與快速，三大特色。系統開始時，會自動偵測拍攝對象位置，並於拍攝對象準備好後，自動開始拍攝，因此，在只有一個人的情況下，也可以拍攝跳躍照片，並快速且精準的的到最高點之跳躍照片。如此一來，對於所有跳躍照片的拍攝者來說，透過本作品，都可以輕鬆的拍攝出高品質的跳躍照片。

## 目錄
* [硬體需求](#硬體需求)
* [環境需求](#環境需求)
* [開始使用](#開始使用)
* [參考網站](#參考網站)

## 硬體需求

<p align="center">
  <img width=800 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/hardware_equipment.png" alt="硬體設備">
</p>

## 環境需求

* OpenCV 4.4.0 (4.2.0 以上)
* Jetson.GPIO 2.0.11
* Numpy 1.13.3 

## 開始使用

  ### 1. 安裝 Jetson nano
  
  ### 1. 安裝硬體
  
  ### 2. 設定網路卡
  
  ### 3. 安裝 Opencv
  
  ### 執行程式
    ``` sh
    cd /home/pi/dingdang
    python dingdang.py
    ```

## 參考網站

