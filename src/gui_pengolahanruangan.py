# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog
from PIL import ImageTk, Image
from pengolahanruangan import *

verifikasi=0
username = 'null'

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
leftMenu = Frame(root, height = 768, width = 240, bg = "gray22")
PengolahanRuanganMenu = Frame(root, height = 768, width = 230, bg = "gray32")
FrameEmailLogin = Frame(root, height = 768, width = 554, bg = "gray22")
FramePenambahanRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePenghapusanRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
leftMenu.grid(row=1, column=0, sticky='news')
PengolahanRuanganMenu.grid(row = 1, column = 1, sticky='news')
FrameEmailLogin.grid(row = 1, column = 2, sticky='news')
FramePenambahanRuangan.grid(row = 1, column = 2, sticky='news')
FramePenghapusanRuangan.grid(row = 1, column = 2, sticky='news')

# BUTTON-BUTTON UTAMA : MatchUp, Reset, Quit, Next
ButtonPengolahanRuangan = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Pengolahan Ruangan" , command=lambda:(FrameEmailLogin).tkraise())
ButtonPengolahanRuangan['font'] = helv12
ButtonPengolahanRuangan.place(x=30, y=20, in_=leftMenu)

ButtonPembatalanPaksa = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Pembatalan Paksa")
ButtonPembatalanPaksa['font'] = helv12
ButtonPembatalanPaksa.place(x=30, y=90, in_=leftMenu)

ButtonPembayaran = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Pembayaran")
ButtonPembayaran['font'] = helv12
ButtonPembayaran.place(x=30, y=160, in_=leftMenu)

ButtonPemesanan = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Booking Ruangan")
ButtonPemesanan['font'] = helv12
ButtonPemesanan.place(x=30, y=230, in_=leftMenu)

ButtonMembership = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Membership")
ButtonMembership['font'] = helv12
ButtonMembership.place(x=30, y=300, in_=leftMenu)

# Middle Menu
ButtonPenambahanRuangan = tkinter.Button(PengolahanRuanganMenu, height = 2, width = 20, bg='cyan', text ="Penambahan", command=lambda:(FramePenambahanRuangan).tkraise() if verifikasi==1 else ErrorEmailMessage())
ButtonPenambahanRuangan['font'] = helv12
ButtonPenambahanRuangan.place(x=20, y=20, in_=PengolahanRuanganMenu)

ButtonPenghapusanRuangan = tkinter.Button(PengolahanRuanganMenu, height = 2, width = 20, bg='cyan', text ="Penghapusan",  command=lambda:(FramePenghapusanRuangan).tkraise() if verifikasi==1 else ErrorEmailMessage())
ButtonPenghapusanRuangan['font'] = helv12
ButtonPenghapusanRuangan.place(x=20, y=90, in_=PengolahanRuanganMenu)

# Right Menu
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


#FramePenambahanRuangan

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


#FramePenghapusanRuangan

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


FramePenghapusanRuangan.tkraise()
FramePenambahanRuangan.tkraise()
FrameEmailLogin.tkraise()

root.resizable(0,0)
root.mainloop()