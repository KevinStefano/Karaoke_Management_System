# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

# Import Library
from tkinter import *
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog
from tkinter import ttk
from bookingpesanan import *

# raise_frame -> Membangkitkan frame selanjutnya untuk menggantikan frame sebelumnya
def raise_frame(frame):
    frame.tkraise()

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
    isValid = True
    for entry in (PilihanWaktuReadInfo, PilihanRuanganReadInfo, NamaPemesanInfo, AlamatPemesanInfo, NomorTeleponInfo):
        if (len(entry.get()) == 0):
            isValid = False
            break
    if (isValid):
        bookNow(PilihanWaktuReadInfo, PilihanRuanganReadInfo, NamaPemesanInfo, AlamatPemesanInfo, NomorTeleponInfo, EmailAddressInfo)
        resetEntry("FrameBiodataPemesan")
    else:
        messagebox.showerror("Error", "Masih terdapat entri yang kosong")

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
RootMenu = Frame(root, height = 768, width = 240, bg = "gray22")
RootMenu.grid(row=1, column=0, sticky='news')

PemesananRuanganMenu = Frame(root, height = 768, width = 230, bg = "gray32")
PemesananRuanganMenu.grid(row = 1, column = 1, sticky='news')

FrameBiodataPemesan = Frame(root, height = 768, width = 554, bg = "gray22")
FrameBiodataPemesan.grid(row = 1, column = 2, sticky='news')

FramePilihWaktu = Frame(root, height = 768, width = 554, bg = "gray22")
FramePilihWaktu.grid(row = 1, column = 2, sticky='news')

FramePilihRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePilihRuangan.grid(row = 1, column = 2, sticky='news')

# Root Menu
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

ButtonBookNow = tkinter.Button(FrameBiodataPemesan, height = 2, width = 10, bg='green', text ="Book Now!", 
                command=bookingRuangan)
ButtonBookNow['font'] = helv14
ButtonBookNow.place(x=405, y=400, in_=FrameBiodataPemesan)

ButtonClearInfo = tkinter.Button(FrameBiodataPemesan, height = 2, width = 10, bg='yellow', text ="Clear All", command=lambda:resetEntry("FrameBiodataPemesan"))
ButtonClearInfo['font'] = helv14
ButtonClearInfo.place(x=265, y=400, in_=FrameBiodataPemesan)

# Bangkitkan Frame Awal
raise_frame(FrameBiodataPemesan)
root.resizable(0,0)
root.mainloop()