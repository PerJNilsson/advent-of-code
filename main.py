from the_tyranny_of_the_rocket_equation import TyrannyOfTheRocket

if __name__ == '__main__':
    filename = "input.txt"
    inputData = open(filename, "r")
    data = inputData.readlines()

    totr = TyrannyOfTheRocket()
    fuelCost = totr.calculateFuelCost(data)   
    print("Fuel requiments = %d" % fuelCost)
