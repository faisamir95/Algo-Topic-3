file = open('data.txt')
lines = file.read().splitlines()
dict = {}

keyname = []
keyaddress = []
keyemail = []
keydob = []
keysalary = []
valuename = []
valueaddress = []
valueemail = []
valuedob = []
valuesalary = []


j = 0
for line in lines:
    keyname.append('name' + str(j))
    keyaddress.append('address' + str(j))
    keyemail.append('email' + str(j))
    keydob.append('dob' + str(j))
    keysalary.append('salary' + str(j))
    valuename.append('')
    valueaddress.append('')
    valueemail.append('')
    valuedob.append('')
    valuesalary.append('')
    j+=1

i = 0
for line in lines:
    valuename[i] = line.split(',')[0]
    valueaddress[i] = line.split(',')[1]
    valueemail[i] = line.split(',')[2]
    valuedob[i] = line.split(',')[3]
    valuesalary[i] = line.split(',')[4]
    dict[keyname[i]] = valuename[i]
    dict[keyaddress[i]] = valueaddress[i]
    dict[keyemail[i]] = valueemail[i]
    dict[keydob[i]] = valuedob[i]
    dict[keysalary[i]] = valuesalary[i]
    i+=1

file.close()
