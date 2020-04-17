# Karaoke Management System (KMS)
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Main Program

# Import library dan modul-modul yang diperlukan
from tkinter import *
from tkinter import ttk
from bookingpesanan import *
from pengolahanruangan import *
from pembatalanpesanan import *
from membership import *
from pembayaran import *
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog

# Fungsi-Fungsi dan Prosedur Karaoke Management System (KMS)   
# raise_frame -> Membangkitkan frame selanjutnya untuk menggantikan frame sebelumnya
def raise_frame(frame):
    frame.tkraise()

# Fitur 1: Pengolahan Ruangan
verifikasi=0
username = 'null'

def resetVerifikasi():
    verifikasi = 0

def ErrorEmailMessage(): 
    messagebox.showerror("Error", "Email anda belom terverifikasi")

def ErrorNomorRuanganMessage(): 
    messagebox.showerror("Error", "Nomor ruangan sudah ada. Tidak bisa digunakan lagi")

def EmailMessageVerif():
    messagebox.showinfo("Information","YEAY... Email terkonfirmasi, silahkan lakukan penambahan ruangan atau penghapusan ruangan")

def NoErorTambahRuanganMessage():
    messagebox.showinfo("Information","YEAY... Tipe Ruangan berhasil ditambahkan")

def NoErorDeleteRuanganMessage():
    messagebox.showinfo("Information","YEAY... Ruangan berhasil dihapus")
   
def checkEmailPassword():
    user = PilihanEmail.get()
    pasw = PilihanPassword.get()
    global verifikasi 
    verifikasi= isInDataAdmin(user,pasw)
    if verifikasi==0:
        ErrorEmailMessage()
    else:
        global username
        username = user 
        EmailMessageVerif()
    ClearInfo1()

def tambahRuangan():

    tipe_ = PilihanTipeRuangan.get()
    kap_ = PilihanKapasitas.get()
    hargabiasa_ = PilihanHargaBiasa.get()
    hargadiskon_ = PilihanHargaDiskon.get()
    nomor_ = PilihanNomorRuangan.get()
    
    if isNomorAvailable(nomor_)==0:
        ErrorNomorRuanganMessage()
    else:
        if isTipeAvailable(tipe_)==0:
            addDaftarRuangan(tipe_,nomor_,username)
        else:
            addTipeRuangan(tipe_,kap_,hargabiasa_,hargadiskon_,nomor_,username)
        NoErorTambahRuanganMessage()
    ClearInfo2()

def hapusTipeRuangan() :
    deleteTipeRuangan(PilihanTipeRuanganHapus.get())
    NoErorDeleteRuanganMessage()
    ClearInfoHapus1()

def hapusNomorRuangan() :
    deleteNomorRuangan(PilihanNomorRuanganHapus.get(),PilihanNomorRuanganHapusTipe.get())
    NoErorDeleteRuanganMessage()
    ClearInfoHapus2()

def ClearInfo1() :
    PilihanEmail.delete(0,END)
    PilihanPassword.delete(0,END)

def ClearInfo2():
    PilihanTipeRuangan.delete(0, END)
    PilihanKapasitas.delete(0,END)
    PilihanHargaBiasa.delete(0,END)
    PilihanHargaDiskon.delete(0, END)
    PilihanNomorRuangan.delete(0,END)

def ClearInfoHapus1():
    PilihanTipeRuanganHapus(0,END)

def ClearInfoHapus2():
    PilihanNomorRuanganHapus(0,END)
    PilihanNomorRuanganHapusTipe(0,END)

# Fitur 2: Pembatalan Pesanan
def handle_focusin_username(_):
    if(Username.get() == "username" and lockUser.get() == 0):
        Username.delete(0, END)
        Username.config(fg="black")
        lockUser.set(1)

def handle_focusout_username(_):
    if(Username.get() == "" and lockUser.get() == 1):
        Username.delete(0,END)
        Username.config(fg="grey")
        usernameVar.set("username")
        lockUser.set(0)

def handle_focusin_password(_):
    if(Password.get() == "password" and lockPass.get() == 0):
        Password.delete(0, END)
        Password.config(fg="black", show="*")
        lockPass.set(1)

def handle_focusout_password(_):
    if(Password.get() == "" and lockPass.get() == 1):
        Password.delete(0,END)
        Password.config(fg="gray", show="")
        passwordVal.set("password")
        lockPass.set(0)

def handle_enter_login(_):
    adminCheck()

def handle_focusin_idtransaksi(_):
    if(IDTransaksi.get() == "ID Transaksi" and lockTrans.get() == 0):
        IDTransaksi.delete(0, END)
        IDTransaksi.config(fg="black")
        lockTrans.set(1)

def handle_focusout_idtransaksi(_):
    if(IDTransaksi.get() == "" and lockTrans.get() == 1):
        IDTransaksi.delete(0,END)
        IDTransaksi.config(fg="grey")
        IDTransaksiVar.set("ID Transaksi")
        lockTrans.set(0)
        NamaL.config(text="")
        EmailL.config(text="")
        NomorRuanganL.config(text="")
        TanggalL.config(text="")
        WaktuMasukL.config(text="")
        DurasiL.config(text="")
        HargaAkhirL.config(text="")
        StatusBayarL.config(text="")

def handle_enter_search(_):
    if(IDTransaksi.get() == ""):
        NamaL.config(text="")
        EmailL.config(text="")
        NomorRuanganL.config(text="")
        TanggalL.config(text="")
        WaktuMasukL.config(text="")
        DurasiL.config(text="")
        HargaAkhirL.config(text="")
        StatusBayarL.config(text="")
    else:
        showDetailPemesanan()

def messageError():
    messagebox.showerror("Login Failed","Username dan password yang dimasukkan salah")

def adminCheck():
    if(dataAdminProcessing(Username.get(),Password.get()) == 1):
        user = "Selamat datang, " + adminName(Username.get(), Password.get())
        messagebox.showinfo("Login Success", user)
        loginVer.set(1)
        LoginButton["state"] = "disabled"
        Password["state"] = "disabled"
        Username["state"] = "disabled"
        raise_frame(FrameDataPembatalan)
    else:
        messageError()

def messageBatal():
    if(isDataPemesananValid(IDTransaksi.get())):
        Msg = messagebox.askquestion("Cancel","Yakin batalkan pesanan?",icon='warning')
        if Msg == 'yes':
            setBatal(IDTransaksi.get())
            messagebox.showinfo("Cancel","Pesanan berhasil dihapus")
    else:
        messagebox.showerror("Data Invalid","Data yang anda masukkan tidak tersedia")

def logOutAdmin():
    if(loginVer.get() == 1):
        LoginButton["state"] = "normal"
        Password["state"] = "normal"
        Username["state"] = "normal"
        loginVer.set(0)
        IDTransaksi.delete(0,END)
        IDTransaksiVar.set("")
        Password.delete(0,END)
        passwordVal.set("")
        Username.delete(0,END)
        usernameVar.set("")
        raise_frame(FrameLogin)

def messageLogout():
    Msg = messagebox.askquestion("Log Out", "Apakah anda ingin Log Out?")
    if Msg == 'yes':
        messagebox.showinfo("Log Out","Log Out berhasil")
        logOutAdmin()

