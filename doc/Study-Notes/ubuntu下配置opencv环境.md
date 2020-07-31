# Ubuntu下配置opencv环境

* [安装准备](#安装准备)
   * [安装cmake](#安装cmake)
   * [安装依赖环境](#安装依赖环境)
   * [下载opencv](#下载opencv)
* [安装](#安装)
   * [解压](#解压)
   * [cmake](#cmake)
   * [编译](#编译)
   * [安装](#安装-1)
* [配置环境](#配置环境)
* [检验](#检验)

------

- **操作系统**：Ubuntu18.04.4
- **版本**：opencv3.2.0

> 【**reference**】
>
> https://zhuanlan.zhihu.com/p/76737748
>
> https://blog.csdn.net/public669/article/details/99044895
>
> https://blog.csdn.net/weixin_41851439/article/details/88712465



## 安装准备

### 安装cmake

```bash
sudo apt-get install cmake
```



### 安装依赖环境

```bash
sudo apt install  build-essential
 
sudo apt install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev  
 
sudo apt install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

>  第三行中，可能会出现 无法定位软件包libjasper-dev 的错误提示
>
> ```bash
> sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
> sudo apt update
> sudo apt upgrade
> sudo apt install libjasper1 libjasper-dev
> ```



### 下载opencv

https://opencv.org/releases/



## 安装

### 解压

在opencv3文件夹下新建build文件夹



### cmake

进入`build/`

```bash
sudo cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
```

> 【由于网络问题无法下载`ippicv_linux_20151201.tgz`文件的解决办法】
>
> <img src="https://upload-images.jianshu.io/upload_images/12014150-dfd32d11133dd2a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image-20200723135727301" style="zoom:50%;" />
>
> 1. 找到`3rdparty/ippicv/downloader.cmake`文件
>
> ```cmake
> set(OPENCV_ICV_URL "https://raw.githubusercontent.com/opencv/opencv_3rdparty/${IPPICV_BINARIES_COMMIT}/ippicv")
> set(IPPICV_BINARIES_COMMIT "81a676001ca8075ada498583e4166079e5744668")
> ```
>
> 	2. 通过这两个语句拼接得到下载地址：https://raw.githubusercontent.com/opencv/opencv_3rdparty/81a676001ca8075ada498583e4166079e5744668/ippicv/ippicv_linux_20151201.tgz
>  	3. 将下载好的文件上传到服务器
>  	4. 替换路径为`"file:///root`



> 【The following variables are used in this project, but they are set to NOTFOUND.解决方案】
>
> >  cuda9不再支持2.0架构
>
> 1.在/home/mario/Projects/opencv-3.1.0/cmake下找到FindCUDA.cmake文件
>
> ​	1. 找到行：
>
> ```cmake
> find_cuda_helper_libs(nppi)
> ```
>
> 然后替换为：
>
> ```cmake
> find_cuda_helper_libs(nppial)
> find_cuda_helper_libs(nppicc)
> find_cuda_helper_libs(nppicom)
> find_cuda_helper_libs(nppidei)
> find_cuda_helper_libs(nppif)
> find_cuda_helper_libs(nppig)
> find_cuda_helper_libs(nppim)
> find_cuda_helper_libs(nppist)
> find_cuda_helper_libs(nppisu)
> find_cuda_helper_libs(nppitc)
> ```
>
> ​	2. 找到行：
>
> ```cmake
> set(CUDA_npp_LIBRARY "${CUDA_nppc_LIBRARY};${CUDA_nppi_LIBRARY};${CUDA_npps_LIBRARY}")
> ```
>
> 然后替换为：**（注意后面的"\"，实际输入的时候把这个反斜杠去掉，弄成一行，这里只是作为显示换行加的"\"）**
>
> ```cmake
> set(CUDA_npp_LIBRARY "${CUDA_nppc_LIBRARY};${CUDA_nppial_LIBRARY};${CUDA_nppicc_LIBRARY};\
> ${CUDA_nppicom_LIBRARY};${CUDA_nppidei_LIBRARY};${CUDA_nppif_LIBRARY};${CUDA_nppig_LIBRARY};\
> ${CUDA_nppim_LIBRARY};${CUDA_nppist_LIBRARY};${CUDA_nppisu_LIBRARY};${CUDA_nppitc_LIBRARY};${CUDA_npps_LIBRARY}")
> ```
>
> ​	3. 找到行：
>
> ```cmake
> unset(CUDA_nppi_LIBRARY CACHE)
> ```
>
> 然后替换为：
>
> ```cmake
> unset(CUDA_nppial_LIBRARY CACHE)
> unset(CUDA_nppicc_LIBRARY CACHE)
> unset(CUDA_nppicom_LIBRARY CACHE)
> unset(CUDA_nppidei_LIBRARY CACHE)
> unset(CUDA_nppif_LIBRARY CACHE)
> unset(CUDA_nppig_LIBRARY CACHE)
> unset(CUDA_nppim_LIBRARY CACHE)
> unset(CUDA_nppist_LIBRARY CACHE)
> unset(CUDA_nppisu_LIBRARY CACHE)
> unset(CUDA_nppitc_LIBRARY CACHE)
> ```
>
> 2. 在/home/mario/Projects/opencv-3.1.0/cmake下找到OpenCVDetectCUDA.cmake文件
>
> 找到以下几行：
>
> ```cmake
>  ...
>   set(__cuda_arch_ptx "")
>   if(CUDA_GENERATION STREQUAL "Fermi")
>     set(__cuda_arch_bin "2.0")
>   elseif(CUDA_GENERATION STREQUAL "Kepler")
>     set(__cuda_arch_bin "3.0 3.5 3.7")
>   ...
> ```
>
> 修改为：
>
> ```cmake
>   ...
>   set(__cuda_arch_ptx "")
>   if(CUDA_GENERATION STREQUAL "Kepler")
>     set(__cuda_arch_bin "3.0 3.5 3.7")
>   elseif(CUDA_GENERATION STREQUAL "Maxwell")
>     set(__cuda_arch_bin "5.0 5.2")
>   ...
> ```
>
> 3. 找到cudafp16.h的头文件`/usr/local/cuda-9.0/include/cudafp16.h`，将这个文件拷贝到opencv目录的cudev下`opencv-3.2.0/modules/cudev/include/opencv2/cudev`，然后在该目录下的`common.hpp`的文件添加:
>
> ```cpp
> #include <cuda_fp16.h>
> ```

### 编译

> 【Unsupported gpu architecture 'compute_20'解决方案】
>
> ```bash
> cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D CUDA_GENERATION=Kepler ..
> ```
>
> hint: 添加Kepler

### 安装

```bash
sudo make install
```



## 配置环境

打开`/etc/ld.so.conf`在文件中加上一行 

```conf
include /usr/loacal/lib
```

```bash
sudo ldconfig
```

打开`/etc/bash.bashrc `，在文件中添加

```bash
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH
```

```bash
source /etc/bash.bashrc
```

## 检验

```bash
pkg-config opencv --modversion
```

> Package opencv was not found in the pkg-config search path.解决方案
>
> 创建`opencv.pc`文件
>
> ```bash
> cd /usr/local/lib
> sudo mkdir pkgconfig
> cd pkgconfig
> sudo touch opencv.pc
> ```
>
> 添加如下信息
>
> ```bash
> prefix=/usr/local
> exec_prefix=${prefix}
> includedir=${prefix}/include
> libdir=${exec_prefix}/lib
> 
> Name: opencv
> Description: The opencv library
> Version:4.0.1
> Cflags: -I${includedir}/opencv4
> Libs: -L${libdir} -lopencv_shape -lopencv_stitching -lopencv_objdetect -lopencv_superres -lopencv_videostab -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_video -lopencv_photo -lopencv_ml -lopencv_imgproc -lopencv_flann  -lopencv_core
> ~
> ```
>
> 将文件导出到环境变量
>
> ```bash
> export  PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
> ```