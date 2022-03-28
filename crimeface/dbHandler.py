import pymysql

def insertData(data):
    rowId = 0

    db = pymysql.connect("localhost", "criminaluser", "", "criminaldb")
    cursor = db.cursor()
    print("database connected")

    query = "INSERT INTO face_criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["FathersName"], data["MothersName"], data["Gender"],
             data["DOB"], data["BloodGroup"], data["IdentificationMark"],
             data["Nationality"], data["Religion"], data["CrimesDone"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")

    db.close()
    print("connection closed")
    return rowId


def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect("localhost", "criminaluser", "", "criminaldb")
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM face_criminaldata WHERE name='%s'" % name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id = result[0]
        crim_data = {
            "Name": result[1],
            "Father's Name": result[2],
            "Mother's Name": result[3],
            "Gender": result[4],
            "DOB(yyyy-mm-dd)": result[5],
            "Blood Group": result[6],
            "Identification Mark": result[7],
            "Nationality": result[8],
            "Religion": result[9],
            "Crimes Done": result[10]
        }

        print("data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)
