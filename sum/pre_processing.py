import os
import numpy as np
import operator
import sys
##This is your Project Root##
sys.path.append(r"../..")
from pushkin.definition import ROOT_DIR
# ROOT_DIR = os.path.abspath('..') #This is the father folder
# ROOT_DIR = os.path.abspath('.') #This is your current Work Root

class dataPreprocessing():
    def __init__(self,data):
        """
        :param data: data you read from original text,(index, @target, polarity, twitterSen)
        """
    def arrangeDic(data):
        """
        arrange data format, input as rawtext, (target,polarity,sentence,target,polarity,sentence...)
        :return:[[target1,polarity,sentence],[target2,polarity,sentence]...]
        """
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


    def joinData(*args):
        """
        :param args: on the baseline data from auhtuan, there have 6 datasets, need to combine together
        :return: [[target1,polarity,sentence],[target2,polarity,sentence]...] #from 6 datasets
        """
        allData = []
        for dataset in args:
            allData = allData + dataPreprocessing.arrangeDic(dataset)
        # print (allData)
        return allData

    def countNumber(data,N):
        """
        :description: there have *n targets and 3 polarity, so totally have 3*n group\
                    we choose the biggest data group to train model
        :param N: top N group you want
        :return: group, countNumber\
                top N groups
        """
        temTopic = []
        temTopicPolarity = []
        for index in data:
            try:
                temTopic.append(index[1])
                temTopicPolarity.append(index[1]+" "+index[2])
            except:
                continue

        countNumber = {}
        for item in set(temTopic):
            countNumber[item] = temTopic.count(item)
        # for item in set(temTopicPolarity):
        #     countNumber[item] = temTopicPolarity.count(item)

        sortedGroup = sorted(countNumber.items(), key=operator.itemgetter(1))
        ##top N groups with its target and number##
        print ("TopGroup",sortedGroup[-N:])

        ##topNGroupTwitter is the final dataset we use to train model##
        topicList = []
        topNGroupTwitter = []
        ##topicList: top N group's target list##
        for item in sortedGroup[-N:]:
            topicList.append(item[0])

        for item in data:
            try:
                if item[1] in topicList:
                    topNGroupTwitter.append(item)
            except:
                continue

        print (topNGroupTwitter)
        return topNGroupTwitter









if __name__ == "__main__":
    #open all rawData & combine together
    with open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016train-BD.txt", "r") as f1, \
            open(ROOT_DIR+"/data/Subtasks_BD/twitter-2015testBD.txt", "r") as f2, \
            open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016dev-BD.txt", "r") as f3, \
            open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016devtest-BD.txt", "r") as f4,\
            open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016test-BD.txt", "r") as f5,\
            open(ROOT_DIR+"/data/Subtasks_BD/twitter-2016train-BD.txt", "r") as f6:
        rawData1,rawData2,rawData3,rawData4,rawData5,rawData6 = f1.read(),f2.read(),f3.read(),f4.read(),f5.read(),f6.read()


    Data = dataPreprocessing.joinData(rawData1,rawData2,rawData3,rawData4,rawData5,rawData6)
    a = dataPreprocessing.joinData(rawData1,rawData2)
    dataPreprocessing.countNumber(a,7)




