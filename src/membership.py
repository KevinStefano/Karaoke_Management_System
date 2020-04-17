# Fitur 5: Membership
# Penanggung Jawab : 13518077 / Filbert Wijaya
# Berisi daftar fungsi yang dibutuhkan terkait pendaftaran membership

import mysql.connector
from datetime import *

mydb = mysql.connector.connect(host="localhost",user="root",passwd="2908Randy",database="kms")

def isInDataAdmin(username, password):
    mycursor = mydb.cursor()
    formula = "SELECT * FROM DataAdmin"
    mycursor.execute(formula)
   
    for (user,passw,name) in mycursor.fetchall():
        if (username ==user and password ==passw) :
            return 1
            break
    return 0
    
def updateTableMembership(email, nama, umur, alamat, notelp, paket, time):
    mycursor = mydb.cursor()
    formula = "INSERT INTO Membership VALUES (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(formula,(email, nama, umur, alamat, notelp, paket, time))
    mydb.commit()
