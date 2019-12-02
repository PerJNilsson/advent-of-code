class TyrannyOfTheRocket:
      def __init__(self):
          self.fuelRequired = 0
          self.lowestMass = 2*3

      def calculateFuelCost(self, data):
            for value in data:
                  try:
                        value = int(value)
                        print(value)
                        if value >= self.lowestMass:
                              self.fuelRequired += int(value / 3) -2
                  except:
                        print("Not EOL char")
            return self.fuelRequired

      def recursiveFuelCost(self, data):
            for value in data:
                  value = int(value)
                  self.totr(value)
            return self.fuelRequired

      def totr(self, value):
            if value > self.lowestMass:
                  fuelCost = int(value/3) -2
                  self.fuelRequired += fuelCost
                  return self.totr(fuelCost)
            else:
                  return 0
