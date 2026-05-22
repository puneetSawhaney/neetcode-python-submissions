# file I/O

# files .txt, .docx, .log etc
# binary files: .mp4, .mov, .png, .jpeg etc

# f = open("filename", "mode")
# filename can be any text files , mode can read, write or append


#data = f.read()
#f.close()

# r+, => read and overwrite (ptr is at start)
# w+ , => read + overwrite (no truncate, if data gets deleted, then ptr doesn't matter)

#a+, => read + append (no truncate, ptr is at end)

##################################
# deleting a file
#################################
# we need to import module for deletion
# import os
# os.remove(filename)


#######################################
#Practice
#########################################

# create a new file "practice.txt" using python, add following data

'''
Hi everyone
we are learning file I/O
using python.
I like programming in .NET, python and Java.
'''
li = [" Hi everyone\n", "we are learning file I/O\n","using python.\n", "I like programming in .NET, python and Java.\n"]
# 1st way
with open("practice.txt", 'w') as f:
    for el in li:
        f.write(el)
 # 2nd way       
with open("practice.txt", 'w') as f:
    f.writelines(li)
        
        
# replace all occurence of python with java in above file

# open file in read mode
with open("practice.txt", 'r') as f:
    data = f.read()
    
data = data.replace("python", "java")
with open("practice.txt", 'w') as f:
    f.write(data)

# search if word "learning" exists in the file or not

with open("practice.txt", 'r') as f:
    data = f.read() 
    if (data.find("learning") != -1):
        print("found")
    else:
        print("not found")


# in which line learning word exists
data = True
line_count =1
with open("practice.txt", 'r') as f:
    while data:
        data = f.readline() 
        if ("learning" in data):
            print(line_count)
            break
        else:
            print("not found")
            
        line_count+=1
        
# from a file containing numbers, check how many are numbers

# practice.txt  = 1,34,667,78,22,99
with open("practice.txt", 'r') as f:
    data = f.read()


num_li = data.split(,)
count = 0
for num in num_li:
    n = int(num)
    if n%2 == 0:
        count+=1
    
print(count)
