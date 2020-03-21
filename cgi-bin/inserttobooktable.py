import sqlite3

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(book_id, book_name, author_id, genre, price, book_image):
    try:
        sqliteConnection = sqlite3.connect('book_portal_proj.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO 'book_table'
                                  ('book_id', 'book_name', 'author_id', 'genre', 'price', 'book_image') VALUES (?, ?, ?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(book_image)
        #resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (book_id, book_name, author_id, genre, price, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

#insertBLOB("1", "HarryPotterPART1", "D:\\5th SEM\\ITT Lab\\database\\img\\harry.jpg")
insertBLOB("b15", "brief","a2","Humour","399" ,"C:\\xampp\\htdocs\\imgret\\brief.jpeg",)
