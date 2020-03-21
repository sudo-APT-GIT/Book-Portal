#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi,cgitb,sqlite3
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('	<title>Navigatio bar animation</title>')
print('	<link rel="stylesheet" type="text/css" href="/blog-page.css">')
print('  <script src="https://kit.fontawesome.com/9743c13cfa.js"></script>')
print(' <style>')

print('.leftcolumn {   ')
print(' float: left;')
print('  width: 75%;')
print('  box-sizing: border-box;')
print('}')
print('.leftcolumn2 {   ')
print('  float: right;')
print('  width: 75%;')
print(' box-sizing: border-box;')
print('}')


print('.rightcolumn {')
print(' float: left;')
print('  width: 25%;')
print('  padding-left: 20px;')
print('  box-sizing: border-box;')
print('}')
print('.rightcolumn2')
print('{')
print('	float:left;')
print('	width: 23%;')

print(' 	box-sizing: border-box;')
print('}')


print('.card {')
print('   background-color: white;')
print('padding: 20px;')
print('margin-top: 20px;')

print('box-sizing: border-box;')

print('}')


print('.row:after {')
print('content: "";')
print('display: table;')
print(' clear: both;')
print(' box-sizing: border-box;')
print('}')

print('.description')
print('{')
print(' position:relative;')
print('display: inline;')
print('box-sizing: border-box;')
print('}')


print("""
@media screen and (max-width: 800px) {
.leftcolumn, .rightcolumn 
{   
width: 100%;
padding: 0;
box-sizing: border-box;
}

img
{
bottom: 50px;
float: right;
position: relative;
display: inline;
height: 200px;
width: 200px;
margin:0px 15px 0px 0px;
box-sizing: border-box;
}
}
p{
    font-family: Roboto Mono, monospace;
}
</style>
</head>
<body onload="myfunction()">
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
</div>
""")



conn=sqlite3.connect('book_portal_proj.db')
cursor=conn.execute('SELECT * FROM blog_table')
ctr=0
for row in cursor:

    if(ctr%2==0):
        print("""<div class="row">
    <div class="leftcolumn">
    <div class="card">
    
    <p style="overflow: auto; height: 220px;">%s</p>
    </div>
    </div>
    <div class="rightcolumn">
    <div class="card">
    <img src="%s" style="height:250px; width:250px;">
    </div>
    </div>
    </div>
    """ %(row[1],row[2]))
    else:
        print("""
<div class="row">
<div class="rightcolumn2">
<div class="card">
<img src="%s" style="height:250px; width:250px;">
</div>
</div>
<div class="leftcolumn2">
<div class="card">


<p style="overflow: auto; height: 220px;">%s</p>
</div>
</div>


</div>""" %(row[2],row[1]))
    ctr=ctr+1


print("""
<form action="blog_save.py" method="post">

<center>
<h4>Please enter your ID</h4>
<input type="text" name="cid">
<h4>Please enter your valuable comments</h4>
<textarea name="review" rows="10" cols="40"></textarea><br><br>
<h4>Please enter a link to the image of the book you have reviewed</h4>
<input type= "text" name="link" value=""><br><br>
<input type="submit" value="Submit" name="submit"></center></form>""")

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

