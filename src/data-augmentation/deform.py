

'''
图像拉伸
'''
def deform(img):
    w, h = image.size
    w = int(w)
    h = int(h)
    # 拉伸成宽为w的正方形
    out_ww = image.resize((int(w), int(w)))
    savename = self.get_savename(operate + '_ww')
    out_ww.save(savename, quality=100)
    # 拉伸成宽为h的正方形
    out_ww = image.resize((int(h), int(h)))
    savename = self.get_savename(operate + '_hh')
    out_ww.save(savename, quality=100)