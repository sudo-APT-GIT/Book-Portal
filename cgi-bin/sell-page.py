#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi, sqlite3
#conn=sqlite3.connect('book_portal.db')
#print ("opened database successfully")
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(book_name, seller_id, price, book_image):
    try:
        sqliteConnection = sqlite3.connect('book_portal.db')
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO 'selling_table'
                                  ('book_name', 'seller_id', 'price', 'book_image') VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(book_image)
        #resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (book_name,seller_id, price, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        #print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        #print("Failed to insert blob data into sqlite table", error)
        print('')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print("the sqlite connection is closed")

#insertBLOB("1", "HarryPotterPART1", "D:\\5th SEM\\ITT Lab\\database\\img\\harry.jpg")
#insertBLOB("Persuasion", "c2","300" ,"C:\\xampp\\htdocs\\imgret\\persuasion.jpeg")

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
        for row in record:
            print('done')
            #print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[5]
            #resumeFile = row[3]
            #print("Storing employee image and resume on disk \n")

            photoPath = "C:\\xampp\\htdocs\\imgret\\" + name + ".jpg"
            #resumePath = "E:\pynative\Python\photos\db_data\\" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            #writeTofile(resumeFile, resumePath)
            print("<img src='/imgret/"+name+".jpg' alt='HP1' width='200' height='200'><br><br><br>")
            cursor.close()
    except sqlite3.Error as error:
        #print("Failed to read blob data from sqlite table", error)
        print("<br>")
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
           # print("sqlite connection is closed")

form=cgi.FieldStorage();
imgname=form.getvalue('imgname')
#imgname='cristmas'
price=form.getvalue('price')
conn=sqlite3.connect('book_portal.db')
imgpath="C:\\xampp\\htdocs\\imgret\\"+imgname+".jpeg"
insertBLOB(imgname,"c3",price, imgpath)
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
print('<h2>Successfully accepted!</h2>')
print('<a href="blog1.py"><h3>Click here to go back to the Reviews page!</h3></a>')
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

