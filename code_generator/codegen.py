import csv
import string
import threading
import time
import sys


class generator(object):
    def __init__(self):
        self.description = """This is the object that generates the codes, do not modify"""


def printAllKLength(set, k, targetFile, listNumber):
    n = len(set)
    printAllKLengthRec(set, "", n, k, targetFile, listNumber)


# The main recursive method
# to print all possible
# strings of length k

def printAllKLengthRec(set, prefix, n, k, targFile, listName):
    # Base case: k is 0,
    # print prefix
    if (k == 0):
        listName.append(prefix)
        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1, targFile, listName)


def logic(currentDigit):
    rollingK = currentDigit
    filename = "file" + str(currentDigit)
    listName = "list" + str(currentDigit)

    printAllKLength(set1, rollingK, filename, list[listName])

    print(list[listName])

    fileToPrint = open("f" + str(currentDigit) + ".txt", "w")
    for element in list[listName]:
        fileToPrint.write(element + "\n")
    fileToPrint.close()


def printToConsole(digitcount, digitCutoff):
    rollingdigits = digitcount
    for i in range(digitcount):
        if rollingdigits <= digitCutoff:
            print("Lists Created In Same Directory As Program")
            sys.exit("Program completed")
        else:
            print(rollingdigits, "Digits")
            rollingdigits -= 1
            logic(rollingdigits)


# Driver Code
if __name__ == "__main__":
    # Define Sets
    # set1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # set1 = ['A', 'B']
    set1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    inputDigits = 3

    totalDigits = inputDigits + 1
    minimumDigits = 3

    listNameLoopingDigits = inputDigits

    # Declare Dictionary
    list = {}

    # Test Define Lists Loop
    for i in range(inputDigits):
        listNameIncStr = "list" + str(listNameLoopingDigits)
        print(listNameIncStr)
        listNameLoopingDigits -= 1

    # Define List
    list22 = []
    list21 = []
    list20 = []
    list19 = []
    list18 = []
    list17 = []
    list16 = []
    list15 = []
    list14 = []
    list13 = []
    list12 = []
    list11 = []
    list10 = []
    list9 = []
    list8 = []
    list7 = []
    list6 = []
    list5 = []
    list4 = []
    list3 = []
    list2 = []
    list1 = []

    # Define Dictionary and add list
    list["list22"] = list22
    list["list21"] = list21
    list["list20"] = list20
    list["list19"] = list19
    list["list18"] = list18
    list["list17"] = list17
    list["list16"] = list16
    list["list15"] = list15
    list["list14"] = list14
    list["list13"] = list13
    list["list12"] = list12
    list["list11"] = list11
    list["list10"] = list10
    list["list9"] = list9
    list["list8"] = list8
    list["list7"] = list7
    list["list6"] = list6
    list["list5"] = list5
    list["list4"] = list4
    list["list3"] = list3
    list["list2"] = list2
    list["list1"] = list1

    printToConsole(totalDigits, minimumDigits)
