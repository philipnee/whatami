import sys
import os
sys.path.append("/Library/Python/2.7/site-packages/Shapely-1.5.9-py2.7-macosx-10.10-intel.egg")

from GeoToWRS import GeoCoordinatesToWorldwideReferenceSystem
import geotiff_handler as gh
from osgeo import gdal
import numpy as np
from stackGeoTIFF import stackGeoTIFF
from calc_NDVI import CalcNDVI
from parse_metadata import ParseMetaData

def construct_directory_path(path, row):
    directory_path = "../data/"+str(path)+"/"+str(row)+"/"
    return directory_path

def get_xy_from_latlng(latlng_pairs, band_file):
    print band_file
    gt, ct = gh.open_and_transform(band_file)
    pixel_pairs = gh.coordarray_to_pixelarray(latlng_pairs, ct, gt)
    return pixel_pairs
   
def get_band_filename(directory_path):
    files = os.listdir(directory_path)
    return files[0]

def get_bands(xy_pairs, directory_path):
    k = stackGeoTIFF(directory_path)
    k.load_bands()
    return k.get_pixel_stacks(xy_pairs)

latLngList = [[27.486772, -81.459955],[27.397890, -81.296839],[27.425886, -81.173685],[27.364792, -81.398872],[27.361307, -81.413538]]
l = GeoCoordinatesToWorldwideReferenceSystem()
image_map = l.getPathRowToLatLngListMapFromLatLngList(latLngList)
print image_map

xy_pairs = []

for path in image_map.keys():
    value = image_map[path]
    for row in value.keys():
        directory_path = construct_directory_path(path, row)
        latlng_pairs = value[row]
        band_file = get_band_filename(directory_path)
        xy_pairs = get_xy_from_latlng(latlng_pairs, directory_path+band_file)
        xy_pairs_bands = get_bands(xy_pairs, directory_path)
        print band_file
        print xy_pairs_bands
        metadata = ParseMetaData(band_file.split('_')[0], directory_path)
        metadata.get_meta_filename()
        metadata.process_metadata()
        m_b4 = metadata.get_radiance_mult_band_4()
        m_b5 = metadata.get_radiance_mult_band_5()
        a_b4 = metadata.get_radiance_add_band_4()
        a_b5 = metadata.get_radiance_add_band_5()
        ndvi = CalcNDVI(m_b4, m_b5, a_b4, a_b5)
        band4And5Pairs = map(lambda allBands : [allBands[3], allBands[4]],
                             xy_pairs_bands)
        print band4And5Pairs
        print ndvi.computeNDVIList(band4And5Pairs)
