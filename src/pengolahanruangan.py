# Fitur 1: Pengolahan Ruangan
# Penanggung Jawab : 13518104 / Kevin Austin Stefano
# Berisi daftar fungsi yang dibutuhkan terkait pengolahan ruangan

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="2908Randy",database="kms")

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
    
def deleteTipeRuangan(tipe_):
    mycursor2 = mydb.cursor()
    formula2 = "DELETE FROM JenisRuangan where tipe = %s "
    formula3 = "DELETE FROM DaftarRuangan where tipe = %s "
    mycursor2.execute(formula2,(tipe_,))
    mydb.commit()
    mycursor2.execute(formula3,(tipe_,))
    mydb.commit()

def deleteNomorRuangan(nomor, tipe):
    mycursor = mydb.cursor()
    formula = "DELETE FROM DaftarRuangan where tipe = %s and no_ruangan = %s"
    mycursor.execute(formula,(tipe,nomor,))
    mydb.commit()

def addTipeRuangan(tipe, kapasitas, hargabiasa,hargadiskon, nomor, username):
    mycursor2 = mydb.cursor()
    formula = "INSERT INTO JenisRuangan VALUES (%s,%s,%s,%s)"
    mycursor2.execute(formula,(tipe,kapasitas,hargabiasa,hargadiskon))
    mydb.commit()

    mycursor = mydb.cursor()
    formula2 = "INSERT INTO DaftarRuangan VALUES (%s,%s,%s)"
    mycursor.execute(formula2,(nomor,tipe,username))    
    mydb.commit()

def addDaftarRuangan(tipe,nomor, username):
    mycursor = mydb.cursor()
    formula2 = "INSERT INTO DaftarRuangan VALUES (%s,%s,%s)"
    mycursor.execute(formula2,(nomor,tipe,username))    
    mydb.commit()

def isNomorAvailable(nomor):
    #return 1 if Found username and password in database
    #return 0 if is not found
    mycursor = mydb.cursor()
    formula = "SELECT * FROM DaftarRuangan"
    mycursor.execute(formula)
    for (no,tipe,name) in mycursor.fetchall():
        if (int(no) == int(nomor)) :
            return 0
            break
    return 1


def isTipeAvailable(tipe_):
    #return 1 if Found username and password in database
    #return 0 if is not found
    mycursor = mydb.cursor()
    formula = "SELECT * FROM DaftarRuangan"
    mycursor.execute(formula)
    for (no,tipe,name) in mycursor.fetchall():
        if (tipe == tipe_) :
            return 0
            break
    return 1

