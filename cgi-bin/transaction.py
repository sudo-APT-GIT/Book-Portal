#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35\python.exe
import cgi,cgitb
print('Content-type:text/html\r\n\r\n')
print('<html>')
print('<head>')
print('	<title>Navigatio bar animation</title>')
print('	<link rel="stylesheet" type="text/css" href="navanimation.css">')
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
<a href="#" onclick="loading()">Categories</a>
<a href="#" onclick="loading()">Newly added</a>
<a href="#" onclick="loading()">Best sellers</a>
<a href="#" onclick="loading()">Sell</a>
<a href="#" onclick="loading()">Blog</a>
<a href="aboutus1.html">About Us</a>


</div>   
<div class="row">
<div class="leftcolumn">
<div class="card">
<h5>Title description, Dec 7, 2017</h5>

<p style="overflow: auto; max-height: 180px;">Sunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit,t in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliquawlejfbwlefjbwlefbwleb. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ullamco.</p>
</div>
</div>
<div class="rightcolumn">
<div class="card">
<img src="pineapple.jpg" style="overflow: auto; max-height: 450px;">
</div>
</div>
</div>
<div class="row">
<div class="rightcolumn2">
<div class="card">
<img src="pineapple.jpg" style="overflow: auto; max-height: 450px;">
</div>
</div>
<div class="leftcolumn2">
<div class="card">
<h5>Title description, Dec 7, 2017</h5>

<p style="overflow: auto; max-height: 180px;">Sunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniledn wlkcd am, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSnim veniledn wlkcd am, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSnim veniledn wlkcd am, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ullamco.</p>
</div>
</div>


</div>
<div class="row">
<div class="leftcolumn">
<div class="card">
<h5>Title description, Dec 7, 2017</h5>

<p style="overflow: auto; max-height: 180px;">Sunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation unim veniledn wlkcd am, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSnim veniledn wlkcd am, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSnim veniledn wlkcd am, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSlSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ulSunt in culpa qudjscbkwjdci officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim sdcjlbsdcjklbwdlfcbwudcvbsdujkcad minim veniam, quis nostrud exercitation ullamco.</p>
</div>
</div>
<div class="rightcolumn">
<div class="card">
<img src="pineapple.jpg" style="overflow: auto; max-height: 450px;">
</div>
</div>
</div>
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
