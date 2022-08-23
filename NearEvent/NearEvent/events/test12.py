import sqlite3



def convertToBinaryData(filename,mode):
    # Convert binary format to images
    # or files data
    with open(filename, mode) as file:
        blobData = file.read()
    return blobData


def insertBLOB(name, photo):
    try:

        # Using connect method for establishing
        # a connection
        sqliteConnection = sqlite3.connect('db.SQL3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert query
        sqlite_insert_blob_query = """ INSERT INTO Student
                                  (name, img) VALUES (?, ?)"""

        # Converting human readable file into
        # binary data
        empPhoto = convertToBinaryData(photo)

        # Convert data into tuple format
        data_tuple = (name, empPhoto)

        # using cursor object executing our query
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")