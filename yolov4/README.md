train

```bash
./darknet detector train ../../data/obj.data cfg/yolov4_custom.cfg yolov4.conv.137 -dont_show
```



test

```bash
./darknet detector test ../../data/obj.data cfg/yolov4_custom_test.cfg backup/yolov4_custom_last.weights ../../data/test.jpg -thresh 0.25 --dont-show
```

