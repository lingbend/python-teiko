


INPUT_FILE_NAME = "cell-count.csv"


class dataLine:

    # assumes line is a cleaned array
    def __init__(self, keys, line):
        self._data = {}
        for i, j in zip(keys, line):
            self._data[i] = j

    def __str__(self):
        selfStr = ""
        for i, j in self._data.items():
            selfStr += i + ": " + j + " | \n"
        return selfStr

        

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
    openFile = open(fileName, encoding="utf-8-sig")
    return openFile

def closeFile(file):
    file.close()

if __name__ == "__main__":
    dataFile = getFile()
    keys = getKeys(dataFile.readline())
    data = getData(dataFile, keys)
    # print(len(data))
    # for i in data:
    #     print(i)
    closeFile(dataFile)