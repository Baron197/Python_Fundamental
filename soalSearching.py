listData = ["Merdeka", "Hello", "Hellos", "Sohib", "Kari ayam"];
print(listData);
inputUser = input("Search : ");

def searchList(keyWord, theList) :
    newList = list(filter(lambda item: keyWord.lower() in item.lower(), theList));
    return newList;

searchedList = searchList(inputUser, listData);
print(searchedList);
