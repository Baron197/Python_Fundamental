#solve 1
# size = int(input("Masukkan size: "));
# z = "";

# for num in range(size):
#     for num1 in range(num, size):
#         z += " * ";
#     z += "\n";

# print(z);

#solve 2
# size = int(input("Masukkan size: "));
# z = "";

# for num in range(size):
#     for num1 in range(num, size):
#         z += " * ";
#     z += "\n";
# for num in range(size-1):
#     for num1 in range(0, num+2):
#         z += " * ";
#     z += "\n";

# print(z);

#solve 3
# size = int(input("Masukkan size: "));
# z = "";

# for num in range(size):
#     for num1 in range(0, size-1-num):
#         z += "   ";
#     for num2 in range(0, (num*2)+1):
#         z += " * ";
#     z += "\n";

# print(z);

#solve 4
# size = int(input("Masukkan size: "));
# z = "";

# for num in range(size):
#     for num1 in range(0, num):
#         z += "   ";
#     for num2 in range(0, (size*2)-(num*2)-1):
#         z += " * ";
#     z += "\n";

# print(z);

#solve 5
# size = int(input("Masukkan size: "));
# z = "";

# for num in range(size):
#     for num1 in range(0, size-1-num):
#         z += "   ";
#     for num2 in range(0, (num*2)+1):
#         z += " * ";
#     z += "\n";
# for num in range(1, size):
#     for num1 in range(0, num):
#         z += "   ";
#     for num2 in range(0, (size*2)-(num*2)-1):
#         z += " * ";
#     z += "\n";

# print(z);

#solve 6
# size = int(input("Masukkan size: "));
# z = "";

# for num in range(size):
#     for num1 in range(num, size):
#         z += " * ";
#     for num2 in range(0, (num*2)-1):
#         z += "   ";
#     for num3 in range(size, num, -1):
#         if(num3 == 1):
#             break;
#         z += " * ";
#     z += "\n";
# for num in range(size-1):
#     for num1 in range(0, num+2):
#         z += " * ";
#     for num2 in range(size*2-5, num*2, -1):
#         z += "   ";
#     for num3 in range(0, num+2):
#         if(num == size-2 and num3 == num+1):
#             break;
#         z += " * ";
#     z += "\n";

# print(z);
    


