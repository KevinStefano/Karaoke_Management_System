# Fitur 2: Pembatalan Pesanan
# Penanggung Jawab : 13518128 / Lionnarta Savirandy
# Berisi daftar fungsi yang dibutuhkan terkait pembatalan pesanan

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="kevin123451001",database="DatabaseKMS")
# Function to validate username and password in dataadmin database
def dataAdminProcessing(username, password):
  mycursor = mydb.cursor()
  formula = "SELECT * FROM dataadmin"
  mycursor.execute(formula)


  for(user,pw,name) in mycursor.fetchall():
    if ((username == user) and (password == pw)):
        return 1
  return 0;

# Function to get admin name based on given username and password
def adminName(username, password):
  mycursor = mydb.cursor()
  formula = "SELECT * FROM dataadmin"
  mycursor.execute(formula)

  for(user,pw,name) in mycursor.fetchall():
    if ((username == user) and (password == pw)):
      return name
  return "";

# Function to get daftarpemesanan detail from database based on given idpesanan
def getDataPemesanan(idpesanan):
  mycursor = mydb.cursor()
  formula = "SELECT * FROM daftarpemesanan"
  mycursor.execute(formula)

  for(idp,nama,email,no,tgl,cin,duration,price,isbayar) in mycursor.fetchall():
    if(int(idpesanan) == idp):
      return idp,nama,email,no,tgl,cin,duration,price,isbayar
  return "Data Invalid","Data Invalid","Data Invalid","Data Invalid","Data Invalid","Data Invalid","Data Invalid","Data Invalid","Data Invalid"

# Function to validate idpesanan in daftarpemesanan database
def isDataPemesananValid(idpesanan):
  mycursor = mydb.cursor()
  formula = "SELECT * FROM daftarpemesanan"
  mycursor.execute(formula)

  for(idp,nama,email,no,tgl,cin,duration,price,isbayar) in mycursor.fetchall():
    if(int(idpesanan) == idp):
      return True
  return False

# Function to delete a tuple information in daftarpemesanan database based on given idpesanan
def setBatal(idpesanan):
  mycursor = mydb.cursor()
  formula = "DELETE FROM daftarpemesanan where id_pesanan = " + idpesanan
  mycursor.execute(formula)
  mydb.commit()
