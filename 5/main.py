#from program_alarm import ProgramAlarm
class SWaCoA:
    def __init__(self, data, input):
        self.data = data
        self.lenData = len(data)
        self.params = []
        self.input = input
        
    def opcode(self, i):
        code = self.getInstructions()
        if code == 4:
            idx = self.getIdx(i+1)
            print(data[idx])
            return i + 2
        elif code == 3:
            dest = self.getIdx(i+1)
            self.data[dest] = self.input
            return i + 2
        elif code == 1:
            opt1 = self.getIdx(i+1)
            opt2 = self.getIdx(i+2)
            dest = self.getIdx(i+3)
            self.data[dest] = self.data[opt1] + self.data[opt2]
            return i + 4
        elif code == 2:    
            opt1 = self.getIdx(i+1)
            opt2 = self.getIdx(i+2)
            dest = self.getIdx(i+3)
            #print("op1=%d, opt2=%d, dest=%d" %(opt1, opt2, dest))
            self.data[dest] = self.data[opt1] * self.data[opt2]
            return i + 4
        elif code == 5:
            opt1 = self.getIdx(i+1)
            if self.data[opt1] != 0:
                opt2 = self.getIdx(i+2)
                return self.data[opt2]
            return i+3
        elif code == 6:
            opt1 = self.getIdx(i+1)
            if self.data[opt1] == 0:
                opt2 = self.getIdx(i+2)
                return self.data[opt2]
            return i+3
        elif code == 7:
            opt1 = self.getIdx(i+1)
            opt2 = self.getIdx(i+2)
            dest = self.getIdx(i+3)
            idx = self.data[dest]
            if self.data[opt1] < self.data[opt2]:
                self.data[dest] = 1
            else:
                self.data[dest] = 0
            if idx == i:
                return i
            else:
                return i + 4
        elif code == 8:
            opt1 = self.getIdx(i+1)
            opt2 = self.getIdx(i+2)
            dest = self.getIdx(i+3)
            idx = self.data[dest]
            if self.data[opt1] == self.data[opt2]:
                self.data[dest] = 1
            else:
                self.data[dest] = 0
            if idx == i:
                return i
            else:
                return i + 4
        elif code == 99:
            exit(0)
        else:
            print(code, i)
            raise ValueError("Not an instruction")
        
    def getIdx(self, j):
        mode = self.getInstructions()
        if mode == 1:
            idx = j
        if mode == 0:
            idx = self.data[j]
        return idx

    def getInstructions(self):
        if len(self.params) == 5:
            tmpParam = self.params.pop()
            tmpParam2 = self.params.pop()
            param = 10*tmpParam2 + tmpParam
        else:
            param = self.params.pop()
        return param
        
    def extractIntegers(self, number):
        integers = []
        while number >= 1:
            integers.append(int(number % 10))
            number = number / 10
        while len(integers) < 5:
            integers.append(0)
        self.params = integers[::-1]
        return self.params
    
    def runOpcode(self):
        i = 0
        while i < self.lenData:
            self.extractIntegers(self.data[i])
            i = self.opcode(i)

if __name__ == '__main__':
    filename = "input.txt"
    inputData = open(filename, "r")
    data = inputData.read()
    data = data.split(",")
    data = list(map(int, data))

    input = 5
    a = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    b = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    d = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
         1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
         999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    cls = SWaCoA(data, input)

    cls.runOpcode()
    
    #a = cls.extractIntegers(1002)
    #print(a)
