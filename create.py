#!C:\python\Anaconda3\envs\py36_32bit\python.exe

print("Content-Type: text/html; charset=utf-8")
print()
import cgitb
import cgi, os
cgitb.enable()
form = cgi.FieldStorage()

if 'id' in form:
    pageID = form["id"].value
    with open("./data/" + pageID) as f:
        description = f.read()

else:
    pageID = "Welcome"
    description = 'Hello, Welcome to My Page'
print(pageID)


listStr = ''
files = os.listdir("./data")
for file in files:
    listStr += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=file)



print("""
<!doctype html>
<html>
<head>
    <title>WEB1 - html</title>
    <meta charset="UTF8">
</head>

<body>
  <h1><a href="index.html">WEB</a></h1>
    <ol>
        {list}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <P><input type="submit"></p>
    </form>
</body>
</html>
""".format(title=pageID, description=description, list=listStr))