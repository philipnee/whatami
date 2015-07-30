from stackGeoTIFF import stackGeoTIFF
import numpy as np

k = stackGeoTIFF('../data/')
k.load_bands()

xy_pairs = np.array([[4169,911],
             [4123,900],
             [4069,911]]) 

print k.get_pixel_stack(4169,911)
print k.get_pixel_stacks(xy_pairs)
