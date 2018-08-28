def mainMenu(theList) : 
    while True :
        munculkan(theList);
        inputArah = input('Mau diputar ke Kanan atau ke Kiri? : ');
        inputKali = input('Mau diputar berapa kali? : ');
        theList = putar(inputArah, int(inputKali), theList);
        inputBerhenti = input('Input 1 untuk keluar lain untuk lanjut : ');
        if(inputBerhenti == '1'):
            break;
    
def munculkan(theList) :
    outPut = '';
    for i in range(4) :
        outPut += '\n';
        for j in range(4) :
            outPut += (' ' + str(theList[i][j]));
    print(outPut);


def putar(arah, inputKali, arr) :
    kali = inputKali % 4;
    newArr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];

    if(kali == 0) :
        newArr = arr;

    elif((kali == 1 and arah == 'Kanan') or (kali == 3 and arah == 'Kiri')) :
        for i, k in zip(range(4), range(3,-1,-1)) :
            for j in range(4) :
                newArr[j][k] = arr[i][j];

    elif(kali == 2) :
        for i, k in zip(range(4), range(3,-1,-1)) :
            for j, l in zip(range(4), range(3,-1,-1)) :
                newArr[k][l] = arr[i][j];

    elif((kali == 3 and arah == 'Kanan') or (kali == 1 and arah == 'Kiri')) :
        for i in range(4) :
            for j, l in zip(range(4), range(3,-1,-1)) :
                newArr[l][i] = arr[i][j];

    arr = newArr;
    munculkan(arr);
    return arr;

list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];

mainMenu(list1);

testList = [0,1,2,3,4,5];

def test(theList) :
    newList = theList.copy();

    newList[1] = 5;
    return newList;

test(testList);
print(testList);


# list1 = [1,2,3,4,5,6,7];
# list2 = [];

# for index in range(len(list1)-1, -1, -1) :
#     list2.append(list1[index]);

# list2.append(list1[6]);
# list2.append(list1[5]);
# list2.append(list1[4]);
# list2.append(list1[0]);

# list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
# listHasil = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];

# listHasil[0][0] = list1[3][0];
# listHasil[0][1] = list1[2][0];
# listHasil[0][2] = list1[1][0];
# listHasil[0][3] = list1[0][0];

# for i,j in zip(range(4), range(3,-1,-1)) :
#     listHasil[0][i] = list1[j][0];

# listHasil[0][0] = list1[3][0];
# listHasil[0][1] = list1[2][0];
# listHasil[0][2] = list1[1][0];
# listHasil[0][3] = list1[0][0];

# listHasil[1][0] = list1[3][1];
# listHasil[1][1] = list1[2][1];
# listHasil[1][2] = list1[1][1];
# listHasil[1][3] = list1[0][1];

# for i in range(4) :
#     for j,k in zip(range(4), range(3,-1,-1)) :
#         listHasil[i][j] = list1[k][i];


