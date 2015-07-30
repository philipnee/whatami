import os
import re

class ParseMetaData:
   
    def __init__(self, scene_name, path):
        self.scene = scene_name
        self.path = path

    def get_meta_filename(self):
        self.filename = self.path + self.scene + "_MTL.txt"

    def process_metadata(self):
        metadata_map = {}
        with open(self.filename) as f:
            metadata_map = self.get_metadata_map(f)
        return metadata_map

    def get_metadata_map(self, f):
        metadata_map = {}
        for line in f:
            if line.find('RADIANCE_') >= 0:
              metadata = line.rstrip().split('=')
              key = metadata[0]
              value = float(metadata[1])
              metadata_map[key] = value
        return metadata_map
