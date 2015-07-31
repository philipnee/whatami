class CalcNDVI:

  def __init__(self,
               multiplicativeRescalingFactor_Band4,
               multiplicativeRescalingFactor_Band5,
               additiveRescalingFactor_Band4,
               additiveRescalingFactor_Band5):
    self.multiplicativeRescalingFactor_Band4 = multiplicativeRescalingFactor_Band4
    self.multiplicativeRescalingFactor_Band5 = multiplicativeRescalingFactor_Band5
    self.additiveRescalingFactor_Band4 = additiveRescalingFactor_Band4
    self.additiveRescalingFactor_Band5 = additiveRescalingFactor_Band5

  def computeNDVI(self, band4Value, band5Value):
    toaRadiance_Band4 = band4Value * self.multiplicativeRescalingFactor_Band4 + \
                        self.additiveRescalingFactor_Band4
    toaRadiance_Band5 = band5Value * self.multiplicativeRescalingFactor_Band5 + \
                        self.additiveRescalingFactor_Band5
    return (toaRadiance_Band5 - toaRadiance_Band4) / \
           (toaRadiance_Band5 + toaRadiance_Band4)

  def computeNDVIList(self, band4And5ValuePairs):
    return map(lambda band4And5 : self.computeNDVI(band4And5[0], band4And5[1]),
               band4And5ValuePairs)
