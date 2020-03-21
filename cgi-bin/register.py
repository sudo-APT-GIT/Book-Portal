#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi,cgitb,sqlite3
form=cgi.FieldStorage()
name=form.getvalue("namee")
email=form.getvalue("email")
pwd=form.getvalue("pwd")

fil=open("newfile.txt","r")
lin=fil.readlines()
fil.close()
y=lin[0].split('c')
x=y[1]
z=int(x)
z=z+1
id1='c'+str(z)
fil=open("newfile.txt","w")
fil.write(id1)
fil.close()

conn=sqlite3.connect("book_portal_proj.db")
statement='INSERT INTO customer VALUES (?,?,?,?)'
record=[(id1,name,email,pwd)]
cur=conn.cursor()
cur.executemany(statement,record)
conn.commit()
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/book-page.css">')
print('</head>')
print("""<body onload="myfunction()">
<div id="load1">
<div id="load">
<hr/><hr/><hr/><hr/>

</div>
<br>
<p>"It is our choices, Harry, that show what we truly are, far more than our abilities.”<br>&nbsp;&nbsp; — Albus Dumbledore, Harry Potter and the Chamber of Secrets</p>
</div>
<header>
<div id="name">
<h1>Books & Coffee</h1>
</div>
<div id="social-media">
<a href="https://twitter.com/login?lang=en" class="item2">
<i class="fab fa-twitter fa-1x"></i>
</a>
<a href="https://instagram.com" class="item3">
<i class="fab fa-instagram fa-1x"></i>
</a>
<a href="https://facebook.com" class="item4">
<i class="fab fa-facebook fa-1x"></i>
</a>
</div>
</header>

<div class="container circleBehind">
<a href="categories.py" onclick="loading()">Categories</a>
<a href="newlyadded.py" onclick="loading()">Newly added</a>
<a href="bestseller.py" onclick="loading()">Best sellers</a>
<a href="/sellingpage.html" onclick="loading()">Sell</a>
<a href="blog1.py" onclick="loading()">Blog</a>
<a href="/aboutus1.html">About Us</a>
</div><br><br>
""")
print('<center>')
print('<h2>Successfully registered!</h2>')
print('<a href="/loadinganim2.html"><h3>Click here to go back to the login page!</h3></a>')
#print('<input type="button"  value="Back to Reviews page">')
print('</center>')
print("""
<script type="text/javascript">
document.querySelector('.img__btn').addEventListener('click', function() {
document.querySelector('.cont').classList.toggle('s--signup');
});
</script>
<script type="text/javascript">

function myfunction(){

document.getElementById('load1').style.display="none";

}
function loading(){

document.getElementById('load1').style.display="block";

}

</script>
</body>
</html>
""")
conn.close()
