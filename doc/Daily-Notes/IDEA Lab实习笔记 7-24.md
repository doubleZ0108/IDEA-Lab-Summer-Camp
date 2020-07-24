# IDEA Lab实习笔记 7-23

[toc]

------

## Yolov3训练自定义数据集

In order to create a custom YOLOv3 detector we will need the following:

- Labeled Custom Dataset
- Custom .cfg file
- obj.data and obj.names files
- train.txt file (test.txt is optional here as well)

### pre-trained weights

Download pre-trained weights for the convolutional layers

This step downloads the weights for the convolutional layers of the YOLOv3 network. By using these weights it helps your custom object detector to be way more accurate and not have to train as long. You don't have to use these weights but trust me it will help your modle converge and be accurate way faster.

```bash
wget http://pjreddie.com/media/files/darknet53.conv.74
```



### data

#### labeled custom dataset

由于玩具还没到货，所以采用之前实验室的数据，通过大致观察原始数据，发现有部分图像比较奇怪，考虑在之后自己拍摄数据的时候进行避免。

编写了两个脚本用来清洗之前的图像和label

- find_classes.py: 用来找到之前的数据是对几类对象进行分类
- match_img_label.py: 一一匹配图像和label，并删除多余的数据

#### .cfg

- **train**: 

  - $classes= \text{待分类的类别数}$
  - $filters=(classes+5) \times 3$

  ```cfg
  [convolutional]
  size=1
  stride=1
  pad=1
  filters=27
  activation=linear
  
  
  [yolo]
  mask = 6,7,8
  anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
  classes=4
  num=9
  jitter=.3
  ignore_thresh = .7
  truth_thresh = 1
  random=1
  ```

- **test**

  - batch: 1
  - subdivisions: 1

  ```cfg
  [net]
  # Testing
  batch=1
  subdivisions=1
  ```

  

#### obj.data

包含待分类的种类数，训练集、验证集等

> 由于本次这是做模型测试，故指定train和valid为同一列表

```data
classes= 4
train  = data/train.txt
valid  = data/train.txt
names = data/obj.names
backup = backup
```



#### obj.names

待分类的四类对象的名称

```
sheep
giraffe
cloud
snow
```



#### train.txt

训练、验证用的对象列表，这里编写了一个脚本用于生成列表

- generate_train.py: 根据文件夹中的图像和txt数据生成训练列表



### Train训练

```bash
./darknet detector train data/obj.data cfg/yolov3_custom.cfg darknet53.conv.74 -dont_show
```


每100epoches会将weights写入`backup/`一次

> 从上次的权重开始训练
>
> ```bash
> ./darknet detector train data/obj.data cfg/yolov3_custom.cfg backup/yolov3_custom_last.weights darknet53.conv.74 -dont_show
> ```

<img src="IDEA Lab实习笔记 7-24.assets/image-20200724152444234.png" alt="image-20200724152444234" style="zoom:50%;" />

### Test测试


```bash
./darknet detector test data/obj.data cfg/yolov3_custom_test.cfg backup/yolov3_custom_last.weights test.jpg -thresh 0.25 --dont-show
```

大约1000epoches之后对比较规矩的照片来讲效果很好

<img src="IDEA Lab实习笔记 7-24.assets/predictions.jpg" alt="predictions" style="zoom:50%;" />