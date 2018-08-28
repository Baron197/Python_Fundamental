def mainMenu() :
    return input("\nMain Menu : \n 1. Lihat Full Dictionary \n 2. Isi Dictionary \n 3. Searching Dictionary \n 4. Keluar \n\n Pilih : ");

def lihatFullDictionary(theDictionary) :
    print("Full Dictionary : ");
    print("__________________________________________");
    print("|        Key         |       Value       |");
    print("|____________________|___________________|");
    for key in theDictionary :
        if(str(type(theDictionary[key])) == "<class 'str'>") :
            print("|        " + key + "        |        '" + theDictionary[key] + "'        |");
        elif(str(type(theDictionary[key])) == "<class 'int'>") :
            print("|        " + key + "         |       " + str(theDictionary[key]) + "        |");
        print("|____________________|___________________|");

def isiDictionary(theDictionary) :
    inputKey = input("Isi Key : ");
    inputJenis = input("Value input 1 untuk string, 2 untuk number? : ");
    if(inputJenis == "1") :
        inputValue = input("Valuenya : ");
        theDictionary[inputKey] = inputValue;
    elif(inputJenis == "2") :
        inputValue = int(input("Valuenya : "));
        theDictionary[inputKey] = inputValue;
    else :
        print("Bandel ya, balik ke main menu dulu gih merenung dulu sana");

def searchDictionary(theDictionary) :
    inputSearch = input("Key search : ");
    newDDictionary = {};
    for key in theDictionary :
        if(inputSearch.lower() in key.lower()) :
            newDDictionary[key] = theDictionary[key];

    lihatFullDictionary(newDDictionary);


newDictionary = {};
while True :
    check = mainMenu();
    if(check == "1") :
        lihatFullDictionary(newDictionary);
    elif(check == "2") :
        isiDictionary(newDictionary);
    elif(check == "3") :
        searchDictionary(newDictionary);
    elif(check == "4") :
        print("Sampai jupa cus! salam bertasbih!");
        break;


