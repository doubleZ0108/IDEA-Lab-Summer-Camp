train

```bash
./darknet detector train ../../data/obj.data cfg/yolov3_custom.cfg backup/yolov3_custom_last.weights darknet53.conv.74 -dont_show
```





test

```bash
./darknet detector test ../../data/obj.data cfg/yolov3_custom_test.cfg backup/yolov3_custom_last.weights ../../data/demo.jpg -thresh 0.25 -dont-show
```



test for video

```bash
./darknet detector demo ../../data/obj.data cfg/yolov3_custom.cfg backup/yolov3_custom_last.weights -thresh 0.5 -dont_show ../../data/demo.mp4 -i 0 -out_filename results.avi
```

