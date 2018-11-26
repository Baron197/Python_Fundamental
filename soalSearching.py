listData = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari ayam"]
print(listData)
inputUser = input("Search : ")

def searchList(keyWord, theList) :
    newList = list(filter(lambda item: keyWord.lower() in item.lower(), theList))
    return newList

searchedList = searchList(inputUser, listData)
print(searchedList)

# Map & Filter

def mapBertasbih(fn, theList) :
    newList = []
    for item in theList :
        newList.append(fn(item))
    
    return newList

def filterBertasbih(fn, theList) :
    newList = []
    for item in theList :
        if(fn(item)):
            newList.append(item)

    return newList

# listTest = [1,2,3,4,5]

# list1 = mapBertasbih(lambda item: item*2, listTest)
# list2 = filterBertasbih(lambda item: item % 2 == 0, listTest)

# print(list1)
# print(list2)
