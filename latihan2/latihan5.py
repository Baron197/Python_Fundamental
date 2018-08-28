# d = ({ "key1" : [1, { "test1" : [0, True]}]}, 4);

# d[0]["key1"][1]["test1"][1] = False;
# print(d[0]["key1"][1]["test1"][1]);

# newList = [1, (3, "test2"), ("test1", 2), (3, "test2")];
# s = set(newList);

# print(s);
# newList1 = list(s);
# print(newList1);

# listNum = [{ "test1" : [5,2] }, { "test1" : [7,3] }, { "test1" : [9,7]}];
# # for i in range(len(listNum)) :
# #     listNum[i] *= 2;
# # print(listNum);
# def test(a,b) :
#     b = 5;
#     return { "test1" : [(a + b, 5, 9, 8)] };

# listNum = list(test(item["test1"][1], item["test1"][0]) for item in listNum);
# print(listNum);
# print(listNum[1]["test1"][0][2:][1]);
#[7,8,12]

# def times2(num, test = 2) :
#     #isi num{"test1" : [5,2] }
#     #isi test{"test1" : [5,2] }
#     return num + test;

# listNum = [{ "test1" : [5,2] }, { "test1" : [7,3] }, { "test1" : [9,7]}];
# listNum = [1,3,5,7,9];
# abc = [2, 4, 6, 8, 10];
# listNum = list(map(times2, abc, listNum));
# print(listNum);

# def genap(num) :
#     return num % 3 == 0;

# listNum = [1,2,3,4,5,6,7];
# listNum = list(filter(genap, listNum));
# print(listNum);
a = "test1";
b = 20
d = { "" + a + "": 5, "" + str(b) + "": 9, "maruk": [7,8]};

for item in d :
    print(item);
for item in d :
    print(d[item]);
print("| key | Value |")
d["keren"] = 70;
print(d);
