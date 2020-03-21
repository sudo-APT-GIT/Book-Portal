#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi, sqlite3,math
#conn=sqlite3.connect('book_portal_proj.db')
#print ("opened database successfully")
count=0
bookname=[]
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    #print("Stored blob data into: ", filename, "\n")

def readBlobData():
    try:
        sqliteConnection = sqlite3.connect('book_portal_proj.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from book_table"""
        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        i=len(record)
        count=0
        for row in record:
            #print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[5]
            #price = row[4]
            #resumeFile = row[3]
            #print("Storing employee image and resume on disk \n")

            photoPath = "C:\\xampp\\htdocs\\imgret\\" + name + ".jpg"
            #resumePath = "E:\pynative\Python\photos\db_data\\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
        cursor.close()
        cursor1 = sqliteConnection.cursor()
        sql_fetch_blob_query = """SELECT price, book_name from book_table"""
        cursor1.execute(sql_fetch_blob_query)
        record = cursor1.fetchall()
        z=math.floor(i/3)
        for k in range(z):            
            print (' <div class="box">')
            for row in record:
                print ('  <div class="card">')
                print ('   <div class="imgBx">')
                name  = row[1]
                price = row[0]
                bookname.append(name)
                #print ('     <img src="/imgret/harry.jpg" alt="images">')
                count=count+1
                print ('<a href="orderconfirm.py"><img src="/imgret/'+name+'.jpg" alt="images"></a><br>')
                print (' </div>')
                print (' <div class="details">')
                print ('   <h2>'+name+'<br><span>Price: &#x20b9;'+str(price)+'</span></h2>')
                print ('  </div>')
                print ('  </div>')
            print ('</div>')
            print('<br><br>')       
            #writeTofile(resumeFile, resumePath)
           # print ("<img src='/imgret/"+name+".jpg' width='500' height='500'><br>")
        cursor1.close()
       

    except sqlite3.Error as error:
        #print("Failed to read blob data from sqlite table", error)
        print('')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("sqlite connection is closed")
form=cgi.FieldStorage();
username=form.getvalue('username')
password=form.getvalue('password')
conn=sqlite3.connect('book_portal_proj.db')
cursor=conn.execute('SELECT cust_id FROM customer WHERE email="%s"' %(username))
for row in cursor:
    cid=row[0]
fil=open("output.txt","a")
fil.write(cid+"\n")
fil.close()
cursor=conn.execute("SELECT email, password from customer")
flag=0
for row in cursor:
    if row[0]==username and row[1]==password:
        flag=1
        break
conn.close()
if flag==1:
    print ('Content-type:text/html\r\n\r\n')
    print ('<html>')
    print ('<head>')
    print ('<title>BookPage</title>')
    print ('    <link rel="stylesheet" type="text/css" href="/book-page.css">')
    print ('    <script src="https://kit.fontawesome.com/9743c13cfa.js"></script>')
    print ('</head>')
    print ('<body>')
    print ('<body onload="myfunction()">')
    print ('    <div id="load1">')
    print ('    <div id="load">')
    print ('  <hr/><hr/><hr/><hr/> ')
    print ('</div>')
    print ('   <br>')
    print ('   <p>"It is our choices, Harry, that show what we truly are, far more than our abilities.”<br>&nbsp;&nbsp; — Albus Dumbledore, Harry Potter and the Chamber of Secrets</p>')
    print ('    </div>')
    print ('    <header>')
    print ('       <div id="name">')
    print ('            <h1>Books & Coffee</h1>')
    print ('        </div>')
    print ('        <div id="social-media">')
    print ('            <a href="https://twitter.com/login?lang=en" class="item2">')
    print ('            <i class="fab fa-twitter fa-1x"></i>')
    print ('            </a>')
    print ('            <a href="https://instagram.com" class="item3">')
    print ('            <i class="fab fa-instagram fa-1x"></i>')
    print ('            </a>')
    print ('           <a href="https://facebook.com" class="item4">')
    print ('           <i class="fab fa-facebook fa-1x"></i>')
    print ('           </a>')
    print ('      </div>')
    print ('  </header>')

    print ('  <div class="container circleBehind">')
    print ('      <a href="categories.py" onclick="loading()">Categories</a>')
    print ('      <a href="newlyadded.py" onclick="loading()">Newly added</a>')
    print ('      <a href="bestseller.py" onclick="loading()">Best sellers</a>')
    print ('     <a href="/sellingpage.html" onclick="loading()">Sell</a>')
    print ('     <a href="blog1.py" onclick="loading()">Blog</a>')
    print ('     <a href="/aboutus1.html">About Us</a>     ')
    print ('     <a href="rec.py">Surprise Me</a>     ')

    print ('  </div>   ')

    print (' <br>')
    readBlobData()
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
else:
    print ('Content-type:text/html\r\n\r\n')
    print ('<html>')
    print ('<head>')
    print ('<title>BookPage</title>')
    print ('    <link rel="stylesheet" type="text/css" href="/book-page.css">')
    print ('    <script src="https://kit.fontawesome.com/9743c13cfa.js"></script>')
    print ('</head>')
    print ('<body onload="myfunction()">')
    print ('    <div id="load1">')
    print ('    <div id="load">')
    print ('  <hr/><hr/><hr/><hr/> ')
    print ('</div>')
    print ('   <br>')
    print ('   <p>"It is our choices, Harry, that show what we truly are, far more than our abilities.”<br>&nbsp;&nbsp; — Albus Dumbledore, Harry Potter and the Chamber of Secrets</p>')
    print ('    </div>')
    print ('    <header>')
    print ('       <div id="name">')
    print ('            <h1>Books & Coffee</h1>')
    print ('        </div>')
    print ('        <div id="social-media">')
    print ('            <a href="https://twitter.com/login?lang=en" class="item2">')
    print ('            <i class="fab fa-twitter fa-1x"></i>')
    print ('            </a>')
    print ('            <a href="https://instagram.com" class="item3">')
    print ('            <i class="fab fa-instagram fa-1x"></i>')
    print ('            </a>')
    print ('           <a href="https://facebook.com" class="item4">')
    print ('           <i class="fab fa-facebook fa-1x"></i>')
    print ('           </a>')
    print ('      </div>')
    print ('  </header>')

    print ('  <div class="container circleBehind">')
    print ('      <a href="#" onclick="loading()">Categories</a>')
    print ('      <a href="#" onclick="loading()">Newly added</a>')
    print ('      <a href="#" onclick="loading()">Best sellers</a>')
    print ('     <a href="#" onclick="loading()">Sell</a>')
    print ('     <a href="#" onclick="loading()">Blog</a>')
    print ('     <a href="/aboutus1.html">About Us</a>     ')
    print ('  </div>   ')
    print (' <br>')
    print ('<center>')
    print ('<h1>Please Register!</h1>')
    print('''<h2>New here?</h2>
        <p>Sign up and discover great<br> amount of new genres!</p>''')
    print ('</center>')
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
