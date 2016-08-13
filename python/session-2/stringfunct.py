string = "Hello World!"

#can extract individual characters using dereferencing (string[index])

#prints "H"
print string[0]

#prints "e"
print string[1]

#print string[2]

#Slicing


#of form foo[num1:num2] - extract all elements from and including num1, up to num2 (but not including element at num2)

#all of the below prints World
print string[-6:-1]
print string[6:-1]
print string[6:11]

#print everything before the space: prints Hello
print string[:5]

#print everything after the space: World!
print string[6:]


sentence = "I am a teapot!"

print sentence.split(" ")


#***LISTS***

myList = ["a word", 3, 3, 4.6, "end"]
print myList

print myList[0]

print myList[1:]

print myList + [5, 4, 5, 67]

myList.append([1, 2, 3, 4])

print myList


myList.remove('end')

print myList

print len(myList)


myList[1] = 'one'
print myList

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in nums:
    if ((i % 2) == 1):
        nums.remove(i)
print nums



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in nums:
    if ((i % 2) == 1):
        nums = nums[0:i-1] + nums[i+1:]
print nums




#***DICTIONARIES***

myDict = {'one':1, 'two':2, 'three':3, 'four':4}

print myDict['two']

myDict['five'] = 5

print myDict

for i in myDict:
    print myDict[i]

months = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}

print ('apr' in months)

#PRACTICE:

#Input: "A man a plan a canal Panama" -> {'A':1, 'a':2, 'man':1, 'plan':1, 'Panama':1, 'canal':1}

