import matplotlib.pyplot as mat
import numpy as np


INPUT_FILE_NAME = "cell-count.csv"
ENCODING_TYPE = "utf-8-sig"
CELL_TYPES = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]


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

def getTotal(dataLine):
    total = 0
    for key in CELL_TYPES:
        total += int(dataLine._data[key])
    return total

def filterByKeyPairs(data, pairs):
    filteredData = []
    dataSet = data.copy()
    for key, value in pairs.items():
        for dataLine in dataSet:
            if (dataLine._data.get(key) == value):
                filteredData.append(dataLine)
        dataSet = filteredData.copy()
        filteredData = []
    return dataSet

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

def getBoxPlotData(fields, data, processing=(lambda x, field : x)):
    dataSet = []
    for field in fields:
        dataSet.append([processing(point, field) for point in data])
    return dataSet

if __name__ == "__main__":
    dataFile = getFile()
    keys = getKeys(dataFile.readline())
    data = getData(dataFile, keys)
    newKeys, newData = getPercentages(data, ["sample"], ["total_count", "population", "count", "percentage"], CELL_TYPES)
    packToCSV(newData, newKeys)

    tr1Data = filterByKeyPairs(data, {"condition":"melanoma", "treatment":"tr1", "sample_type":"PBMC"})
    tr1ResponderData = filterByKeyPairs(tr1Data, {"response":"y"})
    tr1NonResponderData = filterByKeyPairs(tr1Data, {"response":"n"})

    processedResponderData = getBoxPlotData(CELL_TYPES, tr1ResponderData, (lambda point, field: int(point._data.get(field)) / getTotal(point)))
    processedNonResponderData = getBoxPlotData(CELL_TYPES, tr1NonResponderData, (lambda point, field: int(point._data.get(field)) / getTotal(point)))

    plotArrays = [None] * len(processedNonResponderData * 2)
    plotArrays[::2] = processedResponderData
    plotArrays[1::2] = processedNonResponderData

    mat.boxplot(plotArrays, tick_labels=["R b", "Non-R b", "R cd8 t", "Non-R cd8 t", "R cd4 t", "Non-R cd4 t", "R nk", "Non-R nk", "R monocyte", "Non-R monocyte"])
    mat.show()

    closeFile(dataFile)