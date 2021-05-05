# JumpPhotoshoot

AI-Inspired Jump Photoshoot with Body Movement Dynamics

本作品基於人工智慧人體動作分析技術之跳躍照片產生系統，利用人工智慧之人像偵測技術，偵測出每位拍攝對象的跳躍軌跡後，並對其做動作分析，達到自動化的捕捉全體拍攝對象於最高點之跳躍照片。

<p align="center">
  <img width=500 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/yolo_jump.gif" alt="JumpPhotoshoot">
</p>

## 本作品特色

本作品兼具以下三項特色：
* ***自動化系統***：不須有人按下快門，即可完成拍攝。
* ***快速獲得照片***：在短時間內獲取跳躍照片。
* ***精準選取***：精準挑選出最高點之跳躍照片。

對於所有跳躍照片的拍攝者來說，透過本作品，都可以輕鬆的拍攝出高品質的跳躍照片。

## 目錄
* [硬體需求](#硬體需求)
* [開始使用](#開始使用)
* [參考網站](#參考網站)

## 硬體需求

* Nvidia Jetson Nano
* Micro SD卡
* 網路介面卡(EW-7811Unv2)
* 攝影機(Pi Camera)
* LED模組

<p align="center">
  <img width=800 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/hardware_equipment.png" alt="JumpPhotoshoot">
</p>


## 開始使用

  ### 1. 安裝 Jetson nano 
    
  * 安裝Jetson Nano。先下載官方的[映像檔](https://developer.nvidia.com/embedded/downloads)，解壓縮後使用[映像檔燒錄軟體](https://sourceforge.net/projects/win32diskimager/)，將其燒錄至SD卡當中。
  * 若須更詳細的安裝步驟，可參考[官網安裝手冊](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)，與[這裡](https://www.rs-online.com/designspark/jetson-nano-1-cn)。
  
    * 若SD卡已使用過，必須先進行[格式化](https://blog.csdn.net/u011119817/article/details/106946176)。
  
  ### 2. 安裝硬體
  
  * 根據以下硬體接腳圖，安裝設備硬體。
  
    <p align="center">
      <img width=800 src="" alt="硬體接腳圖">
    </p>
    
  ### 3. 設定網路卡(可選)
  
  
    
    
  ### 3. 設定環境
  
  * 安裝環境
        pip install -r requirements.txt
      
  * 按[這裡](https://github.com/mdegans/nano_build_opencv)下載OpenCV安裝檔。
  * 解壓縮後，至該目錄資料夾，執行以下程式碼，進行安裝。
  
        ./build_opencv.sh
        
      * (OpenCv必須使用 4.2.0 以上版本)
  
  * 可執行以下程式確認OpenCv版本
        
        python3
        import cv2
        cv2.__version__ // 4.4.0
        
  ### 執行程式
  
  下載程式
    
    git clone https://github.com/bigmms/JumpPhotoshoot
    
  進入資料夾
  
    cd JumpPhotoshoot
  
  執行程式
  
    python3 main.py

## 參考網站

[mdegans/nano_build_opencv](https://github.com/mdegans/nano_build_opencv)

[[第一次用Jetson Nano 就上手]硬體介紹、開機步驟、遠端連線（繁體）](https://www.rs-online.com/designspark/jetson-nano-1-cn)

[Jetson Download Center](https://developer.nvidia.com/embedded/downloads)

[【 Tools 】NVIDIA® Jetson AGX Xavier 安裝 EDIMAX EW-7811Un V2 無線網卡](https://learningsky.io/tools-nvidia-jetson-agx-xavier-install-edimax-ew-7811un-v2-wifi/)

[【Jetson-Nano】SD卡重新格式化](https://blog.csdn.net/u011119817/article/details/106946176)
