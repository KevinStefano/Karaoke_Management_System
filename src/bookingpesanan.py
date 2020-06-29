# Fitur 4: Booking Pesanan / Pemesanan Ruangan
# Penanggung Jawab : 13518056 / Michael Hans
# Berisi daftar fungsi yang dibutuhkan terkait booking pesanan

from datetime import date
from datetime import datetime
import mysql.connector
import tkinter.messagebox as messagebox

# Menghubungkan modul dengan database
mydb = mysql.connector.connect(host="localhost",user="root",passwd="kevin123451001",database="DatabaseKMS")

# cekMembership -> mengecek email dalam tabel membership pada database
def cekMembership(emailPelanggan):
    mycursor = mydb.cursor()
    formula = "SELECT email FROM membership"
    mycursor.execute(formula)
    for email in mycursor.fetchall():
        if (emailPelanggan == email[0]) :
            return True
    return False

# cekWaktu ->  mengecek ketersediaan waktu pada hari ini
def cekWaktu(waktu, date):
    mycursor = mydb.cursor()
    formula = "select no_ruangan from daftarruangan where no_ruangan not in (select nomor_ruangan from daftarpemesanan where waktu_masuk = '" + waktu + "' and tanggal = '" + date + "')"
    mycursor.execute(formula)
    if len(mycursor.fetchall()) == 0:
        return False
        messagebox.showerror("Maaf", "Waktu pada "+waktu+" sudah penuh")
    else:
        return True
        messagebox.showinfo("Success", "Waktu pada "+waktu+" tersedia")

# getDaftarRuangan -> mengembalikan daftarruangan yang tersedia pada waktu yang dipilih
def getDaftarRuangan(waktu, date):
    mycursor = mydb.cursor()
    formula = "select distinct(tipe) from jenisruangan where tipe in "
    formula += "(select tipe from daftarruangan where no_ruangan not in (select nomor_ruangan from daftarpemesanan where waktu_masuk = '" + waktu + "' and tanggal = '" + date + "'))"
    mycursor.execute(formula)
    return [i[0] for i in mycursor.fetchall()]

# getTotalPesanan -> mengembalikan banyaknya pesanan dalam tabel daftarpemesanan
def getTotalPesanan():
    mycursor = mydb.cursor()
    formula = "SELECT count(id_pesanan) FROM daftarpemesanan"
    mycursor.execute(formula)
    data = mycursor.fetchone()[0]
    return data

# getIDPesanan -> membangkitkan IDPesanan secara unik dari database
def getIDPesanan():
    mycursor = mydb.cursor()
    formula = "SELECT id_pesanan FROM daftarpemesanan ORDER BY id_pesanan ASC"
    mycursor.execute(formula)
    queryresult = mycursor.fetchall()
    result = 1
    iterator = 0
    max_iterator = getTotalPesanan()
    while (iterator < max_iterator):
        if (result != queryresult[iterator][0]):
            break
        else:
            result += 1
            iterator += 1
    return result

# getPriceOfRuangan -> mengembalikan harga dari suatu ruangan
def getPriceOfRuangan(nomor, email):
    mycursor = mydb.cursor()
    formula = "SELECT no_ruangan, hargabiasa, hargadiskon FROM daftarruangan, jenisruangan WHERE daftarruangan.tipe = jenisruangan.tipe ORDER BY no_ruangan"
    mycursor.execute(formula)
    for (no_ruangan, hargabiasa, hargadiskon) in mycursor.fetchall():
        if (nomor == no_ruangan):
            if (cekMembership(email)):
                return hargadiskon
            else:
                return hargabiasa
    return 0

# getAvailableRoom -> mengembalikan nomor ruangan dengan tipe yang diinginkan
def getAvailableRoom(tipe, waktu, date):
    mycursor = mydb.cursor()
    formula = "select no_ruangan from daftarruangan where tipe = '" + tipe + "' and no_ruangan not in (select nomor_ruangan from daftarpemesanan where waktu_masuk = '" + waktu + "' and tanggal = '" + date + "')"
    mycursor.execute(formula)
    return mycursor.fetchone()[0]

# printPemesanan -> menuliskan ke dalam layar semua info terkait pemesanan
def printPemesanan():
    print("all")
    mycursor = mydb.cursor()
    formula = "SELECT * FROM daftarpemesanan"
    mycursor.execute(formula)
    for (id_pesanan, nama, email, no_ruangan, tanggal, waktu_masuk, durasi, harga_akhir, is_bayar) in mycursor.fetchall():
        print("ID Pesanan:",id_pesanan)
        print("Nama:",nama)
        print("Email:",email)
        print("No Ruangan:",no_ruangan)
        print("Tanggal:",tanggal)
        print("Waktu Masuk:",waktu_masuk)
        print("Durasi:",durasi)
        print("Harga Akhir:",harga_akhir)
        print("Status Bayar:",is_bayar)

# tambahPesananRuangan -> menambahkan pesanan ruangan ke dalam tabel daftarpemesanan
def tambahPesananRuangan(id_pesanan, nama, email, no_ruangan, tanggal, waktu_masuk, durasi, harga_akhir):
    mycursor = mydb.cursor()
    status = "BELUMBAYAR"
    formula = "INSERT INTO daftarpemesanan VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(formula,(id_pesanan, nama, email, no_ruangan, tanggal, waktu_masuk, durasi, harga_akhir, status))
    mydb.commit()

# Connect to DatabaseKMS.sql
def bookNow(waktuInfo, ruanganInfo, namaInfo, alamatInfo, telpInfo, emailInfo):
    today = date.today()
    now = datetime.now()
    id_pesanan = getIDPesanan()
    nama = namaInfo.get()
    email = emailInfo.get()
    tanggal = today.strftime("%Y-%m-%d")
    waktu_masuk = waktuInfo.get() + ":00"
    no_ruangan = getAvailableRoom(ruanganInfo.get(), waktu_masuk, tanggal)
    durasi = 60
    harga_akhir = getPriceOfRuangan(no_ruangan, email)
    if (cekMembership(email)):
        messagebox.showinfo("Perhatian!", "Selamat, anda mendapatkan diskon dari membership")
    else:
        email = None;
    tambahPesananRuangan(id_pesanan, nama, email, no_ruangan, tanggal, waktu_masuk, durasi, harga_akhir)
    messagebox.showinfo("Success", "Pesanan berhasil ditambahkan!")