#!C:\Python27\python.exe
print ("Content-type: text/html\n\n");
import cgi
form = cgi.FieldStorage()
ScouterInitials = form.getvalue("sname")
print (ScouterInitials)