def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

#===================================================MAIN PROGRAM=========================================
file = open('data.txt')
file2 = open('newSortedData.txt', 'a')
lines = file.read().splitlines()

name = []
address = []
email = []
dob = []
salary = []

j = 0
for line in lines:
    name.append('')
    address.append('')
    email.append('')
    dob.append('')
    salary.append('')
    j+=1

i = 0
for line in lines:
    name[i] = line.split(',')[0]
    address[i] = line.split(',')[1]
    email[i] = line.split(',')[2]
    dob[i] = line.split(',')[3]
    salary[i] = line.split(',')[4]
    i+=1

print("How do you want to sort the data?. Based on:")
print("1: Name \n2: City \n3: Date of Birth \n4: Salary\n")
choice = int(input("Your choice: "))

if choice == 1:
    print("UNSORTED: ")
    for a, b, c, d, e in zip(name, address, email, dob, salary):
        print("{:30} {:30} {:40} {:20} {:10}".format(a, b, c, d, e))
    index_col = list(zip(name, range(len(name))))
    mergeSort(index_col)
    index = [k[1] for k in index_col]
    print()
    print("SORTED: ")
    for i in index:
        print("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
    file2.write("===================================================THIS IS THE SORTED DATA BASED ON NAME================================================\n")
    for i in index:
        file2.write("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
        file2.write("\n")

elif choice == 2:
    print("UNSORTED: ")
    for a, b, c, d, e in zip(name, address, email, dob, salary):
        print("{:30} {:30} {:40} {:20} {:10}".format(a, b, c, d, e))
    index_col = list(zip(address, range(len(address))))
    mergeSort(index_col)
    index = [k[1] for k in index_col]
    print()
    print("SORTED: ")
    for i in index:
        print("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
    file2.write("===================================================THIS IS THE SORTED DATA BASED ON ADDRESS================================================\n")
    for i in index:
        file2.write("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
        file2.write("\n")

elif choice == 3:
    print("UNSORTED: ")
    for a, b, c, d, e in zip(name, address, email, dob, salary):
        print("{:30} {:30} {:40} {:20} {:10}".format(a, b, c, d, e))
    index_col = list(zip(dob, range(len(dob))))
    mergeSort(index_col)
    index = [k[1] for k in index_col]
    print()
    print("SORTED: ")
    for i in index:
        print("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
    file2.write("=================================================THIS IS THE SORTED DATA BASED ON DATE OF BIRTH================================================\n")
    for i in index:
        file2.write("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
        file2.write("\n")

elif choice == 4:
    print("UNSORTED: ")
    for a, b, c, d, e in zip(name, address, email, dob, salary):
        print("{:30} {:30} {:40} {:20} {:10}".format(a, b, c, d, e))
    index_col = list(zip(salary, range(len(salary))))
    mergeSort(index_col)
    index = [k[1] for k in index_col]
    print()
    print("SORTED: ")
    for i in index:
        print("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
    file2.write("===================================================THIS IS THE SORTED DATA BASED ON SALARY================================================\n")
    for i in index:
        file2.write("{:30} {:30} {:40} {:20} {:10}".format(name[i], address[i], email[i], dob[i], salary[i]))
        file2.write("\n")

print("\nDo you want to clear the text file? -> 1: YES    2: NO")
clearFile = int(input("Your choice: "))
if clearFile == 1:
    open('newSortedData.txt', 'w').close()

file2.write('\n')
file.close()
file2.close()