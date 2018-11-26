arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
newArr = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

# newArr[0][0] = arr[3][0]
# newArr[0][1] = arr[2][0]
# newArr[0][2] = arr[1][0]
# newArr[0][3] = arr[0][0]

# newArr[1][0] = arr[3][1]
# newArr[1][1] = arr[2][1]
# newArr[1][2] = arr[1][1]
# newArr[1][3] = arr[0][1]

# newArr[2][0] = arr[3][2]
# newArr[2][1] = arr[2][2]
# newArr[2][2] = arr[1][2]
# newArr[2][3] = arr[0][2]

# newArr[3][0] = arr[3][3]
# newArr[3][1] = arr[2][3]
# newArr[3][2] = arr[1][3]
# newArr[3][3] = arr[0][3]

# for i,j in zip(range(0,4,1), range(3,-1,-1)) :
#     newArr[0][i] = arr[j][0]

# for i,j in zip(range(0,4,1), range(3,-1,-1)) :
#     newArr[1][i] = arr[j][1]

# for i,j in zip(range(0,4,1), range(3,-1,-1)) :
#     newArr[2][i] = arr[j][2]

# for i,j in zip(range(0,4,1), range(3,-1,-1)) :
#     newArr[3][i] = arr[j][3]

for k in range(0, 4, 1) :
    for i,j in zip(range(0,4,1), range(3,-1,-1)) :
        newArr[k][i] = arr[j][k]

output = ''

# output += str(newArr[0][0]) + ' '
# output += str(newArr[0][1]) + ' '
# output += str(newArr[0][2]) + ' '
# output += str(newArr[0][3]) + ' '
# output += '\n'
# output += str(newArr[1][0]) + ' '
# output += str(newArr[1][1]) + ' '
# output += str(newArr[1][2]) + ' '
# output += str(newArr[1][3]) + ' '
# output += '\n'

# for i in range(4) :
#     output += str(newArr[0][i]) + ' '
# output += '\n'
# for i in range(4) :
#     output += str(newArr[1][i]) + ' '
# output += '\n'
# for i in range(4) :
#     output += str(newArr[2][i]) + ' '
# output += '\n'
# for i in range(4) :
#     output += str(newArr[3][i]) + ' '
# output += '\n'

arr = newArr 

for i in range(4) :
    for j in range(4) :
        output += str(arr[i][j]) + ' '
    output += '\n'

print(output)



