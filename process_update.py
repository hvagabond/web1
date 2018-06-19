#!C:\python\Anaconda3\envs\py36_32bit\python.exe


import cgitb
import cgi, os
cgitb.enable()

form = cgi.FieldStorage()
pageID = form['pageID'].value
title = form['title'].value
description = form['description'].value

with open('data/'+pageID, 'w') as f:
    f.write(description)
os.rename('./data/'+pageID, './data/'+title)

print("Location: index.py?id="+title) #Redirection Header
print()

# print("Content-Type: text/html; charset=utf-8")
# print()