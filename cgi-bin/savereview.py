#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import sqlite3, cgi, cgitb
cust_id='c4'
form=cgi.FieldStorage()
rating=form.getvalue('review')
book_id=form.getvalue('bookid')
conn=sqlite3.connect('book_portal_proj.db')
statement="""INSERT into ratings_table (cust_id, book_id, rating) VALUES  (?,?,?)"""
data_tuple = (cust_id, book_id, rating)
conn.execute(statement, data_tuple)
conn.commit()
conn.close()
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('<link rel="stylesheet" type="text/css" href="/blog-page.css">')
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
print('<h2>RATING SAVED</h2><p>Thank you for rating the book!<br>Happy reading!:)</p>')
print('<a href="blog1.py"><h3>Go  to review!</h3></a>')
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
