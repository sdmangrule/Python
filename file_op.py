
f = open("sachin.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)
print("Using try: ")
try:
    file = open("sachin.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()

with open("sachin.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

### Read opreation
try:
    with open("sachin.txt", 'r') as f:
        content = f.read()
        print(content)
finally:
    f.close()

#### File operations write and read line by line using loop
L = ["Geeks\n", "for\n", "Geeks\n"]

file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

file1 = open('myfile.txt', 'r')
count = 0

print("Using for loop")
for line in file1:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

file1.close()

## File operations write and read line by line using list comprehension

with open('myfile.txt') as f:
    l = [line for line in f]

print(l)

with open('myfile.txt') as f:
    l = [line.rstrip() for line in f]

print(l)

## File operations write and read line by line using writelines and readlines

L = ["Geeks\n", "for\n", "Geeks\n"]

file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

file1 = open('myfile.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

### file op using with and writelines and readlines 

L = ["Geeks\n", "for\n", "Geeks\n"]

with open("myfile.txt", "w") as fp:
    fp.writelines(L)

count = 0
print("Using readlines()")

with open("myfile.txt") as fp:
    l = fp.readlines()
    for line in l:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

count = 0
print("\nUsing readline()")

with open("myfile.txt") as fp:
    while True:
        count += 1
        line = fp.readline()

        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))

count = 0
print("\nUsing for loop")

with open("myfile.txt") as fp:
    for line in fp:
        count += 1
        print("Line{}: {}".format(count, line.strip()))