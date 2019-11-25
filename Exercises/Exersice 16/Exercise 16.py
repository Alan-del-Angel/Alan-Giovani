#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#EXERCISE 16

from sys import argv                    #First we use the library sys and import argv for implement arguments

name_archive, filename = argv          #save the name of the file and the name when your type in the console

print(f"We are going to erase {filename}")      #Make some scripts
print("\n")
print(f"If you don't want to see, hit A ")  #And select one of these options
print("\n")
print(f"If do you want to read, hit B ")

input("?")

print("Opening your file ...")  #Open the file
tar = open(filename, 'w')     #Select the file
print("The file is truncated")

tar.tell()  # Show the cursos
tar.seek(0, 0) #at the begining
tar.truncate()  #and finally truncate the archive (erase the content)


print("Now you are  to write 3 lines....")    #Type a phrase in 3 lines
line1 = input("line 1:  ")
line2 = input("line 2:  ")
line3 = input("line 3:  ")

print("Writing.....")                     #And finally print the archive
tar.write("\n")
tar.write(line1)
tar.write("\n")
tar.write(line2)
tar.write("\n")
tar.write(line3)
tar.write("\n")

print("Now see you file..... 7u7")

tar.close()                           #And close everywhere

