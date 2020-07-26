# IDEA Lab实习笔记 7-25

[toc]

------

## 数据集拍摄

四个玩具已经到货，而且这四个玩具材质比较相近，适合作为一组进行拍摄

- 拍摄设备：iPhone 11

- 辅助设备：DJI OSMO Mobile3

  <img src="IDEA Lab实习笔记 7-26.assets/image-20200726215156945.png" alt="image-20200726215156945" width="15%;" />

在拍摄的时候尽可能使的画面稳定，iso和曝光大致相同，且不同角度尽可能反映好玩具的不同侧面的样子，因此采用云台的自动跟踪模式进行焦点跟踪

<img src="IDEA Lab实习笔记 7-26.assets/IMG_3864.PNG" alt="IMG_3864" width=" 33%;" />

同时边拍照边倒入电脑看效果，并记录拍摄过程中的一些图片数量等信息，方便后期进行数据清洗

<img src="IDEA Lab实习笔记 7-26.assets/image-20200726215125678.png" alt="image-20200726215125678" width=" 15%;" />

由于并不想在真实环境中拍摄太多，因此只选取了两个场景

- 偏暖色调的沙发
- 偏冷色调的墙壁

这两个场景分别与长颈鹿、云与羊颜色相近，也进一步加强目标检测网络的能力

<img src="IDEA Lab实习笔记 7-26.assets/image-20200726215112598.png" alt="image-20200726215112598" width="33%;" />

最终筛除掉一些比较劣质的数据，共得到93张有效数据，数量并不是很多，这是因为想通过学习数据集扩充的方法减少人力劳动。

同时由于手机像素比较高，每张图片在4M左右，数据量过千之后会对服务器和训练造成不少的时间消耗，因此在处理之前首先进行预处理——图像压缩，压缩后的图像大概在500k左右，效果十分明显

- [图像压缩预处理](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/util/data_compression.py)

<br/>

## 数据集扩充

[数据集扩充](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/doc/Study-Notes/%E6%95%B0%E6%8D%AE%E9%9B%86%E6%89%A9%E5%85%85.md)

通过一整天的学习和调研，共使用了11种方法进行数据集的扩充

- 图像强度变换
  - 亮度变化： [lightness](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/lightness.py)
  - 对比度变化：[contrast](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/contrast.py)
- 图像滤波
  - 锐化：[sharpen](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/sharpen.py)
  - 高斯模糊：[blur](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/blur.py)
- 透视变换
  - 镜像翻转：[flip](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/flip.py)
  - 图像裁剪：[crop](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/crop.py)
  - 图像拉伸：[deform](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/deform.py)
  - 镜头畸变：[distortion](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/distortion.py)
- 注入噪声
  - 椒盐噪声：[noise](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/noise.py)
  - 渐晕：[vignetting](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/vignetting.py)
- 其他
  - 随机抠除：[cutout](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/data-augmentation/cutout.py)

> 同时我在进行数据集扩充的时候尽量模拟镜头在拍摄时造成的干扰，而不是一味的对图像进行“奇怪”的处理，尽可能大程度的加强数据集扩充的作用，避免之前同学产生的如下问题
>
> 随机裁剪带来很多奇怪的数据，对网络的训练会造成负面的影响
>
> <img src="IDEA Lab实习笔记 7-26.assets/2Rotatetf_0028.jpg" alt="2Rotatetf_0028" width="50%;" />
>
> <img src="IDEA Lab实习笔记 7-26.assets/2Rotatetf_0029.jpg" alt="2Rotatetf_0029" width="20%;" />
>
> <img src="IDEA Lab实习笔记 7-26.assets/2Rotatetf_0030.jpg" alt="2Rotatetf_0030" width="50%;" />
>
> <img src="IDEA Lab实习笔记 7-26.assets/2Rotatetf_0039.jpg" alt="2Rotatetf_0039" width="50%;" />

## 数据集标注

首先采用昨天搜集到的[labelImage](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/doc/Study-Notes/labelImg工具.md)工具标注拍到的93张图片，这些图片存放在`main/`目录下，为所有数据中最原始的未处理数据；之后手工标注`_crop`, `_deform`, `_distortion`处理过的数据集，因为这部分如果采用脚本自动生成的话效果会很差，不能达到train集的素质，因此采用手工标注；`_flip`处理过的数据可以通过脚本自动生成有逻辑的标注，其余图像处理也可以直接复制之前手工标注的`main/`中的数据

<br/>

## 数据集训练

最后将 <u>手工标注的拍摄数据</u> + <u>手工标注的处理数据</u> + <u>自动生成的处理数据</u> + <u>之前同学留下的数据</u> 四份数据进行训练，并且编写相应脚本进行一些预处理

- [划分训练集、验证集、测试集](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/util/divide_train_valid_test.py)
- [将数据按类别分类整理](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/util/move.py)
- [将数据按类别重命名](https://github.com/doubleZ0108/IDEA-Lab-Summer-Camp/blob/master/src/util/rename.py)

这些看似不值一提的util，不仅能简化烦冗的工作，更是能整理一份清晰的目录结构，让之后在此方面进行的其他工作变得容易

**文件命名方法**

`giraffe_10_sharpen.jpg`

- pos0：类别名（people, sheep, giraffe, cloud, two, three, four, etc.)
- pos1: 在此类别中的编号
- pos2: 经过何种图像处理方法