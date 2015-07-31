import os
import re

class ParseMetaData:
   
    def __init__(self, scene_name, path):
        self.scene = scene_name
        self.path = path
        self.metadata_map = {}

    def get_meta_filename(self):
        self.filename = self.path + self.scene + "_MTL.txt"

    def process_metadata(self):
        with open(self.filename) as f:
            self.load_metadata_map(f)

    def load_metadata_map(self, f):
        for line in f:
            if line.find('RADIANCE_') >= 0:
              metadata = line.split('=')
              key = metadata[0].strip()
              value = float(metadata[1])
              self.metadata_map[key] = value

    def print_metadata(self):
        print self.metadata_map

    def get_radiance_add_band_4(self):
        return self.metadata_map['RADIANCE_ADD_BAND_4']

    def get_radiance_add_band_5(self):
        return self.metadata_map['RADIANCE_ADD_BAND_5']

    def get_radiance_mult_band_4(self):
        return self.metadata_map['RADIANCE_MULT_BAND_4']

    def get_radiance_mult_band_5(self):
        return self.metadata_map['RADIANCE_MULT_BAND_5']
