import matplotlib.pyplot as plt
import copy

def getPath(data):
    pathCoordinateX = []
    pathCoordinateY = []
    tmpCoordX = 0
    tmpCoordY = 0
    for path in data:
        direction = path[0]
        steps = int(path[1:])+1

        if direction == 'R':
            for i in range(1, steps):
                tmpCoordX += 1
                pathCoordinateX.append(tmpCoordX)
                pathCoordinateY.append(tmpCoordY)
              
        if direction == 'L':
            for i in range(1, steps):
                tmpCoordX -= 1
                pathCoordinateX.append(tmpCoordX)
                pathCoordinateY.append(tmpCoordY)
                
        if direction == 'U':
            for i in range(1, steps):
                tmpCoordY += 1
                pathCoordinateX.append(tmpCoordX)
                pathCoordinateY.append(tmpCoordY)
                
        if direction == 'D':
            for i in range(1, steps):
                tmpCoordY -= 1
                pathCoordinateX.append(tmpCoordX)
                pathCoordinateY.append(tmpCoordY)
                
    return pathCoordinateX, pathCoordinateY

def findManhattanDistance(xData1, xData2, yData1, yData2):
    listManhattanDistance = []
    combinedStepDistance = []
    for ix1, x1 in enumerate(xData1,0):
        for ix2, x2 in enumerate(xData2,0):
            if (x1 == x2 and yData1[ix1] == yData2[ix2]):
                print(x1, x2, yData1[ix1], yData2[ix2])
                listManhattanDistance.append(abs(x1)+abs(yData1[ix1]))
                combinedStepDistance.append(ix1+ ix2+2) # +2 since we're starting at index 1
        print("%d runs out of %d" % (ix1, len(xData1)-1))
    return listManhattanDistance, combinedStepDistance

def runTestCase():
    a = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    b = ['U62','R66','U55','R34','D71','R55','D58','R83']

    x1, y1 = getPath(a)
    x2, y2 = getPath(b)

    mhd, csd = findManhattanDistance(x1,x2,y1,y2)
    print("Manhattan Distances", mhd)
    print("Shortest Manhattan distance =", min(mhd))
    print("Shortest combined distance=", min(csd))
    plt.scatter(x1, y1)
    plt.scatter(x2,y2)
    plt.show()
    
    

def main():

    filename = "input.txt"
    inputData = open(filename, "r")
    rawData = inputData.read()
  
    wirePaths = rawData.split('\n')

    wirePathOne = wirePaths[0]
    wirePathOne = wirePathOne.split(',')

    wirePathTwo = wirePaths[1]
    wirePathTwo = wirePathTwo.split(',')
    
    x1, y1 = getPath(wirePathOne)
    x2, y2 = getPath(wirePathTwo)

    mhd, csd = findManhattanDistance(x1,x2,y1,y2)
    print("Shortest Manhattan distance =", min(mhd))
    print("Shortest combined distance=", min(csd))
    #plt.scatter(x1, y1)
    #plt.scatter(x2,y2)
    #plt.show()
    #runTestCase()

if __name__ == '__main__':
    main()
