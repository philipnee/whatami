#!/usr/bin/python

import geotiff_handler as gh
import numpy as np
from osgeo import gdal

def main():
    image = '../data/LC80160412015172LGN00_B4.TIF'
    lat_lon_pairs = np.array([[28.240435, -81.294046]])
    pixel_pairs = []
    gt, ct = gh.open_and_transform(image)
    pixel_pairs = gh.coordarray_to_pixelarray(lat_lon_pairs, ct, gt)
    img = gdal.Open(image)
    myarray = np.array(img.GetRasterBand(1).ReadAsArray())
    for pixel_pair in pixel_pairs:
        print pixel_pair
        print myarray[pixel_pair[0]][pixel_pair[1]]
        print myarray[pixel_pair[1]][pixel_pair[0]]


if __name__ == "__main__":
    main()
