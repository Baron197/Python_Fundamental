x = [ 1,2,3,2,5,2,7,2 ]
def getMode(list) :
    countList = [];
    # create countList
    for num in list :
        check = False;
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1;
                check = True;
                break;
        if(check == False) :
            countList.append([num, 0]);
    # create list of mode/s
    maxFrequency = 0;
    modes = [];
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modes = [list1[0]];
            maxFrequency = list1[1];
        elif (list1[1] == maxFrequency) :
            modes.append(list1[0]);
    # if every value appears same amount of times
    if (len(modes) == len(countList)) :
        modes = [];
    return modes;
print(getMode(x));
