# IDEA Lab实习笔记 7-23

Table of Contents
=================

   * [IDEA Lab实习笔记 7-23](#idea-lab实习笔记-7-23)
      * [服务器环境搭建](#服务器环境搭建)
         * [远程服务器](#远程服务器)
            * [ssh](#ssh)
            * [ftp](#ftp)
         * [依赖安装](#依赖安装)
      * [Yolov3环境搭建](#yolov3环境搭建)
         * [Cloning and Building Darknet](#cloning-and-building-darknet)
         * [Download pretrained YOLOv3 weights](#download-pretrained-yolov3-weights)
            * [Run Detections with Darknet and YOLOv3](#run-detections-with-darknet-and-yolov3)

------

## 服务器环境搭建

> 工欲善其事，必先利其器

### 远程服务器

#### ssh

- macOS使用「终端」app进行连接

- iPadOS使用「Termius」app进行连接

  <img src="IDEA Lab实习笔记 7-23.assets/image-20200723100810888.png" alt="image-20200723100810888" width="50%;" />

#### ftp

使用「Cyberduck」app进行连接

<img src="IDEA Lab实习笔记 7-23.assets/截屏2020-07-23 10.10.09.png" alt="截屏2020-07-23 10.10.09" width="50%;" />

### 依赖安装

- git
- [opencv](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/doc/Study-Notes/ubuntu下配置opencv环境.md)



## Yolov3环境搭建

### Cloning and Building Darknet

```bash
# clone darknet repo
git clone https://github.com/AlexeyAB/darknet
cd darknet/

# change makefile to have GPU and OPENCV enabled
sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile

make
```

### Download pretrained YOLOv3 weights

YOLOv3 has been trained already on the coco dataset which has 80 classes that it can predict.

```bash
# get yolov3 pretrained coco dataset weights
wget https://pjreddie.com/media/files/yolov3.weights
```

#### Run Detections with Darknet and YOLOv3

```bash
# run darknet detection
!./darknet detect cfg/yolov3.cfg yolov3.weights data/person.jpg
```

<img src="IDEA Lab实习笔记 7-23.assets/image-20200723200009451.png" alt="image-20200723200009451" style="zoom:50%;" />

<img src="IDEA Lab实习笔记 7-23.assets/predictions-5504340.jpg" alt="predictions" style="zoom: 50%;" />