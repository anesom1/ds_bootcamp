dict1 = {1: {"name": "Mike"},
         2: {"name": "John"}}
print(dict1[1]["name"])



D = dict([('first', 1), ('second', 2)])
D2 = dict([('second', 2), ('first', 1)])
print(D == D2)


sampleDict = dict([('first', 1), ('second', 2)])
print(sampleDict)




temp = dict1.get("age")
print(temp)


set1 = {10, 50}
set2 = {60, 70, 30, 40, 80, 20, 50}
print(set1.issubset(set2))



listOne = ['a', 'b', 'c', 'd']
listTwo = ['e', 'f', 'g']

newList = listOne + listTwo
print(newList)

listOne.extend(listTwo) ; newList = listOne
print(newList)



print(newList)

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

simpleList = [10, 20, 30, 40]
del simpleList[0:6]
print(simpleList)

simpleList = [10, 20, 30, 40, 50]
simpleList.append(60)
print(simpleList)
simpleList.append(60)
print(simpleList)


aList = ['PYnative', [4, 8, 12, 16]]
print(aList[0][1])
print(aList[1][3])


simpleList = [10, 20, 30, 40, 50]
simpleList.pop()
print(simpleList)
simpleList.pop(2)
print(simpleList)

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])