#!C:\Users\MAHE\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi, sqlite3
conn=sqlite3.connect('book_portal_proj.db')
#print ("opened database successfully")

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

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
        print("Failed to read blob data from sqlite table", error)
        print("<br>")
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")
print ("Content-type:text/html\r\n\r\n")

print ("<html>")
print ("<head>")
print ("<meta charset='UTF-8'>")
print ("<title>Order Yo</title>")
print ("</head>")
print ("<body>")
readBlobData()
print ("</body>")
print ("</html>")
