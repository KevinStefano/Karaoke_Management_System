# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog
from PIL import ImageTk, Image
from frame import *
from pengolahanruangan import *

verifikasi=0


def checkEmailPassword():
    user = PilihanEmail.get()
    pasw = PilihanPassword.get()
    global verifikasi 
    verifikasi= isInDataAdmin(user,pasw)
    if verifikasi==0:
        ErrorEmailMessage()
    else:
        EmailMessageVerif()

def ErrorEmailMessage(): 
    messagebox.showerror("Error", "Email anda belom terverifikasi")

def EmailMessageVerif():
    messagebox.showinfo("Information","YEAY... Email terkonfirmasi, silahkan lakukan penambahan ruangan atau penghapusan ruangan")

def ErrorTambahRuanganMessage(): 
    messagebox.showerror("Error", "Tipe Ruangan sudah ada")

def NoErorTambahRuanganMessage():
    messagebox.showinfo("Information","YEAY... Tipe Ruangan berhasil ditambahkan")

   
def tambahRuangan():
    tipe_ = PilihanTipeRuangan.get()
    kap_ = PilihanKapasitas.get()
    hargabiasa_ = PilihanHargaBiasa.get()
    hargadiskon_ = PilihanHargaDiskon.get()
    print(tipe_)
    print(kap_)
    print(hargabiasa_)
    print(hargadiskon_)
    updateTableJenisRuangan(tipe_,kap_,hargabiasa_,hargadiskon_)
    NoErorTambahRuanganMessage()

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
middleMenu = Frame(root, height = 768, width = 230, bg = "gray32")
rightMenu = Frame(root, height = 768, width = 554, bg = "gray22")
rightMenu2 = Frame(root, height = 768, width = 554, bg = "gray22")
rightMenu3 = Frame(root, height = 768, width = 554, bg = "gray22")
leftMenu.grid(row=1, column=0, sticky='news')
middleMenu.grid(row = 1, column = 1, sticky='news')
rightMenu.grid(row = 1, column = 2, sticky='news')
rightMenu2.grid(row = 1, column = 2, sticky='news')
rightMenu3.grid(row = 1, column = 2, sticky='news')

# BUTTON-BUTTON UTAMA : MatchUp, Reset, Quit, Next
ButtonPengolahanRuangan = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Pengolahan Ruangan" , command=lambda:raise_frame(rightMenu))
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
ButtonPenambahanRuangan = tkinter.Button(middleMenu, height = 2, width = 20, bg='cyan', text ="Penambahan", command=lambda:raise_frame(rightMenu2) if verifikasi==1 else ErrorEmailMessage())
ButtonPenambahanRuangan['font'] = helv12
ButtonPenambahanRuangan.place(x=20, y=20, in_=middleMenu)

ButtonPenghapusanRuangan = tkinter.Button(middleMenu, height = 2, width = 20, bg='cyan', text ="Penghapusan",  command=lambda:raise_frame(rightMenu3) if verifikasi==1 else ErrorEmailMessage())
ButtonPenghapusanRuangan['font'] = helv12
ButtonPenghapusanRuangan.place(x=20, y=90, in_=middleMenu)

# Right Menu
LabelNamaUser = Label(rightMenu, text="Nama User", bg = "gray22", fg= "white")
LabelNamaUser['font'] = helv16
LabelNamaUser.place(x=355, y=20, in_=rightMenu)

LabelEmail= Label(rightMenu, text="Email", bg = "gray22", fg= "white")
LabelEmail['font'] = helv16
LabelEmail.place(x=50, y=145, in_=rightMenu)

PilihanEmail = Entry(rightMenu, bd =2, width = 23)
PilihanEmail['font'] = helv16
PilihanEmail.place(x=240, y=145, in_=rightMenu)


LabelPassword= Label(rightMenu, text="Password", bg = "gray22", fg= "white")
LabelPassword['font'] = helv16
LabelPassword.place(x=50, y=190, in_=rightMenu)

