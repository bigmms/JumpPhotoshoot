# AI-Inspired Jump Photoshoot

AI-Inspired Jump Photoshoot , by using human detection of artificial intelligence technology, detecting every people who are being photographed to get the jumping track. Next, our works use detection analysis to analysis the track to acheive automatically capture the image that people being photographed at the highest point.

<p align="center">
  <img width=500 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/yolo_jump.gif" alt="JumpPhotoshoot">
</p>

## Features <!--##本作品特色 -->

Our works have the following three feature:
* ***Automatic System***：Without others to triger the shutter, everyone can take the jumping image by himself/herself .
* ***Rapidly Obtain***：In the period of time, the photographer can get the jumping image.
* ***Percisely Select***： AI-Inspired Jump Photo shoot percisely pick up the highest jumping image.
With our works, All photographer who cature jumping image can easily get the high quality jumping image.

## Content <!-- ## 目錄 -->

* [HardwareRequirement](#Hardware Requirement)
* [GettingStart](#Getting Start)
* [Reference](##Reference)

## Hardware Requirement<!--##硬體需求 -->

  * Nvidia Jetson Nano
  * Micro SD Card
  * Network Interface Card(EW-7811Unv2)<!--   * 網路介面卡(EW-7811Unv2) -->
  * cmaera(Pi Camera) <!--   * 攝影機(Pi Camera) -->
  * LED Module <!--* LED模組 -->

  <p align="center">
    <img width=800 src="https://github.com/bigmms/JumpPhotoshoot/blob/main/img/hardware_equipment.png" alt="JumpPhotoshoot">
  </p>

## Getting Start <!-- ## 開始使用 -->

  ### Setup Jetson Nano
    
  * 安裝Jetson Nano。先下載官方的[映像檔](https://developer.nvidia.com/embedded/downloads)，解壓縮後使用[映像檔燒錄軟體](https://sourceforge.net/projects/win32diskimager/)，將其燒錄至SD卡當中。
  * 若須更詳細的安裝步驟，可參考[官網安裝手冊](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)，與[這裡](https://www.rs-online.com/designspark/jetson-nano-1-cn)。
  
    * 若SD卡已使用過，必須先進行[格式化](https://blog.csdn.net/u011119817/article/details/106946176)。
  
  ### Setup Hardware
  
  * 根據以下硬體接腳圖，安裝設備硬體。
  
    <p align="center">
      <img width=800 src="" alt="硬體接腳圖">
    </p>
    
  ### Setup The Internet(if you use EW-7811Unv2)
  
  
  
  ### Setup enviroment
  
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
        
  ### Execute the program
  
  * Download
        
        git clone https://github.com/bigmms/JumpPhotoshoot
    
  * Get into the Floder
  
        cd JumpPhotoshoot
        
  * Run the main.py
  
        python3 main.py

## Reference

[mdegans/nano_build_opencv](https://github.com/mdegans/nano_build_opencv)

[[第一次用Jetson Nano 就上手]硬體介紹、開機步驟、遠端連線（繁體）](https://www.rs-online.com/designspark/jetson-nano-1-cn)

[Jetson Download Center](https://developer.nvidia.com/embedded/downloads)

[【 Tools 】NVIDIA® Jetson AGX Xavier 安裝 EDIMAX EW-7811Un V2 無線網卡](https://learningsky.io/tools-nvidia-jetson-agx-xavier-install-edimax-ew-7811un-v2-wifi/)

[【Jetson-Nano】SD卡重新格式化](https://blog.csdn.net/u011119817/article/details/106946176)
