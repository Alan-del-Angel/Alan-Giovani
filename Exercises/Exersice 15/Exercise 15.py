#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#EXERCISE 15


from sys import argv                    #Use the library sys and import argv for implement arguments

name_archive, username = argv          #save the name of the archive and the name when your type in the console

text = open('Example.txt')               #Open the archive

print(f"Your text is {text}")         #Print the name
print(text.read())                    #And finally print the text

x = "> "

print(f"Type the name of the text again:")     #And print the text again
a = input("> ")

t_a =  open(a)

print(t_a.read())

