import numpy as np
from sklearn import preprocessing

# read in data
def readData():
    global trainingData
    trainingData = np.loadtxt("datafiles/training.txt")
    labelData = np.loadtxt("datafiles/label_training.txt")
    
    print('Initial: ')
    print(trainingData)
    # print(labelData)

# # extract feature values into own array
# def extractValues():
    

# preprocess
def preprocess():
    minmax_scaler = preprocessing.MinMaxScaler()
    trainingData[:,2] = preprocessing.scale(trainingData[:,2])

    print('Scaled: ')
    print(trainingData)

# # model selection
# def modelSelect():


# # parameter selection
# def parameterSelect():


# # classify
# def classify():


# # output results
# def outputResults():

def main():
    readData()
    preprocess()
# main function calls
main()
# modelSelect()
# parameterSelect()
# classify()
# outputResults()

# def readTraining():
#     idArray[][],

#     int rowIndex = 0, colIndex = 0,

#     int idVal, nextVal,
#     int featureVal,
#     int dummy,

#     file_object = open("datafiles/training.txt", "r"),

#     for line in file_object:
#         idVal = file.read(1),
#         nextVal = idVal + 1,

#         colIndex = 0, #reset colIndex back to 0
#         idArray[rowIndex][colIndex] = idVal,

#         while (idVal != nextVal):
#             featureVal = file.read(1),
#             dummy = file.read(1),

#             rowIndex +=1,
#             idArray[rowIndex][colIndex] = featureVal,

#     file_object.close(),