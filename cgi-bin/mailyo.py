#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
# Define these once; use them twice!
strFrom = 'helo76477@gmail.com'
strTo = 'paishreya1412@gmail.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'ONLINE BOOK PORTAL Order no-7121999 shipping notification'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('Hello there, <br/><br/></br>Your Order no. 7121999 has been shipped. We hope you like the book.<br/><br/></br><br><img src="cid:image1"><br><br><br><b><i>Happy reading! :)</i></b>', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('oliver twist.jpeg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)

#smtp = smtplib.SMTP()
#smtp.connect('smtp.gmail.com',587)
#smtp.login('helo76477', 'swashe99')
#smtp.sendmail(strFrom, strTo, msgRoot.as_string())
#smtp.quit()
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login('helo76477@gmail.com', 'swashe99')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(strFrom, strTo, msgRoot.as_string())
s.quit()
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
print('<h2>HOLA! ORDER SHIPPED</h2><p>We hope you like the book.<br>Happy reading!:)</p>')
print('<form action="/cgi-bin/savereview.py" method="get"><input type="text" name="review"/><br><br><input type="text" name="bookid"/><br><br><button type="submit" class="submit">Rate!</button></form><br>')
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