def showDetailPemesanan():
    idp,nama,email,no,tgl,cin,duration,price,isbayar = getDataPemesanan(IDTransaksi.get())
    NamaL.config(text=nama)
    EmailL.config(text=email)
    NomorRuanganL.config(text=no)
    TanggalL.config(text=tgl)
    WaktuMasukL.config(text=cin)
    DurasiL.config(text=duration)
    HargaAkhirL.config(text=price)
    StatusBayarL.config(text=isbayar)

# Fitur 3: Pembayaran
current_id_pesanan = 0
current_harga = 0
def raise_frame(frame):
    frame.tkraise()

def cariRuangan():
    global current_id_pesanan
    res = findUnpaidBookingTransaction(PilihanEmailMember1.get())
    if(res != 0):
        current_id_pesanan = res[0]
        print(current_id_pesanan)
        ListPembayaranRuangan.insert("","end",values=(res[1],res[2],res[3]))
        Total.configure(state="normal")
        if(len(Total.get()) != 0):
            current_total = int(Total.get())
            Total.delete(0, "end")
            new_total = current_total + res[3]
            Total.insert("end",str(new_total))
        else:
            Total.insert("end",str(res[3]))
        Total.configure(state="readonly")
    else:
        messagebox.showerror("Error","Data tidak ditemukan")

def cariMember():
    global current_harga
    res = findUnpaidMembershipTransaction(PilihanEmailMember.get())
    if(res != 0):
        harga = cariHarga(res[1])
        current_harga = harga
        ListPembayaranMember.insert("","end",values=(res[0],res[1],res[2],harga))
        Total1.configure(state="normal")
        if(len(Total1.get()) != 0):
            current_total = int(Total1.get())
            Total1.delete(0,"end")
            new_total = current_total + harga
            Total1.insert("end",str(new_total))
        else:
            Total1.insert("end",str(harga))
        Total1.configure(state="readonly")
    else:
        messagebox.showerror("Error", "Data tidak ditemukan")

def cariHarga(jenisMembership):
    if(jenisMembership == "Bronze"):
        return 1000000
    elif(jenisMembership == "Silver"):
        return 1500000
    else:
        return 2000000

def selesaiRuangan():
    updateBookingTransaction(current_id_pesanan)
    ListPembayaranRuangan.delete(*ListPembayaranRuangan.get_children())
    Total.configure(state="normal")
    Kembalian.configure(state="normal")
    Total.delete(0,"end")
    Uang.delete(0,"end")
    Kembalian.delete(0, "end")
    Total.configure(state="readonly")
    Kembalian.configure(state="readonly")

def selesaiMembership():
    updateMembershipTransaction(PilihanEmailMember.get(),current_harga)
    ListPembayaranMember.delete(*ListPembayaranMember.get_children())
    Total1.configure(state="normal")
    Kembalian1.configure(state="normal")
    Total1.delete(0,"end")
    Uang1.delete(0,"end")
    Kembalian1.delete(0, "end")
    Total1.configure(state="readonly")
    Kembalian1.configure(state="readonly")

def getKembalianRuangan():
    current_uang = int(Uang.get())
    current_total = int(Total.get())
    kembalian = current_uang - current_total
    if(kembalian < 0):
        messagebox.showerror("Error", "Kesalahan input jumlah uang")
    else:
        Kembalian.configure(state="normal")
        Kembalian.delete(0, "end")
        Kembalian.insert("end",str(kembalian))
        Kembalian.configure(state="readonly")

def getKembalianMembership():
    current_uang = int(Uang1.get())
    current_total = int(Total1.get())
    kembalian = current_uang - current_total
    if(kembalian < 0):
        messagebox.showerror("Error", "Kesalahan input jumlah uang")
    else:
        Kembalian1.configure(state="normal")
        Kembalian1.delete(0, "end")
        Kembalian1.insert("end",str(kembalian))
        Kembalian1.configure(state="readonly")

# Fitur 4: Pemesanan Ruangan
# setWaktu -> Menyetel waktu sesuai dengan waktu yang sudah dipilih
def setWaktu():
    if (len(PilihanWaktuInfo.get()) == 0):
        messagebox.showerror("Error", "Masih terdapat entri yang kosong")
    else:
        today = date.today()
        tanggal = today.strftime("%Y-%m-%d")
        waktu = PilihanWaktuInfo.get()
        if cekWaktu(waktu,tanggal):
            PilihanWaktuReadInfo.configure(state='normal')
            PilihanWaktuReadInfo.delete(0, 'end');
            PilihanWaktuReadInfo.insert(0, PilihanWaktuInfo.get())
            PilihanWaktuReadInfo.configure(state='readonly')
            PilihanRuanganInfo['values'] = getDaftarRuangan(waktu, tanggal)
            PilihanRuanganInfo.delete(0, 'end');
            PilihanRuanganReadInfo.configure(state='normal')
            PilihanRuanganReadInfo.delete(0, 'end');
            PilihanRuanganReadInfo.configure(state='readonly')
            messagebox.showinfo("Success", "Waktu pada "+PilihanWaktuInfo.get()+" tersedia")
        else:
            messagebox.showerror("Maaf", "Waktu pada "+waktu+" sudah penuh")

# setRuangan -> menyetel tipe ruangan sesuai dengan pilihan ruangan yang dipilih
def setRuangan():
    if (len(PilihanRuanganInfo.get()) == 0):
        messagebox.showerror("Error", "Masih terdapat entri yang kosong")
    else:
        PilihanRuanganReadInfo.configure(state='normal')
        PilihanRuanganReadInfo.delete(0, 'end');
        PilihanRuanganReadInfo.insert(0, PilihanRuanganInfo.get())
        PilihanRuanganReadInfo.configure(state='readonly')
        messagebox.showinfo("Success", "Pilihan ruangan pada "+PilihanRuanganInfo.get()+" berhasil dipilih")

# bookingRuangan -> melakukan proses pemesanan ruangan
def bookingRuangan():
    global PilihanWaktuReadInfo, PilihanRuanganReadInfo, NamaPemesanInfo, AlamatPemesanInfo, NomorTeleponInfo, EmailAddressInfo
    isValid = True
    for entry in (PilihanWaktuReadInfo, PilihanRuanganReadInfo, NamaPemesanInfo, AlamatPemesanInfo, NomorTeleponInfo):
        if (len(entry.get()) == 0):
            isValid = False
            break
    if (isValid):
        bookNow(PilihanWaktuReadInfo, PilihanRuanganReadInfo, NamaPemesanInfo, AlamatPemesanInfo, NomorTeleponInfo, EmailAddressInfo)
        resetEntry("FrameBiodataPemesan")
    else:
        messagebox.showerror("Error", "Wow Masih terdapat entri yang kosong")

# resetEntry -> membersihkan seluruh buffer dalam setiap entry dalam suatu frameName
def resetEntry(frameName):
    PilihanWaktuReadInfo.configure(state='normal')
    PilihanRuanganReadInfo.configure(state='normal')
    if (frameName == "FramePilihWaktu"):
        PilihanWaktuInfo.delete(0, 'end');
        PilihanRuanganReadInfo.delete(0, 'end');
    elif (frameName == "FramePilihRuangan"):
        PilihanRuanganInfo.delete(0, 'end');
        PilihanRuanganReadInfo.delete(0, 'end');
    elif (frameName == "FrameBiodataPemesan"):
        PilihanWaktuInfo.delete(0, 'end');
        PilihanWaktuReadInfo.delete(0, 'end');
        PilihanRuanganInfo.delete(0, 'end');
        PilihanRuanganReadInfo.delete(0, 'end');
        NamaPemesanInfo.delete(0, 'end');
        AlamatPemesanInfo.delete(0, 'end');
        EmailAddressInfo.delete(0, 'end');
        NomorTeleponInfo.delete(0, 'end');
    PilihanWaktuReadInfo.configure(state='readonly')
    PilihanRuanganReadInfo.configure(state='readonly')

