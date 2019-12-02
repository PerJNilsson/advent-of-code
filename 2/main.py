from program_alarm import ProgramAlarm   

if __name__ == '__main__':
    filename = "input.txt"
    inputData = open(filename, "r")
    data = inputData.read()
    data = data.split(",")
    data = list(map(int, data))
    #data[1] = 53
    #data[2] = 98
    #pa = ProgramAlarm(data)
    #ouput = pa.runProgram()
    #print(100*53+98)

    idc = ProgramAlarm(data)
    for i in range(0, 99):
        for j in range(0,99):
            idc.findParameters(data, i, j)
            reset()
