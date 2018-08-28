# looping

hasil = 5;
i = 0;
while i < 50 :
    for j in range(5,8) :
        for k in range(4,4) :
            hasil -= 1;
        for l in range(6,4,-2) :
            hasil += j;
    for m in range(8, 9, 2) :
        hasil += m; 
    i += 25;

print(hasil);
#57

# soal 2

hasil = 2;
list1 = [4, 2, 24, 87, 91, 8];
check = True;
num = 5;

while check :
    for i in range(9,4,-2) :
        for j in range(3, i+1, 2) :
            if(j == i) :
                hasil += num;
                num += 2;
        for k in range(i, num, -1) :
            if(k == 6 or k == 7) :
                hasil += list1[num - i];
    if(hasil > 85) :
        check = False;

print(hasil);

#119