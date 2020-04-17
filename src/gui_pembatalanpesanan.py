# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pembatalan Pesanan

# Import Library yang kira-kira perlu
from tkinter import *
from tkinter import messagebox
from pembatalanpesanan import *
import tkinter.font
import tkinter.filedialog

def raise_frame(frame):
    frame.tkraise()

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

# Frame-Frame dalam GUI
# Root Menu
RootMenu = Frame(root, height = 768, width = 240, bg = "gray22")
RootMenu.grid(row=1, column=0, sticky='news')

# Middle Menu
LoginMenu = Frame(root, height = 768, width = 230, bg = "gray32")
LoginMenu.grid(row = 1, column = 1, sticky='news')

# Right Menu
FrameDataPembatalan = Frame(root, height = 768, width = 554, bg = "gray22")
FrameDataPembatalan.grid(row = 1, column = 2, sticky='news')

FrameLogin = Frame(root, height = 768, width = 554, bg = "gray22")
FrameLogin.grid(row = 1, column = 2, sticky='news')

# BUTTON-BUTTON UTAMA : MatchUp, Reset, Quit, Next
ButtonPengolahanRuangan = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Pengolahan Ruangan")
ButtonPengolahanRuangan['font'] = helv12
ButtonPengolahanRuangan.place(x=30, y=20, in_=RootMenu)

ButtonPembatalanPaksa = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Pembatalan Paksa")
ButtonPembatalanPaksa['font'] = helv12
ButtonPembatalanPaksa.place(x=30, y=90, in_=RootMenu)

ButtonPembayaran = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Pembayaran")
ButtonPembayaran['font'] = helv12
ButtonPembayaran.place(x=30, y=160, in_=RootMenu)

ButtonPemesanan = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Booking Ruangan")
ButtonPemesanan['font'] = helv12
ButtonPemesanan.place(x=30, y=230, in_=RootMenu)

ButtonMembership = tkinter.Button(RootMenu, height = 2, width = 20, bg='green yellow', text ="Membership")
ButtonMembership['font'] = helv12
ButtonMembership.place(x=30, y=300, in_=RootMenu)

# FRAME MIDDLE MENU
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

raise_frame(FrameLogin)

root.resizable(0,0)
root.mainloop()