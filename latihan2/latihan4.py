def sort(theList, fn) :
   for i in range(len(theList)) :
       for j in range(i+1, len(theList)) :
           check = fn(theList[i], theList[j]);
           if(check > 0) :
               temp = theList[i];
               theList[i] = theList[j];
               theList[j] = temp;

def minMax(theList):
    min = theList[0];
    max = theList[0];
    for i in range(1, len(theList)) :
        if(min > theList[i]) :
            min = theList[i];
        if(max < theList[i]) :
            max = theList[i];

    return [min,max];


x = [40, 100, 1, 5, 25, 10];

# def test(a,b) :
#     return b-a;

test = lambda a,b: b-a;
print(test(5,8));

sort(x, lambda a,b: a-b);
print(x);
# sort(x, test);
sort(x, lambda a,b: b-a);
print(x);

theMinAndMax = minMax(x);
print("Min : " + str(theMinAndMax[0]));
print("Max : " + str(theMinAndMax[1]));


