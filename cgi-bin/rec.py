#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib, cgi,cgitb
import sqlite3 as sq
import numpy as np
import pandas as pd
# Define these once; use them twice!
strFrom = 'helo76477@gmail.com'
#strTo = orderconfirm.email
form=cgi.FieldStorage()
#username=form.getvalue('username')
username='paishreya1412@gmail.com'
me = "helo76477@gmail.com"
you = username

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Online Book Portal-Password"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hey there,Your Surprise Package is Packed. Happy Reading:)"
html = """\
<html>
<head></head>
<body>
  <p>Hey there!<br>
     Hey there,Your Surprise Package is Packed. Happy Reading:)
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



with open('output.txt', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    #print (last_line)
    c_id=last_line
#if the final set is empty give reccomendation for the highest selling/avg rating book
#c_id='c1'
#query no of customers and books
#cursor=conn.execute('select * from cust
n_c=10
n_b=15
a=np.full((n_c,n_b),np.nan)
conn=sq.connect('book_portal_proj.db')
cursor=conn.execute('select * from ratings_table')

for i in cursor :
    c=int (i[0][1:])
    b=int (i[1][1:])
    a[c-1][b-1]=i[2]

#print(a)


df = pd.DataFrame(a)
x=df.corr(method='pearson')
b=x.get_values()


cursor=conn.execute('select * from order_items_table2 where cust_id="%s"'%(c_id))
b_id_s=[]
k=0
for i in cursor:
     b_id_s.append(i[1])
     #print (b_id_s[k])
     k=k+1
     

#b_id_s=['b10','b3','b6']
a=set(b_id_s)
b_id_s=list(a)
b_id=[]
for i in b_id_s:
    b_id.append(int (i[1:])-1)

#print(b_id)
rec_book=[]
for i in b_id:
    for j in range(0,n_b):
        if(b[i][j]>0 and b[i][j]!=np.nan):
            rec_book.append(j)
#print(rec_book)
no_rep_book=set(rec_book)
#print(no_rep_book.difference(b_id))
list_rec_book=list(no_rep_book.difference(b_id))
#print(list_rec_book[0])
if(len(list_rec_book)!=0):
    x=str (list_rec_book[0])
    #print(x)
    x="b"+x
    #print(x)
else:
    x="b7"

conn.execute('insert into rec values("%s","%s")'%(c_id,x))
                   
conn.commit()

print('Content-type:text/html\r\n\r\n')

print('''

<html>
<head>
	<title>BookPage</title>
	<link rel="stylesheet" type="text/css" href="/blog-page.css">
  	<script src="https://kit.fontawesome.com/9743c13cfa.js"></script>
</head>
<body>
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
	
    <br><br>

<center>
  <p>You have surprised yourself!</p>  
</center>



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
''')
