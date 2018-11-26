inputUser = input('Masukkan angka : ')

arr = inputUser.split(' ')
# arr = ['1', '2', '3', '4', '5', '6', '7' '8', '8','8', '9', '0', '']
output = ''
dict1 = { '1': '   ', '2': ' _ ', '3': ' _ ' }
dict2 = { '1': '  |', '2': ' _|', '3': ' _|' }
dict3 = { '1': '  |', '2': '|_ ', '3': ' _|' }

for i in range(3) :
    if(i == 0) :
        for item in arr :
            if(item == '2' or item == '3' 
                or item == '5' or item == '6' 
                or item == '7' or item == '8' 
                or item == '9' or item == '0') :
                output += ' _ '
            else :
                output += '   '
    elif(i == 1) :
        for item in arr :
            if(item == '8' or item == '9' or item == '4') :
                output += '|_|'
            elif(item == '2' or item == '3') :
                output += ' _|'
            elif(item == '5' or item == '6') :
                output += '|_ '
            elif(item == '1' or item == '7' ) :
                output += '  |'
            else :
                output += '| |'
    elif(i == 2) :
        for item in arr :
            if(item == '8' or item == '0' or item == '6') :
                output += '|_|'
            elif(item == '5' or item == '3' or item == '9') :
                output += ' _|'
            elif(item == '2') :
                output += '|_ '
            else :
                output += '  |'
    output += '\n'

print(output)
        
