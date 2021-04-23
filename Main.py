from PIL import Image
from numpy import asarray
import numpy as np

class Convert:

    def __init__(self, name, new_h, new_w, save):
        # name is the path; new_h is the height of the converted picture
        # new_h and new_w should be smaller than the original picture
        # save is a boolean
        self.n = name
        self.h = new_h
        self.w = new_w
        self.save = save
        self.ori = self.load()  # a 2_d array
        # print(self.ori)
        self.converted = [[[20,20,20,20] for i in range(self.w)] for j in range(self.h)]
        self.converted = asarray(self.converted)
        # print(self.converted)
        self.convert()    # the result
        print(self.converted)
        self.output()

    def load(self):
        img = Image.open(self.n)
        img = img.convert("RGBA")
        self.ori_w = img.size[0]
        self.ori_h = img.size[1]
        return asarray(img)

    def convert(self):
        w_ratio = self.ori_w // self.w   # how many original pixels correspond to new pixel horizontally
        h_ratio = self.ori_h // self.h
        offset_w = w_ratio//2
        offset_h = h_ratio//2

        for i in range(self.h):
            for j in range(self.w):
                self.converted[i][j] = self.ori[i*h_ratio + offset_h][j*w_ratio + offset_w].copy()
                # convert to transparent if the color is very close to white; the range can be adjusted for different purposes
                if self.converted[i][j][0] > 237 and self.converted[i][j][1] > 237 and self.converted[i][j][2] > 237:
                    self.converted[i][j][3] = 0

    def output(self):
        im = Image.fromarray(np.uint8(self.converted))   # only accepts uint8 format
        im.show()
        if self.save:
            new_name = self.n[:3] + "_converted.png"
            im.save(new_name, "PNG")

path = "whatever.jpg"
test = Convert(path, 90, 130, True)



