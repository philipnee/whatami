import get_wrs

class GeoCoordinatesToWorldwideReferenceSystem:

  def __init__(self):
    self.geoToWRSConverter = get_wrs.ConvertToWRS()

  def latLngToPathRow(self, lat, lng):
    return (self.geoToWRSConverter.get_wrs(lat, lng))[0]

  def latLngListToPathRowList(self, latLngList):
    return map(lambda latLng : self.latLngToPathRow(latLng[0], latLng[1]),
               latLngList)

  def getPathRowToLatLngListMapFromLatLngList(self, latLngList):
    pathRowList = self.latLngListToPathRowList(latLngList)
    pathRowToLatLngListMap = {}
    for pathRow in pathRowList:
      if (not (pathRow['path'] in pathRowToLatLngListMap)):
        pathRowToLatLngListMap[pathRow['path']] = {}
      pathRowToLatLngListMap[pathRow['path']][pathRow['row']] = []
    for i in range(len(pathRowList)):
      pathRowToLatLngListMap[pathRowList[i]['path']][pathRowList[i]['row']].append(latLngList[i])
    return pathRowToLatLngListMap
