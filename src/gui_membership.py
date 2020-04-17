# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Membership

# Import Library
from tkinter import *
from tkinter import messagebox
import tkinter.font
import tkinter.filedialog
from tkinter import ttk
from membership import *

def raise_frame(frame):
    frame.tkraise()

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
    time = datetime.now() + timedelta(days=30)
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
        updateTableMembership(email, nama, umur, alamat, notelp, paket, time)
        messagebox.showinfo("Information","Member baru berhasil ditambahkan")
        resetFrameMember("FrameMembership")


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
TemplateMenu = Frame(root, height = 768, width = 230, bg = "gray32")
TemplateMenu.grid(row = 1, column = 1, sticky='news')

# Right Menu
# ======================================================================
# TO DO: Sesuaikan FrameMenu1, FrameMembership dst nya dengan bagian kalian
#        Gunakan format yang sama sesuai dengan contoh FrameMenu
# ======================================================================
FrameMembership = Frame(root, height = 768, width = 554, bg = "gray22")
FrameMembership.grid(row = 1, column = 2, sticky='news')

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
# ======================================================================
# TO DO: Sesuaikan ButtonMenu1, ButtonMenu2 dst nya dengan bagian kalian
#        Gunakan format yang sama sesuai dengan contoh ButtonMenu
# ======================================================================
'''ButtonMenu1 = tkinter.Button(TemplateMenu, height = 2, width = 20, bg='cyan', text ="Penambahan", command=lambda:raise_frame(FrameMenu1))
ButtonMenu1['font'] = helv12
ButtonMenu1.place(x=20, y=20, in_=TemplateMenu)

ButtonMenu2 = tkinter.Button(TemplateMenu, height = 2, width = 20, bg='cyan', text ="Penghapusan",  command=lambda:raise_frame(FrameMembership))
ButtonMenu2['font'] = helv12
ButtonMenu2.place(x=20, y=90, in_=TemplateMenu)
'''
# FRAME RIGHT MENU
# ======================================================================
# TO DO: Implementasikan setiap frame dari FrameMenu1, FrameMembership, dst
# ======================================================================
# Frame Menu
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

# Ada yang bangkit tapi Frame Awal
raise_frame(FrameMembership)
root.resizable(0,0)
root.mainloop()