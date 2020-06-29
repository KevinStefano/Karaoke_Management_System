# Fitur 3: Pembayaran
# Penanggung Jawab : 13518041 / Samuel
# Berisi daftar fungsi yang dibutuhkan pembayaran

import mysql.connector

# Mengakses database Karaoke KMS dalam sistem localhost
mydb = mysql.connector.connect(host="localhost",user="root",passwd="kevin123451001",database="DatabaseKMS")
# Mengecek ada atau tidaknya seorang member
def doesMemberExist(emailMember):
    mycursor = mydb.cursor()
    formula = "select email from membership where email = %s"
    mycursor.execute(formula, (emailMember,))
    results = mycursor.fetchall()
    if(len(results) != 0):
        return True
    return False

# Mengambil pemesanan ruangan yang belum dibayar
def findUnpaidBookingTransaction(emailMember):
    mycursor = mydb.cursor()
    memberQuery = False
    if(len(emailMember)==0):
        formula = "select p.id_pesanan, p.nomor_ruangan, r.tipe, p.harga_akhir from daftarpemesanan p join daftarruangan r on p.nomor_ruangan = r.no_ruangan where p.is_bayar='BELUMBAYAR' and p.email is null"
        mycursor.execute(formula)
    else:
        formula1 = "select p.id_pesanan, p.nomor_ruangan, r.tipe, p.harga_akhir from daftarpemesanan p join daftarruangan r on p.nomor_ruangan = r.no_ruangan where p.is_bayar='BELUMBAYAR' and p.email = %s"
        memberQuery = True
        mycursor.execute(formula1,(emailMember,))
    results = mycursor.fetchall()
    if(len(results) != 0):
        return results[0]
    return 0
    

# Mengambil iuran membership yang belum dibayar
def findUnpaidMembershipTransaction(emailMember):
    mycursor = mydb.cursor()
    formula = "select email, paket_membership, due_date from membership where due_date <= curdate() and email = %s"
    mycursor.execute(formula, (emailMember,))
    results = mycursor.fetchall()
    if(len(results) != 0):
        return results[0]
    return 0

# Mengupdate table di daftar pemesanan untuk record yang sudah dibayar
def updateBookingTransaction(idPesanan):
    mycursor = mydb.cursor()
    formula = "update daftarpemesanan set is_bayar='LUNAS' where id_pesanan=%s"
    mycursor.execute(formula, (idPesanan,))
    mydb.commit()

# Mengupdate table di pembayaranmembership untuk perpanjangan masa aktif member
def updateMembershipTransaction(emailMember, harga):
    mycursor = mydb.cursor()
    formula1 = "select * from pembayaranmembership where email = %s"
    mycursor.execute(formula1,(emailMember,))
    result = mycursor.fetchall()
    if len(result) == 0:
        query = "insert into pembayaranmembership values(%s, curdate(), date_add(curdate(), interval 1 year), %s)"
        query2 = "update membership set due_date=date_add(curdate(), interval 1 year) where email=%s"
        mycursor.execute(query,(emailMember, harga,))
        mycursor.execute(query2, (emailMember,))
    else:
        formula = "update pembayaranmembership set due_date_lama = due_date_baru, due_date_baru = date_add(due_date_baru, interval 1 year), total_harga = %s where email = %s"
        mycursor.execute(formula, (harga, emailMember,))
        formula2 = "update membership set due_date = (select due_date_baru from pembayaranmembership where email = %s) where email = %s"
        mycursor.execute(formula2, (emailMember, emailMember,))
    mydb.commit()