PilihanPassword = Entry(rightMenu, bd =2, width = 23,show="*")
PilihanPassword['font'] = helv16
PilihanPassword.place(x=240, y=190, in_=rightMenu)


ButtonOK = tkinter.Button(rightMenu, height = 2, width = 10, bg='green', text ="OK", command = checkEmailPassword)
ButtonOK['font'] = helv14
ButtonOK.place(x=405, y=400, in_=rightMenu)


ButtonClearInfo1 = tkinter.Button(rightMenu, height = 2, width = 10, bg='yellow', text ="Clear")
ButtonClearInfo1['font'] = helv14
ButtonClearInfo1.place(x=265, y=400, in_=rightMenu)




#RightMenu2

LabelTipeRuangan = Label(rightMenu2, text="Tipe Ruangan", bg = "gray22", fg= "white")
LabelTipeRuangan ['font'] = helv16
LabelTipeRuangan.place(x=50, y=145, in_=rightMenu2)

PilihanTipeRuangan = Entry(rightMenu2, bd =2, width = 23)
PilihanTipeRuangan['font'] = helv16
PilihanTipeRuangan.place(x=240, y=145, in_=rightMenu2)


LabelKapasitas= Label(rightMenu2, text="Kapasitas", bg = "gray22", fg= "white")
LabelKapasitas['font'] = helv16
LabelKapasitas.place(x=50, y=190, in_=rightMenu2)

PilihanKapasitas = Entry(rightMenu2, bd =2, width = 23)
PilihanKapasitas['font'] = helv16
PilihanKapasitas.place(x=240, y=190, in_=rightMenu2)

LabelHargaBiasa= Label(rightMenu2, text="Harga Biasa", bg = "gray22", fg= "white")
LabelHargaBiasa['font'] = helv16
LabelHargaBiasa.place(x=50, y=235, in_=rightMenu2)

PilihanHargaBiasa = Entry(rightMenu2, bd =2, width = 23)
PilihanHargaBiasa['font'] = helv16
PilihanHargaBiasa.place(x=240, y=235, in_=rightMenu2)

LabelHargaDiskon= Label(rightMenu2, text="Harga Diskon", bg = "gray22", fg= "white")
LabelHargaDiskon['font'] = helv16
LabelHargaDiskon.place(x=50, y=280, in_=rightMenu2)

PilihanHargaDiskon = Entry(rightMenu2, bd =2, width = 23)
PilihanHargaDiskon['font'] = helv16
PilihanHargaDiskon.place(x=240, y=280, in_=rightMenu2)


ButtonAdd= tkinter.Button(rightMenu2, height = 2, width = 10, bg='green', text ="Add!", command = tambahRuangan)
ButtonAdd['font'] = helv14
ButtonAdd.place(x=405, y=400, in_=rightMenu2)

ButtonClearInfo2 = tkinter.Button(rightMenu2, height = 2, width = 10, bg='yellow', text ="Clear")
ButtonClearInfo2['font'] = helv14
ButtonClearInfo2.place(x=265, y=400, in_=rightMenu2)



#RightMenu3

LabelTipeRuanganHapus = Label(rightMenu3, text="Tipe Ruangan", bg = "gray22", fg= "white")
LabelTipeRuanganHapus ['font'] = helv16
LabelTipeRuanganHapus.place(x=50, y=145, in_=rightMenu3)

PilihanTipeRuanganHapus = Entry(rightMenu3, bd =2, width = 23)
PilihanTipeRuanganHapus['font'] = helv16
PilihanTipeRuanganHapus.place(x=240, y=145, in_=rightMenu3)

ButtonHapus = tkinter.Button(rightMenu3, height = 2, width = 10, bg='red', text ="Hapus")
ButtonHapus['font'] = helv14
ButtonHapus.place(x=405, y=400, in_=rightMenu3)


raise_frame(rightMenu3)
raise_frame(rightMenu2)
raise_frame(rightMenu)

root.resizable(0,0)
root.mainloop()