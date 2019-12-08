class ProgramAlarm:
    def __init__(self, data):
        self.calcOutput = 0
        self.output = 19690720
        self.lenData = len(data)
        
    def opcode(self, i, data):
        code = data[i]
        if code == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            return i + 4
        elif code == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            return i + 4
        elif code == 99:
            self.calcOutput = data[0]
            return self.lenData
        else:
            return self.lenData

    def runProgram(self, data):
        i = 0
        while i < self.lenData:
            i = self.opcode(i, data)
        print("??", self.calcOutput)

    def findParameters(self, data, i, j):
        newData = data
        newData[1], newData[2] = i, j
        self.runProgram(data)
        print(self.calcOutput)
        if self.calcOutput == self.output:
            print("The puzzle answer is", 100*i+j)
