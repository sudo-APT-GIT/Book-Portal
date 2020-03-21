#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib, cgi,cgitb,sqlite3
# Define these once; use them twice!
strFrom = 'helo76477@gmail.com'
#strTo = orderconfirm.email
form=cgi.FieldStorage()
#username=form.getvalue('username')
username='paishreya1412@gmail.com'
conn=sqlite3.connect('book_portal_proj.db')
cursor=conn.execute("SELECT email, password from customer")
flag=0
password=""
for row in cursor:
    if row[0]==username:
        password=row[1]
        flag=1
        break
conn.close()
#flag=0
if flag==1:
        # me == my email address
        # you == recipient's email address
        me = "helo76477@gmail.com"
        you = username

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Online Book Portal-Password"
        msg['From'] = me
        msg['To'] = you

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hey there,Your password is "+password+". Happy Reading:)"
        html = """\
        <html>
          <head></head>
          <body>
            <p>Hey there!<br>
               Your password is """+password+""".<br>Happy Reading:)
            </p>
          </body>
        </html>
        """

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message via local SMTP server.
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login('helo76477@gmail.com', 'swashe99')
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(me, you, msg.as_string())
        s.quit()

        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
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
        print('<h2>HOLA!</h2><p>Please check your email!</p>')
        print('<a href="/loadinganim2.html"><h3>Go back to Login</h3></a>')
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
else:
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
	print('<h2>Invalid Username!</h2><p>Sign up and discover great<br> amount of new genres!</p>')
	print('<a href="/loadinganim2.html"><h3>Click here to go back to the Login page!</h3></a>')
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
