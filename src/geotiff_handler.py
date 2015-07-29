from osgeo import gdal
from osgeo import osr
from numpy import array

def latLonToPixel(geotifAddr, latLonPairs):
    # Load the image dataset
    ds = gdal.Open(geotifAddr)
    # Get a geo-transform of the dataset
    gt = ds.GetGeoTransform()
    # Create a spatial reference object for the dataset
    srs = osr.SpatialReference()
    srs.ImportFromWkt(ds.GetProjection())
    # Set up the coordinate transformation object
    srsLatLong = srs.CloneGeogCS()
    ct = osr.CoordinateTransformation(srsLatLong,srs)
    # Go through all the point pairs and translate them to latitude/longitude pairings
    pixelPairs = []
    for point in latLonPairs:
        # Change the point locations into the GeoTransform space
        (point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
        # Translate the x and y coordinates into pixel values
        x = (point[1]-gt[0])/gt[1]
        y = (point[0]-gt[3])/gt[5]
        # Add the point to our return array
        pixelPairs.append([int(x),int(y)])
    return pixelPairs


# open geotif file and do image transform
# returns: gt (geometry transform), ct (coordinate transform)
def open_and_transform(geotif_fname):
    # Load the image dataset
    ds = gdal.Open(geotifAddr)
    # Get a geo-transform of the dataset
    gt = ds.GetGeoTransform()
    # Create a spatial reference object for the dataset
    srs = osr.SpatialReference()
    srs.ImportFromWkt(ds.GetProjection())
    # Set up the coordinate transformation object
    srsLatLong = srs.CloneGeogCS()
    # ct: coordinate transform
    ct = osr.CoordinateTransformation(srsLatLong,srs)
    return gt, ct

# take array of lat long pairs and return array of pixel pairs
def coordarray_to_pixelarray(latlon_pairs, gt, ct):
    pixel_pairs = []
    for point in latlon_pairs:
        pixel = coord_to_pixel(point, ct, gt)
        pixel_pairs.append(pixel)
    return pixel_pairs

# take array with coordinates and return array of pixel (x,y)
def coord_to_pixel(point, ct, gt):
        (point[1],point[0],holder) = ct.TransformPoint(point[1],point[0])
        # Translate the x and y coordinates into pixel values
        x = (point[1]-gt[0])/gt[1]
        y = (point[0]-gt[3])/gt[5]
        return [int(x), int(y)]
 

def geotiff_to_imagery(input_image):
    ds = gdal.Open(input_image)
    gt = ds.GetGeoTransform()
    srs = osr.SpatialReference()
    srsLatLong = srs.CloneGeogCS()
    cord_transform = osr.CoordinateTransformation(srsLatLong,srs)
    return cord_transform

image = 'LC80160412015172LGN00_B4.TIF'
lat_lon = array([[28.240435, -81.294046]])
ct = geotiff_to_imagery(image)
pixel_pairs = []
pixel_pairs = latlong_to_pixel(ct, lat_lon)
img = gdal.Open(image)
myarray = array(img.GetRasterBand(1).ReadAsArray())
for pixel_pair in pixel_pairs:
    print pixel_pair
    print myarray[pixel_pair[0]][pixel_pair[1]]
    print myarray[pixel_pair[1]][pixel_pair[0]]
