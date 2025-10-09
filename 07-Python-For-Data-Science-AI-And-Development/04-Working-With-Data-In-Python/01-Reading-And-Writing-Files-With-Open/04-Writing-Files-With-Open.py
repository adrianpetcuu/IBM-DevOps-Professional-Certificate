# Writing line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write('This is line A\n')
    writefile.write('This is line B\n')

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
print(Lines)

# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# mode to w overwrites all the existing data in the file
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Appending files
# Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write('This is line C\n')
    testwritefile.write('This is line D\n')
    testwritefile.write('This is line E\n')

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write('This is line E\n')
    print(testwritefile.read())

with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data): # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0) # move 0 bytes from beginning

    print("\nNew Location: {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print('Location after read: {}'.format(testwritefile.tell()))

with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 0) # write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0, 0)
    print(testwritefile.read())

with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 0) # write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    # Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())

# Copy the file to another
with open('Example2.txt', 'r') as readfile:
    with open('Example3.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

# Verify if the copy is successfully executed
with open('Example3.txt', 'r') as testwritefile:
    print(testwritefile.read())

#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)


def cleanFiles(currentMem, exMem):
    # Deschide currentMem în r+ (citire/scriere) și exMem în a+ (append)
    with open(currentMem, "r+") as cur, open(exMem, "a+") as ex:
        # Citește toate liniile din currentMem
        lines = cur.readlines()
        if not lines:
            return  # nimic de procesat

        header = lines[0]
        members = lines[1:]

        # Liste separate pentru activi / inactivi
        active_lines = []
        inactive_lines = []

        # Iterează membrii și separă după ultima coloană ("Active")
        for line in members:
            if not line.strip():
                continue  # sare peste linii goale, dacă există
            status = line.split()[-1]          # ultimul "cuvânt" din linie
            if status.lower() == "no":
                inactive_lines.append(line)    # mutăm în exMem
            else:
                active_lines.append(line)      # rămâne în currentMem

        # Scrie înapoi în currentMem doar activii (păstrând header-ul)
        cur.seek(0)
        cur.write(header)
        cur.writelines(active_lines)
        cur.truncate()  # taie restul vechiului conținut

        # Atașează în exMem pe inactivi (formatul inițial al fișierului este păstrat)
        ex.writelines(inactive_lines)


def testMsg(passed):
    if passed:
        return 'Test Passed'
    else:
        return 'Test Failed'


testWrite = "testWrite.txt"
testAppend = "testAppend.txt"
passed = True

genFiles(testWrite, testAppend)

with open(testWrite, 'r') as file:
    ogWrite = file.readlines()

with open(testAppend, 'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite, testAppend)
except:
    print('Error')

with open(testWrite, 'r') as file:
    clWrite = file.readlines()

with open(testAppend, 'r') as file:
    clAppend = file.readlines()

# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False

for line in clWrite:
    if 'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print("{}".format(testMsg(passed)))

