# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

import mysql.connector

#Connect to Database
#bisa disesuaikan sendiri sama MYSQL masing-masing
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="kevin123451001",
  database="DatabaseKMS"
)

def isInDataAdmin(username, password):
#return 1 if Found username and password in database
#return 0 if is not found
    mycursor = mydb.cursor()
    formula = "SELECT * FROM DataAdmin"
    mycursor.execute(formula)
   
    for (user,passw,name) in mycursor.fetchall():
        if (username ==user and password ==passw) :
            return 1
            break
    return 0

def updateTableJenisRuangan(tipe, kapasitas, hargabiasa,hargadiskon):
    mycursor = mydb.cursor()
    formula = "INSERT INTO JenisRuangan VALUES (%s,%s,%s,%s)"
    mycursor.execute(formula,(tipe,kapasitas,hargabiasa,hargadiskon))
    mydb.commit()



def deleteTableJenisRuangan(tipe_):
    mycursor = mydb.cursor()
    formula = "DELETE FROM JenisRuangan where tipe = tipe_ "
    mycursor.execute(formula)
    mydb.commit()