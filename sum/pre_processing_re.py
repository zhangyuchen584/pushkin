import os
import numpy as np
import sys
#This is your Project Root
sys.path.append(r"../..")
from pushkin.definition import ROOT_DIR






with open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016train-BD.txt", "r") as f1, \
        open(ROOT_DIR+"/data/Subtasks_BD/twitter-2015testBD.txt", "r") as f2, \
        open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016dev-BD.txt", "r") as f3:
    rawData1,rawData2,rawData3 = f1.read(),f2.read(),f3.read()


def arrangeDic(data):
    temArray = []
    lineData = data.split("\n")
    for line in lineData:
        attrData = line.split("\t")
        for item in attrData:
            if item == '':
                attrData.remove('')
        temArray.append(attrData)
    # print (temArray)
    return temArray

arrangeDic(rawData1)

temArray = []
lineData = rawData1.split("\n")
for line in lineData:
    attrData = line.split("\t")
    temArray.append(attrData)

# print (temArray)

list = [['a','a','a'],['b','b','b'],['c','c','c'],['a','a','a'],['b','b','b'],['c','c','c'],['a','a','a'],['b','b','b'],['c','c','c']]
dic = {'a' : 4, 'b' : 3}
a = [('jurassic world', 89), ('ac/dc', 91), ('fleetwood mac', 92), ('bob marley', 92), ('magic mike xxl', 92), ('eric church', 93)]

for item in a :
    print (item[0])
    print (1)


# print (list)
# print (dic)

keyList = []
targetList = []
for key,value in dic.items():
    keyList.append(key)
for item in list:
    if item[1] in keyList:
        targetList.append(item)
# print ("target",targetList)