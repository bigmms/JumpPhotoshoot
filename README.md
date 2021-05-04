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
* [開始使用](#開始使用)
* [參考網站](#參考網站)

## 硬體需求

<p align="center">
  <img width=800 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/hardware_equipment.png" alt="JumpPhotoshoot">
</p>


## 開始使用

  ### 1. 設定 Jetson nano
    
  * 安裝Jetson Nano。先下載官方的[映像檔](https://developer.nvidia.com/embedded/downloads)，解壓縮後使用映像檔燒錄軟體[(Win32 Disk Imager)](https://sourceforge.net/projects/win32diskimager/)，將其燒錄至SD卡當中。若須更詳細的安裝步驟，可[參考官網安裝手冊](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)，與這裡(https://www.rs-online.com/designspark/jetson-nano-1-cn)。
  
    * 若SD卡已使用過，必須先格式化，可參考[這裡](https://blog.csdn.net/u011119817/article/details/106946176)。
  
  ### 1. 硬體接腳圖
  
  * 根據下圖，接上設備硬體。
    <p align="center">
      <img width=800 src="" alt="硬體接腳圖">
    </p>
    
  ### 2. 設定網路卡(根據網路卡)
  
  
    
    
  ### 3. 設定環境
  
  * 安裝環境
    * 在這份程式當中，因
    
  * 安裝 OpenCV (因必須使用 4.2.0 以上版本)
    * 
  
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
