import os
from osgeo import gdal
import numpy as np

class stackGeoTIFF:

    def __init__(self, folder_path):
        self.folder_path = folder_path     
 
    def load_bands(self): 
        self.band1 = self.load_band(1)
        self.band2 = self.load_band(2)
        self.band3 = self.load_band(3)
        self.band4 = self.load_band(4)
        self.band5 = self.load_band(5)
        self.band6 = self.load_band(6)
        self.band7 = self.load_band(7)

    def get_pixel_stack(self, y, x):
        print "finding "+str(x)+" "+str(y)
        #initialize a 7x1 array, each correspond to the value of a band
        pixel_stack = np.zeros((7,1))
        pixel_stack[0] = self.band1[y][x]
        pixel_stack[1] = self.band2[y][x]
        pixel_stack[2] = self.band3[y][x]
        pixel_stack[3] = self.band4[y][x]
        pixel_stack[4] = self.band5[y][x]
        pixel_stack[5] = self.band6[y][x]
        pixel_stack[6] = self.band7[y][x]

        return pixel_stack

    #x_y_pairs is a n x 2 array
    def get_pixel_stacks(self, x_y_pairs):
        num_pairs = len(x_y_pairs)
        pixel_stack = []
        for x_y in x_y_pairs:
            pixel_stack.append(self.get_pixel_stack(x_y[1], x_y[0]))
        return pixel_stack
             
    def load_band(self, band_num):
        image_name = self.find_band(band_num)
        image_array = self.open_band(image_name)
        return image_array

    def open_band(self, image_name):
        print("printing "+image_name)
        image = gdal.Open(image_name)
        image_array = image.GetRasterBand(1).ReadAsArray()
        return image_array

    def find_band(self, band_num):
        files = os.listdir(self.folder_path)
        for f in files:
            band_num_file = self.get_bandnum(f)
            if str(band_num) == band_num_file:
                return self.folder_path+f

    def get_bandnum(self, filename):
        basename = os.path.splitext(filename)[0].split('_')[1]
        return basename[1]
