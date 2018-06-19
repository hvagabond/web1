#!C:\python\Anaconda3\envs\py36_32bit\python.exe


import cgitb
import cgi
cgitb.enable()

form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value


with open('data/'+title, 'w') as f:
    f.write(description)

print("Location: index.py?id="+title) #Redirection Header
print()

# print("Content-Type: text/html; charset=utf-8")
# print()