# Fitur 5: Membership
def resetFrameMember(frameName):
    EmailAddressMemberInfo.delete(0, 'end')
    NamaCaMemberInfo.delete(0, 'end')
    UmurCaMemberInfo.delete(0, 'end')
    AlamatCaMemberInfo.delete(0, 'end')
    NomorTeleponCaMemberInfo.delete(0, 'end')
    PilihanMembernInfo.current(0)

def SubmitMember():
    email = EmailAddressMemberInfo.get()
    nama = NamaCaMemberInfo.get()
    umur = UmurCaMemberInfo.get()
    alamat = AlamatCaMemberInfo.get()
    notelp = NomorTeleponCaMemberInfo.get()
    paket = PilihanMembernInfo.get()
    time = datetime.now()
    if(email == ""):
        messagebox.showerror("Error","Email belum terisi")
    elif(nama == ""):
        messagebox.showerror("Error","Nama belum terisi")
    elif(umur == ""):
        messagebox.showerror("Error","Umur belum terisi")
    elif(alamat == ""):
        messagebox.showerror("Error","Alamat belum terisi")
    elif(notelp == ""):
        messagebox.showerror("Error","No Telp belum terisi")
    elif(paket == PilihanMemberValues[0]):
        messagebox.showerror("Error","Paket belum terisi")
    else:
        if (not(doesMemberExist(email))):
            updateTableMembership(email, nama, umur, alamat, notelp, paket, time)
            messagebox.showinfo("Information","Member baru berhasil ditambahkan")
            resetFrameMember("FrameMembership")
        else:
            messagebox.showinfo("Information","Email sudah diambil oleh yang lain")

# PROGRAM UTAMA: INITIALIZE APPLICATION PROGRAM
# Memanfaatkan Library Tkinter untuk Menampilkan GUI
# Main Program
root = Tk()
root.geometry('1024x768')
root.title("Karaoke Management System (KMS)")
root.configure(background='gray22')

# All Text and Labels In GUI
helv36 = tkinter.font.Font(family='Helvetica', size=36, weight='bold')
helv10 = tkinter.font.Font(family='Helvetica', size=10)
helv12 = tkinter.font.Font(family='Helvetica', size=12)
helv14 = tkinter.font.Font(family='Helvetica', size=14)
helv16 = tkinter.font.Font(family='Helvetica', size=16)

# Judul Program KMS
L2 = Label(root, text="Karaoke Management System (KMS)             ", bg = "orange", fg= "white")
L2['font'] = helv36
L2.grid(row=0, column=0, columnspan=3, sticky='news')

# SETUP SECTION: PELETAKKAN SETIAP FRAME DALAM GUI
# Menginisialisasi Letak-Letak Frame dalam GUI dengan Susunan:
# Left Menu     : RootMenu
# Middle Menu   : PengolahanRuanganMenu, LoginMenu, PembayaranMenu, PemesananRuanganMenu, TemplateMenu
# Right Menu    : Frame-Frame yang dibangkitkan dari setiap menu dalam Middle Menu

# Frame-Frame dalam GUI
RootMenu = Frame(root, height = 768, width = 240, bg = "gray22")
RootMenu.grid(row=1, column=0, sticky='news')

# Setup untuk Pengolahan Ruangan
PengolahanRuanganMenu = Frame(root, height = 768, width = 230, bg = "gray32")
PengolahanRuanganMenu.grid(row = 1, column = 1, sticky='news')
FramePenambahanRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePenambahanRuangan.grid(row = 1, column = 2, sticky='news')
FramePenghapusanRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePenghapusanRuangan.grid(row = 1, column = 2, sticky='news')

# Setup untuk Pembatalan Paksa
LoginMenu = Frame(root, height = 768, width = 230, bg = "gray32")
LoginMenu.grid(row = 1, column = 1, sticky='news')
FrameEmailLogin = Frame(root, height = 768, width = 554, bg = "gray22")
FrameEmailLogin.grid(row = 1, column = 2, sticky='news')
FrameDataPembatalan = Frame(root, height = 768, width = 554, bg = "gray22")
FrameDataPembatalan.grid(row = 1, column = 2, sticky='news')
FrameLogin = Frame(root, height = 768, width = 554, bg = "gray22")
FrameLogin.grid(row = 1, column = 2, sticky='news')

# Setup untuk Pembayaran
PembayaranMenu = Frame(root, height = 768, width = 230, bg = "gray32")
PembayaranMenu.grid(row = 1, column = 1, sticky='news')
FramePembayaranRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePembayaranRuangan.grid(row = 1, column = 2, sticky='news')
FramePembayaranMembership = Frame(root, height = 768, width = 554, bg = "gray22")
FramePembayaranMembership.grid(row = 1, column = 2, sticky='news')

# Setup Untuk PemesananRuangan
PemesananRuanganMenu = Frame(root, height = 768, width = 230, bg = "gray32")
PemesananRuanganMenu.grid(row = 1, column = 1, sticky='news')
FrameBiodataPemesan = Frame(root, height = 768, width = 554, bg = "gray22")
FrameBiodataPemesan.grid(row = 1, column = 2, sticky='news')
FramePilihWaktu = Frame(root, height = 768, width = 554, bg = "gray22")
FramePilihWaktu.grid(row = 1, column = 2, sticky='news')
FramePilihRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePilihRuangan.grid(row = 1, column = 2, sticky='news')

# Setup untuk Membership
TemplateMenu = Frame(root, height = 768, width = 230, bg = "gray32")
TemplateMenu.grid(row = 1, column = 1, sticky='news')
FrameMembership = Frame(root, height = 768, width = 554, bg = "gray22")
FrameMembership.grid(row = 1, column = 2, sticky='news')

# BUILDING SECTION: PELETAKKAN SETIAP OBJECT DALAM MASING-MASING FRAME
# Menu utama dalam aplikasi Karaoke Management System (KMS)
# Dibagi menjadi 5 bagian menu utama, yaitu:
# 1. Pengolahan Ruangan : menambahkan atau menghapus ruangan
# 2. Pembatalan Paksa   : membatalkan pesanan pelanggan
# 3. Pembayaran         : melakukan pembayaran terhadap pesanan atau iuran membership
# 4. Pemesanan Ruangan  : melakukan pemesanan ruangan berdasarkan waktu dan ruangan
# 5. Membership         : melakukan pendaftaran menjadi anggota member

# Background: Root Menu
# Menampilkan 5 buah button yang mewakili 5 buah fitur yang sudah disebutkan sebelumnya
ButtonPengolahanRuangan = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Pengolahan Ruangan", command=lambda:[resetVerifikasi(), raise_frame(PengolahanRuanganMenu), raise_frame(FrameEmailLogin)])
ButtonPengolahanRuangan['font'] = helv12
ButtonPengolahanRuangan.place(x=30, y=20, in_=RootMenu)

