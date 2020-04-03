# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

from tkinter import *
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog
from PIL import ImageTk, Image
from frame import *

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
leftMenu.grid(row=1, column=0, sticky='news')
middleMenu.grid(row = 1, column = 1, sticky='news')
rightMenu.grid(row = 1, column = 2, sticky='news')
FramePilihWaktu = Frame(root, height = 768, width = 554, bg = "gray22")
FramePilihWaktu.grid(row = 1, column = 2, sticky='news')

LoadFrame(FramePilihWaktu)

# BUTTON-BUTTON UTAMA : MatchUp, Reset, Quit, Next
ButtonPengolahanRuangan = tkinter.Button(leftMenu, height = 2, width = 20, bg='green yellow', text ="Pengolahan Ruangan")
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
ButtonPilihanWaktu = tkinter.Button(middleMenu, height = 2, width = 20, bg='cyan', text ="Pilih Waktu", command=lambda:raise_frame(FramePilihWaktu))
ButtonPilihanWaktu['font'] = helv12
ButtonPilihanWaktu.place(x=20, y=20, in_=middleMenu)

ButtonPilihanRuangan = tkinter.Button(middleMenu, height = 2, width = 20, bg='cyan', text ="Pilih Ruangan")
ButtonPilihanRuangan['font'] = helv12
ButtonPilihanRuangan.place(x=20, y=90, in_=middleMenu)

ButtonBiodataPemesan = tkinter.Button(middleMenu, height = 2, width = 20, bg='cyan', text ="Biodata", command=lambda:raise_frame(rightMenu))
ButtonBiodataPemesan['font'] = helv12
ButtonBiodataPemesan.place(x=20, y=160, in_=middleMenu)

# Right Menu
LabelBookingPesanan = Label(rightMenu, text="Booking Pesanan", bg = "gray22", fg= "white")
LabelBookingPesanan['font'] = helv16
LabelBookingPesanan.place(x=355, y=20, in_=rightMenu)

LabelPilihanWaktu = Label(rightMenu, text="Pilihan Waktu", bg = "gray22", fg= "white")
LabelPilihanWaktu['font'] = helv16
LabelPilihanWaktu.place(x=50, y=100, in_=rightMenu)

PilihanWaktuInfo = Entry(rightMenu, bd =2, width = 23)
PilihanWaktuInfo['font'] = helv16
PilihanWaktuInfo.place(x=240, y=100, in_=rightMenu)

LabelPilihanRuangan = Label(rightMenu, text="Pilihan Ruangan", bg = "gray22", fg= "white")
LabelPilihanRuangan['font'] = helv16
LabelPilihanRuangan.place(x=50, y=145, in_=rightMenu)

PilihanRuanganInfo = Entry(rightMenu, bd =2, width = 23)
PilihanRuanganInfo['font'] = helv16
PilihanRuanganInfo.place(x=240, y=145, in_=rightMenu)

LabelNamaPemesan = Label(rightMenu, text="Nama Pemesan", bg = "gray22", fg= "white")
LabelNamaPemesan['font'] = helv16
LabelNamaPemesan.place(x=50, y=190, in_=rightMenu)

NamaPemesanInfo = Entry(rightMenu, bd =2, width = 23)
NamaPemesanInfo['font'] = helv16
NamaPemesanInfo.place(x=240, y=190, in_=rightMenu)

LabelAlamatPemesan = Label(rightMenu, text="Alamat", bg = "gray22", fg= "white")
LabelAlamatPemesan['font'] = helv16
LabelAlamatPemesan.place(x=50, y=235, in_=rightMenu)

AlamatPemesanInfo = Entry(rightMenu, bd =2, width = 23)
AlamatPemesanInfo['font'] = helv16
AlamatPemesanInfo.place(x=240, y=235, in_=rightMenu)

LabelNomorTelepon = Label(rightMenu, text="Nomor Telepon", bg = "gray22", fg= "white")
LabelNomorTelepon['font'] = helv16
LabelNomorTelepon.place(x=50, y=280, in_=rightMenu)

NomorTeleponInfo = Entry(rightMenu, bd =2, width = 23)
NomorTeleponInfo['font'] = helv16
NomorTeleponInfo.place(x=240, y=280, in_=rightMenu)

LabelEmailAddress = Label(rightMenu, text="Email Address", bg = "gray22", fg= "white")
LabelEmailAddress['font'] = helv16
LabelEmailAddress.place(x=50, y=325, in_=rightMenu)

EmailAddressInfo = Entry(rightMenu, bd =2, width = 23)
EmailAddressInfo['font'] = helv16
EmailAddressInfo.place(x=240, y=325, in_=rightMenu)

ButtonBookNow = tkinter.Button(rightMenu, height = 2, width = 10, bg='green', text ="Book Now!")
ButtonBookNow['font'] = helv14
ButtonBookNow.place(x=405, y=400, in_=rightMenu)

ButtonClearInfo = tkinter.Button(rightMenu, height = 2, width = 10, bg='yellow', text ="Clear All")
ButtonClearInfo['font'] = helv14
ButtonClearInfo.place(x=265, y=400, in_=rightMenu)

raise_frame(rightMenu)
root.resizable(0,0)
root.mainloop()