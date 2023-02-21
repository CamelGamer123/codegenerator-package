class Generator(object):
    def __init__(self):
        self.description = """This is the object that generates the codes, do not modify"""
        # Declare Dictionary
        self.list = {}

    def generate(self, length, list_of_strings, minimum_length=1, output_mode="List", file_out=False):
        """
        Main function.

        :parameter file_out:  If True, will output to a file.  If False, will output to console.
        :parameter length:  The maximum length of combinations to be generated.
        :parameter minimum_length:  The minimum length of combinations to be generated.
        :parameter list_of_strings:  A list of strings to be used to generate combinations.
        :parameter output_mode:  The output mode.  Can be "List" or "Set". Set is faster but is unordered.
        :return:
        """

        try:
            inputDigits = int(length)
        except ValueError:
            raise ValueError("Length must be an integer")

        try:
            minimumDigits = int(minimum_length)
        except ValueError:
            raise ValueError("Minimum Length must be an integer")

        totalDigits = inputDigits + 1

        listNameLoopingDigits = inputDigits

        # Test Define Lists Loop
        for i in range(inputDigits):
            listNameIncStr = "list" + str(listNameLoopingDigits)
            print(listNameIncStr)
            listNameLoopingDigits -= 1

        # Create All Lists
        self.createAllLists(totalDigits, minimumDigits)

        rollingdigits = inputDigits
        for i in range(inputDigits):
            if rollingdigits <= inputDigits:
                print("Lists Created In Same Directory As Program")
                exit("Program completed")
            else:
                print(rollingdigits, "Digits")
                rollingdigits -= 1
                rollingK = rollingdigits
                filename = "file" + str(rollingdigits)
                listName = "list" + str(rollingdigits)

                printAllKLength(list_of_strings, rollingK, filename, list[listName])

                print(list[listName])

                fileToPrint = open("f" + str(rollingdigits) + ".txt", "w")
                for element in self.list[listName]:
                    fileToPrint.write(element + "\n")
                fileToPrint.close()

    def createAllLists(self, highestDigit, lowestDigit):
        for i in range(highestDigit):
            if i >= lowestDigit:
                listName = "list" + str(i)
                self.list[listName] = []


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