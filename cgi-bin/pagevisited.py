#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi, cgitb
filew=open('times.txt','r')
string=filew.readline().strip()
num=int(string)
filew.close()
num=num+1
filew=open('times.txt','w')
filew.write(str(num))
filew.close()
strr=str(num)
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>PageVisited</title>")
print ("</head>")
print ("<body>")
print ("<h1> The page was opened %s times </h1>" % (strr))
print ("</body>")
print ("</html>")