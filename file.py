##################
# file handling in python
##################

# files by default get open in read mode, 2nd arg after path of file is mode only

f = open('somepath/data.txt', 'r') # here I gave r for read mode similarly w for write mode but by default if we don't give argument other than path file gets opened in read mode

print(f.readline()) # reads first line and if we use multiple times so it reads next lines

print(f.readline()) # next line
print(f.readline()) # 3rd
print(f.readline()) # 4th

# for loop to itterate over all the lines if there 10k or more lines you can't just do readline 10k times

for line in f: # we took f as file object
    print(line) # gets printed all the lines (no need to do readline here)
    
# let' say if some error occurs in between before f.close()
# file never gets closed and resources related to file never gets released.



f.close() # mandatory to close the file



# # file never gets closed and resources related to file never gets released.

# use of with

with open('somepath/data.txt') as f:
    for line in f:
        print(line)
        
# if any error get occur it will close the file

    print(f.read())  # to read complete file
    
    print(f.read(10)) # reads 10 chars
    print(f.read(10))  # next 10 chars
    
# with each read operation f keeps track of cursor so after 1st 10 char reading it will keep cursor at 10 and starts from there for next read

    f.seek(0) # to move cursor to specific positon
    # 0 will set to initial char, we can make it 20 and else
    
    
# write part of file handling

# we will open using w mode

with open('path/new_data.txt', 'w') as f:
    f.write('anything ') # this will bet printed inside new data txt file
    f.writelines(lines_data) # lines_data is some list of lines and here we used writelines for multiple lines writing


# append mode is there
# this helps us to preserve the earlier data
with open('path/new_data.txt', 'a') as f:
    f.write('anything ') # this will bet printed inside new data txt file
    f.writelines(lines_data)
# we can pass string, sequece list of string to write
    
