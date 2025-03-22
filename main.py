


INPUT_FILE_NAME = "cell-count.csv"



def getKeys(rawLine):
    return [label.strip() for label in rawLine.split(",")]


def getFile(fileName = INPUT_FILE_NAME):
    openFile = open(fileName, encoding="utf-8-sig")
    return openFile

def closeFile(file):
    file.close()







if __name__ == "__main__":
    dataFile = getFile()
    print(getKeys(dataFile.readline()))
    closeFile