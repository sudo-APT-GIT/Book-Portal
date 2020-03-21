#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi, sqlite3,math
book_id="b7"
email="paishreya1412@gmail.com"
print ('Content-type:text/html\r\n\r\n')
print('''
	<html>
<head>
  <title>try</title>
  <link rel="stylesheet" type="text/css" href="/yass.css">
  <script src="https://kit.fontawesome.com/9743c13cfa.js"></script>
<link href="https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap" rel="stylesheet">
  <style type="text/css">
    p{
      font-family: 'Roboto Mono', monospace;
    }
  </style>
</head>
<body>
<div id="form-main">
  <div id="form-div">
    <form class="form" id="form1" method="get" action="mailyo.py">
      ''')
conn=sqlite3.connect('book_portal_proj.db')
cursor=conn.execute("SELECT email from customer where cust_id='c4'")

book_name=""
price=""
for row in cursor:
	email=row[0]
cursor=conn.execute("SELECT book_name,price from book_table where book_id='b7'")
for row in cursor:
	book_name=row[0]
	price=row[1]
conn.close()
print('''
      <p>
        EMAIL ID:"%s"
      </p>
      
      <p class="text">
        <p>ADDRESS:</p>
        <textarea name="text" class="validate[required,length[6,300]] feedback-input" id="comment" placeholder="Address"></textarea>
      </p>
      
      <p>
        BOOK TITLE:"%s"
        <br><br>
        <img src="/imgret/oliver twist.jpeg">
      </p>
     <p>Price = &#x20b9;"%s" </p>
     
      <div class="submit">
        <input type="submit" value="CONFIRM" id="button-blue"/>
        <div class="ease"></div>
      </div>
    </form>
  </div>
	'''%(email,book_name,price))

print (' <br>')
print ('<script type="text/javascript">')
print ('  document.querySelector(".img__btn").addEventListener("click", function() {')
print (' document.querySelector(".cont").classList.toggle("s--signup");')
print ('});')
print ('</script>')
print ('<script type="text/javascript">')

print ('  function myfunction(){')

print ('   document.getElementById("load1").style.display="none";')

print (' }')
print (' function loading(){')

print ('    document.getElementById("load1").style.display="block";')

print ('}')

print ('</script>')
print ('</body>')
print ('</html>')
