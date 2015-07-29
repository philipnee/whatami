import get_wrs

class GeoCoordinatesToWorldwideReferenceSystem:

  def __init__(self):
    self.geoToWRSConverter = get_wrs.ConvertToWRS()

  def latitudeLongitudeToPathRow(self, lat, lng):
    return (self.geoToWRSConverter.get_wrs(lat, lng))[0]

  def latitudeLongitudeListToPathRowList(self, latLngList):
    return map(lambda latLng : self.latitudeLongitudeToPathRow(latLng[0], latLng[1]),
               latLngList)