ButtonPembatalanPaksa = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Pembatalan Paksa", command=lambda:[logOutAdmin(), raise_frame(LoginMenu), raise_frame(FrameLogin)])
ButtonPembatalanPaksa['font'] = helv12
ButtonPembatalanPaksa.place(x=30, y=90, in_=RootMenu)

ButtonPembayaran = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Pembayaran", command=lambda:[raise_frame(PembayaranMenu), raise_frame(FramePembayaranRuangan)])
ButtonPembayaran['font'] = helv12
ButtonPembayaran.place(x=30, y=160, in_=RootMenu)

ButtonPemesanan = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Booking Ruangan", command=lambda:[raise_frame(PemesananRuanganMenu), raise_frame(FramePilihWaktu)])
ButtonPemesanan['font'] = helv12
ButtonPemesanan.place(x=30, y=230, in_=RootMenu)

ButtonMembership = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Membership", command=lambda:[raise_frame(TemplateMenu), raise_frame(FrameMembership)])
ButtonMembership['font'] = helv12
ButtonMembership.place(x=30, y=300, in_=RootMenu)

# Fitur 1: Pengolahan Ruangan
# Menampilkan Pengolahan Ruangan Menu dan Frame Email Login apabila Button Pengolahan Ruangan diclick
# Pengolahan Ruangan Menu
ButtonPenambahanRuangan = tkinter.Button(PengolahanRuanganMenu, height = 2, width = 20, bg='cyan', text ="Penambahan", command=lambda:(FramePenambahanRuangan).tkraise() if verifikasi==1 else ErrorEmailMessage())
ButtonPenambahanRuangan['font'] = helv12
ButtonPenambahanRuangan.place(x=20, y=20, in_=PengolahanRuanganMenu)

ButtonPenghapusanRuangan = tkinter.Button(PengolahanRuanganMenu, height = 2, width = 20, bg='cyan', text ="Penghapusan",  command=lambda:(FramePenghapusanRuangan).tkraise() if verifikasi==1 else ErrorEmailMessage())
ButtonPenghapusanRuangan['font'] = helv12
ButtonPenghapusanRuangan.place(x=20, y=90, in_=PengolahanRuanganMenu)

# Frame Email Login
LabelNamaUser = Label(FrameEmailLogin, text="Selamat Datang", bg = "gray22", fg= "white")
LabelNamaUser['font'] = helv16
LabelNamaUser.place(x=355, y=20, in_=FrameEmailLogin)

LabelEmail= Label(FrameEmailLogin, text="Email", bg = "gray22", fg= "white")
LabelEmail['font'] = helv16
LabelEmail.place(x=50, y=145, in_=FrameEmailLogin)

PilihanEmail = Entry(FrameEmailLogin, bd =2, width = 23)
PilihanEmail['font'] = helv16
PilihanEmail.place(x=240, y=145, in_=FrameEmailLogin)

LabelPassword= Label(FrameEmailLogin, text="Password", bg = "gray22", fg= "white")
LabelPassword['font'] = helv16
LabelPassword.place(x=50, y=190, in_=FrameEmailLogin)

PilihanPassword = Entry(FrameEmailLogin, bd =2, width = 23,show="*")
PilihanPassword['font'] = helv16
PilihanPassword.place(x=240, y=190, in_=FrameEmailLogin)

ButtonOK = tkinter.Button(FrameEmailLogin, height = 2, width = 10, bg='green', text ="OK", command = checkEmailPassword)
ButtonOK['font'] = helv14
ButtonOK.place(x=405, y=400, in_=FrameEmailLogin)

ButtonClearInfo1 = tkinter.Button(FrameEmailLogin, height = 2, width = 10, bg='yellow', text ="Clear", command = ClearInfo1)
ButtonClearInfo1['font'] = helv14
ButtonClearInfo1.place(x=265, y=400, in_=FrameEmailLogin)

# Frame Penambahan Ruangan
LabelTipeRuangan = Label(FramePenambahanRuangan, text="Tipe Ruangan", bg = "gray22", fg= "white")
LabelTipeRuangan ['font'] = helv16
LabelTipeRuangan.place(x=50, y=145, in_=FramePenambahanRuangan)

PilihanTipeRuangan = Entry(FramePenambahanRuangan, bd =2, width = 23)
PilihanTipeRuangan['font'] = helv16
PilihanTipeRuangan.place(x=240, y=145, in_=FramePenambahanRuangan)

LabelKapasitas= Label(FramePenambahanRuangan, text="Kapasitas", bg = "gray22", fg= "white")
LabelKapasitas['font'] = helv16
LabelKapasitas.place(x=50, y=190, in_=FramePenambahanRuangan)

PilihanKapasitas = Entry(FramePenambahanRuangan, bd =2, width = 23)
PilihanKapasitas['font'] = helv16
PilihanKapasitas.place(x=240, y=190, in_=FramePenambahanRuangan)

LabelHargaBiasa= Label(FramePenambahanRuangan, text="Harga Biasa", bg = "gray22", fg= "white")
LabelHargaBiasa['font'] = helv16
LabelHargaBiasa.place(x=50, y=235, in_=FramePenambahanRuangan)

PilihanHargaBiasa = Entry(FramePenambahanRuangan, bd =2, width = 23)
PilihanHargaBiasa['font'] = helv16
PilihanHargaBiasa.place(x=240, y=235, in_=FramePenambahanRuangan)

LabelHargaDiskon= Label(FramePenambahanRuangan, text="Harga Diskon", bg = "gray22", fg= "white")
LabelHargaDiskon['font'] = helv16
LabelHargaDiskon.place(x=50, y=280, in_=FramePenambahanRuangan)

PilihanHargaDiskon = Entry(FramePenambahanRuangan, bd =2, width = 23)
PilihanHargaDiskon['font'] = helv16
PilihanHargaDiskon.place(x=240, y=280, in_=FramePenambahanRuangan)

LabelNomorRuangan= Label(FramePenambahanRuangan, text="Nomor Ruangan", bg = "gray22", fg= "white")
LabelNomorRuangan['font'] = helv16
LabelNomorRuangan.place(x=50, y=325, in_=FramePenambahanRuangan)

PilihanNomorRuangan = Entry(FramePenambahanRuangan, bd =2, width = 23)
PilihanNomorRuangan['font'] = helv16
PilihanNomorRuangan.place(x=240, y=325, in_=FramePenambahanRuangan)

ButtonAdd= tkinter.Button(FramePenambahanRuangan, height = 2, width = 10, bg='green', text ="Add!", command = tambahRuangan)
ButtonAdd['font'] = helv14
ButtonAdd.place(x=405, y=400, in_=FramePenambahanRuangan)

ButtonClearInfo2 = tkinter.Button(FramePenambahanRuangan, height = 2, width = 10, bg='yellow', text ="Clear", command = ClearInfo2)
ButtonClearInfo2['font'] = helv14
ButtonClearInfo2.place(x=265, y=400, in_=FramePenambahanRuangan)

