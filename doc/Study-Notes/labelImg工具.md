# labelImg工具的使用

Table of Contents
=================

   * [labelImg工具的使用](#labelimg工具的使用)
      * [安装步骤](#安装步骤)
      * [使用方法](#使用方法)

------

> https://github.com/tzutalin/labelImg

## 安装步骤

1. download from github [repo](https://github.com/tzutalin/labelImg)

2. install dependencies

   ```bash
   pip3 install pyqt5 lxml
   ```

3. build from resource

   - **mac**

     ```bash
     make qt5py3
     ```

   - **win10**

     ```bash
     pyqt5, pyrcc5 -o libs/resources.py resources.qrc
     ```

4. 准备`classes.txt`和`images/`

5. 运行qt工程

   ```bash
   python labelImg.py images/ classes.txt
   ```

   

## 使用方法

<img src="https://upload-images.jianshu.io/upload_images/12014150-12d977b736e482b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200725191912189" width="20%;" /><img src="https://upload-images.jianshu.io/upload_images/12014150-ae5d41844e57c10c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200725192001578" width=" 33%;" /><img src="https://upload-images.jianshu.io/upload_images/12014150-279de93f0ef27dcb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200725192129566" width="40%;" />

1. 切换存储格式为yolo
2. 创建区块
3. 拖拽区域进行标注并选择种类
4. 保存label到`.txt`文件

