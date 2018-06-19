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
    <h2>{title}</h2>
    <p>
        <a href="https://html.spec.whatwg.org/" target="_blank" title="HTML5 specification">Hypertext Markup Language (HTML)</a> is the standard markup language for <strong>creating <u>web</u> pages</strong><br>
        and web applications.Web browsers receive HTML documents from a web server or from local storage and render them<br>
        into multimedia web pages. HTML describes the structure of a web page semantically and originally included<br>
        cues for the appearance of the document.
    </p>

    <p style="margin-bottom:50px"><img src=".\img\sky.jpg" width="30%"></p>

    <p style="margin-top:40px">{description}</p>
    <p>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?list=PLpR7arjC4MiSrHQ0jau4LzWTodEAkUANa"\
         frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </p>
</body>
</html>
""".format(title=pageID, description=description, list=listStr))