# Frame PenghapusanRuangan
LabelTipeRuanganHapusJudul = Label(FramePenghapusanRuangan, text="PENGHAPUSAN TIPE RUANGAN", bg = "gray22", fg= "white")
LabelTipeRuanganHapusJudul ['font'] = helv16
LabelTipeRuanganHapusJudul.place(x=50, y=100, in_=FramePenghapusanRuangan)

LabelTipeRuanganHapus = Label(FramePenghapusanRuangan, text="Tipe Ruangan", bg = "gray22", fg= "white")
LabelTipeRuanganHapus ['font'] = helv16
LabelTipeRuanganHapus.place(x=50, y=145, in_=FramePenghapusanRuangan)

PilihanTipeRuanganHapus = Entry(FramePenghapusanRuangan, bd =2, width = 23)
PilihanTipeRuanganHapus['font'] = helv16
PilihanTipeRuanganHapus.place(x=240, y=145, in_=FramePenghapusanRuangan)

ButtonHapus = tkinter.Button(FramePenghapusanRuangan, height = 2, width = 10, bg='red', text ="Hapus", command = hapusTipeRuangan)
ButtonHapus['font'] = helv14
ButtonHapus.place(x=405, y=190, in_=FramePenghapusanRuangan)

LabelNomorRuanganHapusJudul = Label(FramePenghapusanRuangan, text="PENGHAPUSAN NOMOR RUANGAN", bg = "gray22", fg= "white")
LabelNomorRuanganHapusJudul ['font'] = helv16
LabelNomorRuanganHapusJudul.place(x=50, y=260, in_=FramePenghapusanRuangan)

LabelNomorRuanganHapusTipe = Label(FramePenghapusanRuangan, text="Tipe Ruangan", bg = "gray22", fg= "white")
LabelNomorRuanganHapusTipe ['font'] = helv16
LabelNomorRuanganHapusTipe.place(x=50, y=305, in_=FramePenghapusanRuangan)

PilihanNomorRuanganHapusTipe = Entry(FramePenghapusanRuangan, bd =2, width = 23)
PilihanNomorRuanganHapusTipe['font'] = helv16
PilihanNomorRuanganHapusTipe.place(x=240, y=305, in_=FramePenghapusanRuangan)

LabelNomorRuanganHapus = Label(FramePenghapusanRuangan, text="Nomor Ruangan", bg = "gray22", fg= "white")
LabelNomorRuanganHapus ['font'] = helv16
LabelNomorRuanganHapus.place(x=50, y=345, in_=FramePenghapusanRuangan)

PilihanNomorRuanganHapus = Entry(FramePenghapusanRuangan, bd =2, width = 23)
PilihanNomorRuanganHapus['font'] = helv16
PilihanNomorRuanganHapus.place(x=240, y=345, in_=FramePenghapusanRuangan)

ButtonHapus2 = tkinter.Button(FramePenghapusanRuangan, height = 2, width = 10, bg='red', text ="Hapus", command = hapusNomorRuangan)
ButtonHapus2['font'] = helv14
ButtonHapus2.place(x=405, y=395, in_=FramePenghapusanRuangan)

# Fitur 2: Pembatalan Paksa
# Menampilkan Menu Login dan Frame Pembatalan Pesanan apabila Button Pembatalan Paksa diclick
# Login Menu
# Username GUI
lockUser = IntVar()
lockUser.set(0)
usernameVar = StringVar()
usernameVar.set("username")
Username = Entry(LoginMenu, bd=2, width=20, justify="center", textvariable=usernameVar, fg="grey")
Username['font'] = helv12
Username.place(x=20, y=20, in_=LoginMenu)
Username.bind("<FocusIn>", handle_focusin_username)
Username.bind("<FocusOut>", handle_focusout_username)
Username.bind("<Return>", handle_enter_login)

# Password GUI
lockPass = IntVar()
lockPass.set(0)
passwordVal = StringVar()
passwordVal.set("password")
Password = Entry(LoginMenu, bd=2, width=20, justify="center", textvariable=passwordVal, fg="grey")
Password['font'] = helv12
Password.place(x=20,y=50, in_=LoginMenu)
Password.bind("<FocusIn>", handle_focusin_password)
Password.bind("<FocusOut>", handle_focusout_password)
Password.bind("<Return>", handle_enter_login)

# Login button
loginVer = IntVar()
loginVer.set(0)
LoginButton = tkinter.Button(LoginMenu, height = 1, width = 10, bg='cyan', text ="Login", command=adminCheck)
LoginButton['font'] = helv12
LoginButton.place(x=107, y=80, in_=LoginMenu)
LoginButton.bind("<Return>", handle_enter_login)

# Frame Data Pembatalan
# LogOut batal
LogoutButton = tkinter.Button(FrameDataPembatalan, height = 1, width = 10, bg='red', text ="Log Out", command=messageLogout)
LogoutButton['font'] = helv12
LogoutButton.place(x=420, y=10, in_=FrameDataPembatalan)

# ID Transaksi GUI
lockTrans = IntVar()
lockTrans.set(0)
IDTransaksiVar = StringVar()
IDTransaksiVar.set("ID Transaksi")
IDTransaksi = Entry(FrameDataPembatalan, bd=2, width=43, textvariable=IDTransaksiVar, fg="grey")
IDTransaksi['font'] = helv12
IDTransaksi.place(x=20,y=53, in_=FrameDataPembatalan)
IDTransaksi.bind("<FocusIn>", handle_focusin_idtransaksi)
IDTransaksi.bind("<FocusOut>", handle_focusout_idtransaksi)
IDTransaksi.bind("<Return>", handle_enter_search)

# Button Search
Search = tkinter.Button(FrameDataPembatalan, height = 1, width = 10, bg='white', text ="search", command=showDetailPemesanan)
Search['font'] = helv12
Search.place(x=420, y=50, in_=FrameDataPembatalan)

