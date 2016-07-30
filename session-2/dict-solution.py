def get_sentence_count(line):
    splitLine = line.split(" ")
    dictOfLine = {}
    for i in splitLine:
        if ((i in dictOfLine) == True):
            dictOfLine[i] = dictOfLine[i] + 1
        else:
            dictOfLine[i] = 1
    return dictOfLine



print get_sentence_count("A man a plan a canal Panama!")