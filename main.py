


INPUT_FILE_NAME = "cell-count.csv"
ENCODING_TYPE = "utf-8-sig"


class dataLine:

    # assumes line is a cleaned array
    def __init__(self, keys = [], line = []):
        self._data = {}
        for i, j in zip(keys, line):
            self._data[i] = j

    def __str__(self):
        selfStr = ""
        for i, j in self._data.items():
            selfStr += i + ": " + j + " | \n"
        return selfStr
    
    # Test Output
def getPercentages(data, keepKeys, addKeys, percentKeys):
    percentData = []
    newKeys = keepKeys.copy() + addKeys
    for dataChunk in data:
        total = 0
        sampleData = []
        for perKey in percentKeys:
            total += int(dataChunk._data[perKey])
            newDataLine = dataLine()
            for keepKey in keepKeys:
                newDataLine._data[keepKey] = dataChunk._data[keepKey]
            newDataLine._data[addKeys[0]] = 0
            newDataLine._data[addKeys[1]] = perKey
            newDataLine._data[addKeys[2]] = int(dataChunk._data[perKey])
            newDataLine._data[addKeys[3]] = 0
            sampleData.append(newDataLine)
        for line in sampleData:
            line._data[addKeys[0]] = total
            line._data[addKeys[3]] = line._data[addKeys[2]] / total
        percentData.extend(sampleData)
    return newKeys, percentData
            

        


    

# assumes data processed and sorted
def packToCSV(data, keys):

    outputLines = []
    outputLines.append(",".join(keys))
    for dataLine in data:
        dataValues = [str(value) for value in dataLine._data.values()]
        outputLines.append(",".join(dataValues))

    outputFile = open("__output__" + INPUT_FILE_NAME, "w", encoding=ENCODING_TYPE)
    outputFile.write("\n".join(outputLines))
    outputFile.close()


def getData(file, keys):
    data = []
    for rawLine in file:
        cleanLine = cleanRawLine(rawLine)
        packedData = dataLine(keys, cleanLine)
        data.append(packedData)
    return data

def cleanRawLine(rawLine):
    return [data.strip() for data in rawLine.split(",")]

def getKeys(rawLine):
    return cleanRawLine(rawLine)


def getFile(fileName = INPUT_FILE_NAME):
    openFile = open(fileName, encoding=ENCODING_TYPE)
    return openFile

def closeFile(file):
    file.close()

if __name__ == "__main__":
    dataFile = getFile()
    keys = getKeys(dataFile.readline())
    data = getData(dataFile, keys)
    newKeys, newData = getPercentages(data, ["sample"], ["total_count", "population", "count", "percentage"],
                                      ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"])
    packToCSV(newData, newKeys)
    # print(len(data))
    # for i in data:
    #     print(i)
    closeFile(dataFile)