# Data Transaksi GUI
Nama = Label(FrameDataPembatalan, text="Nama                   :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
Nama['font'] = helv12
Nama.place(x=20, y=125, in_=FrameDataPembatalan)

NamaL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
NamaL['font'] = helv12
NamaL.place(x=145, y=125, in_=FrameDataPembatalan)

Email = Label(FrameDataPembatalan, text="Email                   :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
Email['font'] = helv12
Email.place(x=20, y=150, in_=FrameDataPembatalan)

EmailL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
EmailL['font'] = helv12
EmailL.place(x=145, y=150, in_=FrameDataPembatalan)

NomorRuangan = Label(FrameDataPembatalan, text="Nomor Ruangan :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
NomorRuangan['font'] = helv12
NomorRuangan.place(x=20, y=175, in_=FrameDataPembatalan)

NomorRuanganL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
NomorRuanganL['font'] = helv12
NomorRuanganL.place(x=145, y=175, in_=FrameDataPembatalan)

Tanggal = Label(FrameDataPembatalan, text="Tanggal               :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
Tanggal['font'] = helv12
Tanggal.place(x=20, y=200, in_=FrameDataPembatalan)

TanggalL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
TanggalL['font'] = helv12
TanggalL.place(x=145, y=200, in_=FrameDataPembatalan)

WaktuMasuk = Label(FrameDataPembatalan, text="Waktu Masuk      :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
WaktuMasuk['font'] = helv12
WaktuMasuk.place(x=20, y=225, in_=FrameDataPembatalan)

WaktuMasukL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
WaktuMasukL['font'] = helv12
WaktuMasukL.place(x=145, y=225, in_=FrameDataPembatalan)

Durasi = Label(FrameDataPembatalan, text="Durasi                  :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
Durasi['font'] = helv12
Durasi.place(x=20, y=250, in_=FrameDataPembatalan)

DurasiL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
DurasiL['font'] = helv12
DurasiL.place(x=145, y=250, in_=FrameDataPembatalan)

HargaAkhir = Label(FrameDataPembatalan, text="Harga Akhir        :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
HargaAkhir['font'] = helv12
HargaAkhir.place(x=20, y=275, in_=FrameDataPembatalan)

HargaAkhirL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
HargaAkhirL['font'] = helv12
HargaAkhirL.place(x=145, y=275, in_=FrameDataPembatalan)

StatusBayar = Label(FrameDataPembatalan, text="Status Bayar       :", anchor="nw", bg = "gray22", width=13, height=1, fg="white")
StatusBayar['font'] = helv12
StatusBayar.place(x=20, y=300, in_=FrameDataPembatalan)

StatusBayarL = Label(FrameDataPembatalan, anchor="nw", bg = "white", width=41, height=1, fg="black")
StatusBayarL['font'] = helv12
StatusBayarL.place(x=145, y=300, in_=FrameDataPembatalan)

# Button batal
BatalButton = tkinter.Button(FrameDataPembatalan, height = 1, width = 10, bg='red', text ="Batal", command=messageBatal)
BatalButton['font'] = helv12
BatalButton.place(x=420, y=350, in_=FrameDataPembatalan)

# Fitur 3: Pembayaran
# Akan menampilkan Menu Pembayaran dan Frame Pembayaran Ruangan bila ButtonPembayaran diclick
# Pembayaran Menu
ButtonPembayaranRuangan = tkinter.Button(PembayaranMenu, height = 2, width = 20, bg='cyan', text ="Ruangan", command=lambda:raise_frame(FramePembayaranRuangan))
ButtonPembayaranRuangan['font'] = helv12
ButtonPembayaranRuangan.place(x=20, y=20, in_=PembayaranMenu)

ButtonPembayaranMembership = tkinter.Button(PembayaranMenu, height = 2, width = 20, bg='cyan', text ="Membership",  command=lambda:raise_frame(FramePembayaranMembership))
ButtonPembayaranMembership['font'] = helv12
ButtonPembayaranMembership.place(x=20, y=90, in_=PembayaranMenu)

# Frame Pembayaran Ruangan
LabelEmailMember1 = Label(FramePembayaranRuangan, text="Email Member", bg="gray22", fg="white")
LabelEmailMember1["font"] = helv12
LabelEmailMember1.place(x=5, y=20, in_=FramePembayaranRuangan)

PilihanEmailMember1 = Entry(FramePembayaranRuangan, bd=2, width=23)
PilihanEmailMember1["font"] = helv12
PilihanEmailMember1.place(x=125,y=20,in_=FramePembayaranRuangan)

ButtonCari1 = tkinter.Button(FramePembayaranRuangan,height=1,width=10,bg="teal",text="Cari",command=cariRuangan)
ButtonCari1["font"] = helv14
ButtonCari1.place(x=5, y=60, in_=FramePembayaranRuangan)

cols_1 = ('Nomor Ruangan','Jenis Ruangan','Harga')
ListPembayaranRuangan = ttk.Treeview(FramePembayaranRuangan, columns=cols_1, show='headings')
for col in cols_1:
    ListPembayaranRuangan.heading(col, text=col)
ListPembayaranRuangan.column("Nomor Ruangan",width=130)
ListPembayaranRuangan.column("Jenis Ruangan",width=240)
ListPembayaranRuangan.column("Harga",width=170)
ListPembayaranRuangan.place(x=5,y=120, in_=FramePembayaranRuangan)


LabelTotal = Label(FramePembayaranRuangan, text="Total", bg="gray22",fg="white")
LabelTotal["font"] = helv12
LabelTotal.place(x=280,y=380, in_=FramePembayaranRuangan)

Total = Entry(FramePembayaranRuangan, bd=2, width=18,state="readonly")
Total["font"] = helv12
Total.place(x=380,y=380, in_=FramePembayaranRuangan)

LabelUang = Label(FramePembayaranRuangan, text="Uang", bg="gray22",fg="white")
LabelUang["font"] = helv12
LabelUang.place(x=280,y=430, in_=FramePembayaranRuangan)

Uang = Entry(FramePembayaranRuangan, bd=2, width=18)
Uang["font"] = helv12
Uang.place(x=380,y=430, in_=FramePembayaranRuangan)

ButtonGetKembalian = tkinter.Button(FramePembayaranRuangan,height=1,width=14, bg="pink", text="Hitung Kembalian",command=getKembalianRuangan)
ButtonGetKembalian['font']=helv10
ButtonGetKembalian.place(x=380,y=480, in_=FramePembayaranRuangan)

LabelKembalian = Label(FramePembayaranRuangan, text="Kembalian", bg="gray22",fg="white")
LabelKembalian["font"] = helv12
LabelKembalian.place(x=280,y=530, in_=FramePembayaranRuangan)

Kembalian = Entry(FramePembayaranRuangan, bd=2, width=18,state="readonly")
Kembalian["font"] = helv12
Kembalian.place(x=380,y=530, in_=FramePembayaranRuangan)

ButtonSelesai = tkinter.Button(FramePembayaranRuangan,height=1, width=10, bg="green",text="Selesai",command=selesaiRuangan)
ButtonSelesai["font"] = helv14
ButtonSelesai.place(x=50, y=530, in_=FramePembayaranRuangan)

# Frame Pembayaran Membership
LabelEmailMember = Label(FramePembayaranMembership, text="Email Member", bg="gray22", fg="white")
LabelEmailMember["font"] = helv12
LabelEmailMember.place(x=5, y=20, in_=FramePembayaranMembership)

PilihanEmailMember = Entry(FramePembayaranMembership, bd=2, width=23)
PilihanEmailMember["font"] = helv12
PilihanEmailMember.place(x=125,y=20,in_=FramePembayaranMembership)

ButtonCari = tkinter.Button(FramePembayaranMembership,height=1,width=10,bg="teal",text="Cari",command=cariMember)
ButtonCari["font"] = helv14
ButtonCari.place(x=5, y=60, in_=FramePembayaranMembership)

cols_2 = ('Email Member','Jenis Membership','Tanggal Jatuh Tempo','Harga')
ListPembayaranMember = ttk.Treeview(FramePembayaranMembership, columns=cols_2, show='headings')
for coll in cols_2:
    ListPembayaranMember.heading(coll, text=coll)
ListPembayaranMember.column("Email Member",width=100)
ListPembayaranMember.column("Jenis Membership",width=140)
ListPembayaranMember.column("Tanggal Jatuh Tempo",width=130)
ListPembayaranMember.column("Harga",width=170)
ListPembayaranMember.place(x=5,y=120, in_=FramePembayaranMembership)


LabelTotal1 = Label(FramePembayaranMembership, text="Total", bg="gray22",fg="white")
LabelTotal1["font"] = helv12
LabelTotal1.place(x=280,y=380, in_=FramePembayaranMembership)

Total1 = Entry(FramePembayaranMembership, bd=2, width=18,state="readonly")
Total1["font"] = helv12
Total1.place(x=380,y=380, in_=FramePembayaranMembership)

LabelUang1 = Label(FramePembayaranMembership, text="Uang", bg="gray22",fg="white")
LabelUang1["font"] = helv12
LabelUang1.place(x=280,y=430, in_=FramePembayaranMembership)

Uang1 = Entry(FramePembayaranMembership, bd=2, width=18)
Uang1["font"] = helv12
Uang1.place(x=380,y=430, in_=FramePembayaranMembership)

ButtonGetKembalian1 = tkinter.Button(FramePembayaranMembership,height=1,width=14, bg="pink", text="Hitung Kembalian",command=getKembalianMembership)
ButtonGetKembalian1['font']=helv10
ButtonGetKembalian1.place(x=380,y=480, in_=FramePembayaranMembership)

LabelKembalian1 = Label(FramePembayaranMembership, text="Kembalian", bg="gray22",fg="white")
LabelKembalian1["font"] = helv12
LabelKembalian1.place(x=280,y=530, in_=FramePembayaranMembership)

Kembalian1 = Entry(FramePembayaranMembership, bd=2, width=18,state="readonly")
Kembalian1["font"] = helv12
Kembalian1.place(x=380,y=530, in_=FramePembayaranMembership)

ButtonSelesai1 = tkinter.Button(FramePembayaranMembership,height=1, width=10, bg="green",text="Selesai",command=selesaiMembership)
ButtonSelesai1["font"] = helv14
ButtonSelesai1.place(x=50, y=530, in_=FramePembayaranMembership)

# Fitur 4: Pemesanan Ruangan
# Akan menampilkan Menu Pemesanan Ruangan dan Frame Pilih Waktu bila ButtonBookingPesanan diclick
# Pemesanan Ruangan Menu
ButtonPilihanWaktu = tkinter.Button(PemesananRuanganMenu, height = 2, width = 20, bg='cyan', text ="Pilih Waktu", command=lambda:raise_frame(FramePilihWaktu))
ButtonPilihanWaktu['font'] = helv12
ButtonPilihanWaktu.place(x=20, y=20, in_=PemesananRuanganMenu)

ButtonPilihanRuangan = tkinter.Button(PemesananRuanganMenu, height = 2, width = 20, bg='cyan', text ="Pilih Ruangan", command=lambda:raise_frame(FramePilihRuangan))
ButtonPilihanRuangan['font'] = helv12
ButtonPilihanRuangan.place(x=20, y=90, in_=PemesananRuanganMenu)

ButtonBiodataPemesan = tkinter.Button(PemesananRuanganMenu, height = 2, width = 20, bg='cyan', text ="Biodata", command=lambda:raise_frame(FrameBiodataPemesan))
ButtonBiodataPemesan['font'] = helv12
ButtonBiodataPemesan.place(x=20, y=160, in_=PemesananRuanganMenu)

# Frame Pilih Waktu
helv16 = tkinter.font.Font(family='Helvetica', size=16);

LabelBookingPesanan = Label(FramePilihWaktu, text="Booking Pesanan", bg = "gray22", fg= "white")
LabelBookingPesanan['font'] = tkinter.font.Font(family='Helvetica', size=16)
LabelBookingPesanan.place(x=355, y=20, in_=FramePilihWaktu)

LabelPilihanWaktu = Label(FramePilihWaktu, text="Pilihan Waktu", bg = "gray22", fg= "white")
LabelPilihanWaktu['font'] = tkinter.font.Font(family='Helvetica', size=16)
LabelPilihanWaktu.place(x=50, y=100, in_=FramePilihWaktu)

PilihanWaktuValues = [];
for i in range (11):
    value = str(i+10) + ":00";
    PilihanWaktuValues.append(value)

PilihanWaktuInfo = ttk.Combobox(FramePilihWaktu, values=PilihanWaktuValues, width = 22)
PilihanWaktuInfo['font'] = helv16
PilihanWaktuInfo.place(x=240, y=100, in_=FramePilihWaktu)

ButtonCekWaktu = tkinter.Button(FramePilihWaktu, height = 2, width = 10, bg='green', text ="Cek Waktu!", command=setWaktu)
ButtonCekWaktu['font'] = tkinter.font.Font(family='Helvetica', size=14)
ButtonCekWaktu.place(x=405, y=400, in_=FramePilihWaktu)

ButtonReset = tkinter.Button(FramePilihWaktu, height = 2, width = 10, bg='yellow', text ="Clear All", command=lambda:resetEntry("FramePilihWaktu"))
ButtonReset['font'] = tkinter.font.Font(family='Helvetica', size=14)
ButtonReset.place(x=265, y=400, in_=FramePilihWaktu)

# Frame Pilih Ruangan
LabelBookingPesanan = Label(FramePilihRuangan, text="Booking Pesanan", bg = "gray22", fg= "white")
LabelBookingPesanan['font'] = tkinter.font.Font(family='Helvetica', size=16)
LabelBookingPesanan.place(x=355, y=20, in_=FramePilihRuangan)

LabelPilihanRuangan = Label(FramePilihRuangan, text="Pilihan Ruangan", bg = "gray22", fg= "white")
LabelPilihanRuangan['font'] = tkinter.font.Font(family='Helvetica', size=16)
LabelPilihanRuangan.place(x=50, y=100, in_=FramePilihRuangan)

PilihanRuanganValues = [];
PilihanRuanganInfo = ttk.Combobox(FramePilihRuangan, values=PilihanRuanganValues, width = 22)
PilihanRuanganInfo['font'] = helv16
PilihanRuanganInfo.place(x=240, y=100, in_=FramePilihRuangan)

ButtonCekRuangan = tkinter.Button(FramePilihRuangan, height = 2, width = 10, bg='green', text ="Cek Ruangan", command=setRuangan)
ButtonCekRuangan['font'] = tkinter.font.Font(family='Helvetica', size=14)
ButtonCekRuangan.place(x=405, y=400, in_=FramePilihRuangan)

ButtonReset = tkinter.Button(FramePilihRuangan, height = 2, width = 10, bg='yellow', text ="Clear All", command=lambda:resetEntry("FramePilihRuangan"))
ButtonReset['font'] = tkinter.font.Font(family='Helvetica', size=14)
ButtonReset.place(x=265, y=400, in_=FramePilihRuangan)

# Frame Biodata Pemesan
LabelBookingPesanan = Label(FrameBiodataPemesan, text="Booking Pesanan", bg = "gray22", fg= "white")
LabelBookingPesanan['font'] = helv16
LabelBookingPesanan.place(x=355, y=20, in_=FrameBiodataPemesan)

LabelPilihanWaktu = Label(FrameBiodataPemesan, text="Pilihan Waktu", bg = "gray22", fg= "white")
LabelPilihanWaktu['font'] = helv16
LabelPilihanWaktu.place(x=50, y=100, in_=FrameBiodataPemesan)

PilihanWaktuReadInfo = Entry(FrameBiodataPemesan, bd =2, width = 23, state='readonly')
PilihanWaktuReadInfo['font'] = helv16
PilihanWaktuReadInfo.place(x=240, y=100, in_=FrameBiodataPemesan)

LabelPilihanRuangan = Label(FrameBiodataPemesan, text="Pilihan Ruangan", bg = "gray22", fg= "white")
LabelPilihanRuangan['font'] = helv16
LabelPilihanRuangan.place(x=50, y=145, in_=FrameBiodataPemesan)

PilihanRuanganReadInfo = Entry(FrameBiodataPemesan, bd =2, width = 23, state='readonly')
PilihanRuanganReadInfo['font'] = helv16
PilihanRuanganReadInfo.place(x=240, y=145, in_=FrameBiodataPemesan)

LabelNamaPemesan = Label(FrameBiodataPemesan, text="Nama Pemesan", bg = "gray22", fg= "white")
LabelNamaPemesan['font'] = helv16
LabelNamaPemesan.place(x=50, y=190, in_=FrameBiodataPemesan)

NamaPemesanInfo = Entry(FrameBiodataPemesan, bd =2, width = 23)
NamaPemesanInfo['font'] = helv16
NamaPemesanInfo.place(x=240, y=190, in_=FrameBiodataPemesan)

LabelAlamatPemesan = Label(FrameBiodataPemesan, text="Alamat", bg = "gray22", fg= "white")
LabelAlamatPemesan['font'] = helv16
LabelAlamatPemesan.place(x=50, y=235, in_=FrameBiodataPemesan)

AlamatPemesanInfo = Entry(FrameBiodataPemesan, bd =2, width = 23)
AlamatPemesanInfo['font'] = helv16
AlamatPemesanInfo.place(x=240, y=235, in_=FrameBiodataPemesan)

LabelNomorTelepon = Label(FrameBiodataPemesan, text="Nomor Telepon", bg = "gray22", fg= "white")
LabelNomorTelepon['font'] = helv16
LabelNomorTelepon.place(x=50, y=280, in_=FrameBiodataPemesan)

NomorTeleponInfo = Entry(FrameBiodataPemesan, bd =2, width = 23)
NomorTeleponInfo['font'] = helv16
NomorTeleponInfo.place(x=240, y=280, in_=FrameBiodataPemesan)

LabelEmailAddress = Label(FrameBiodataPemesan, text="Email Address", bg = "gray22", fg= "white")
LabelEmailAddress['font'] = helv16
LabelEmailAddress.place(x=50, y=325, in_=FrameBiodataPemesan)

EmailAddressInfo = Entry(FrameBiodataPemesan, bd =2, width = 23)
EmailAddressInfo['font'] = helv16
EmailAddressInfo.place(x=240, y=325, in_=FrameBiodataPemesan)

ButtonBookNow = tkinter.Button(FrameBiodataPemesan, height = 2, width = 10, bg='green', text ="Book Now!", command=lambda:bookingRuangan())
ButtonBookNow['font'] = helv14
ButtonBookNow.place(x=405, y=400, in_=FrameBiodataPemesan)

ButtonClearInfo = tkinter.Button(FrameBiodataPemesan, height = 2, width = 10, bg='yellow', text ="Clear All", command=lambda:resetEntry("FrameBiodataPemesan"))
ButtonClearInfo['font'] = helv14
ButtonClearInfo.place(x=265, y=400, in_=FrameBiodataPemesan)

# Fitur 5: Membership
# Menampilkan objek-objek yang akan ditampilkan pada bagian Membership
# Akan ditampilkan bila ButtonMembership pada RootMenu diclick
# Frame Membership
LabelMembership = Label(FrameMembership, text="Daftar Member Baru", bg = "gray22", fg= "white")
LabelMembership['font'] = helv16
LabelMembership.place(x=340, y=20, in_=FrameMembership)

LabelEmailAddressMember = Label(FrameMembership, text="Email Address", bg = "gray22", fg= "white")
LabelEmailAddressMember['font'] = helv16
LabelEmailAddressMember.place(x=50, y=100, in_=FrameMembership)

EmailAddressMemberInfo = Entry(FrameMembership, bd =2, width = 23)
EmailAddressMemberInfo['font'] = helv16
EmailAddressMemberInfo.place(x=240, y=100, in_=FrameMembership)

LabelNamaCaMember = Label(FrameMembership, text="Nama Member", bg = "gray22", fg= "white")
LabelNamaCaMember['font'] = helv16
LabelNamaCaMember.place(x=50, y=145, in_=FrameMembership)

NamaCaMemberInfo = Entry(FrameMembership, bd =2, width = 23)
NamaCaMemberInfo['font'] = helv16
NamaCaMemberInfo.place(x=240, y=145, in_=FrameMembership)

LabelUmurCaMember = Label(FrameMembership, text="Umur", bg = "gray22", fg= "white")
LabelUmurCaMember['font'] = helv16
LabelUmurCaMember.place(x=50, y=190, in_=FrameMembership)

UmurCaMemberInfo = Entry(FrameMembership, bd =2, width = 23)
UmurCaMemberInfo['font'] = helv16
UmurCaMemberInfo.place(x=240, y=190, in_=FrameMembership)

LabelAlamatCaMember = Label(FrameMembership, text="Alamat", bg = "gray22", fg= "white")
LabelAlamatCaMember['font'] = helv16
LabelAlamatCaMember.place(x=50, y=235, in_=FrameMembership)

AlamatCaMemberInfo = Entry(FrameMembership, bd =2, width = 23)
AlamatCaMemberInfo['font'] = helv16
AlamatCaMemberInfo.place(x=240, y=235, in_=FrameMembership)

LabelNomorTeleponCaMember = Label(FrameMembership, text="Nomor Telepon", bg = "gray22", fg= "white")
LabelNomorTeleponCaMember['font'] = helv16
LabelNomorTeleponCaMember.place(x=50, y=280, in_=FrameMembership)

NomorTeleponCaMemberInfo = Entry(FrameMembership, bd =2, width = 23)
NomorTeleponCaMemberInfo['font'] = helv16
NomorTeleponCaMemberInfo.place(x=240, y=280, in_=FrameMembership)

LabelPilihanMember = Label(FrameMembership, text="Paket Membership", bg = "gray22", fg= "white")
LabelPilihanMember['font'] = helv16
LabelPilihanMember.place(x=50, y=325, in_=FrameMembership)

PilihanMemberValues = []
PilihanMemberValues.append("--Membership--") #placeholder
PilihanMemberValues.append("Gold")
PilihanMemberValues.append("Silver")
PilihanMemberValues.append("Bronze")

PilihanMembernInfo = ttk.Combobox(FrameMembership, values=PilihanMemberValues, height = 5, width = 22)
PilihanMembernInfo['font'] = helv16
PilihanMembernInfo.place(x=240, y=325, in_=FrameMembership)
PilihanMembernInfo.current(0)

ButtonSubmit = tkinter.Button(FrameMembership, height = 2, width = 10, bg='green', text ="Submit", command=SubmitMember)
ButtonSubmit['font'] = helv14
ButtonSubmit.place(x=405, y=370, in_=FrameMembership)

ButtonClearInfo = tkinter.Button(FrameMembership, height = 2, width = 10, bg='yellow', text ="Clear All", command=lambda:resetFrameMember("FrameMembership"))
ButtonClearInfo['font'] = helv14
ButtonClearInfo.place(x=265, y=370, in_=FrameMembership)

# Bangkitkan Frame Awal
raise_frame(RootMenu)
raise_frame(PengolahanRuanganMenu)
raise_frame(FrameEmailLogin)
root.resizable(0,0)
root.mainloop()