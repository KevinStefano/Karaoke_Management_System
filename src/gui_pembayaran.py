# TEMPLATE GUI UNTUK SETIAP BAGIAN

# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

# Import Library yang kira-kira perlu
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pembayaran import *
import tkinter.font
import tkinter.filedialog


# Global Var
current_id_pesanan = 0
current_harga = 0

def raise_frame(frame):
    frame.tkraise()

# Fungsi untuk mencari dari tabel daftar pemesanan berdasarkan nomor ruangan
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

# Fungsi untuk mencari seorang member dari tabel membership
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

# Fungsi untuk menghitung harga berdasarkan paket membership
def cariHarga(jenisMembership):
    if(jenisMembership == "Bronze"):
        return 1000000
    elif(jenisMembership == "Silver"):
        return 1500000
    else:
        return 2000000

# Fungsi untuk mengupdate tabel daftar pemesanan setelah pembayaran berhasil dilakukan
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

# Fungsi untuk mengupdate tabel pembayaran membership setelah pembayaran untuk iuran membership berhasil dilakukan
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

# Fungsi untuk menghitung kembalian di frame Ruangan
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

# Fungsi untuk menghitung kembalian di frame Membership
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

PembayaranMenu = Frame(root, height = 768, width = 230, bg = "gray32")
PembayaranMenu.grid(row = 1, column = 1, sticky='news')

FramePembayaranRuangan = Frame(root, height = 768, width = 554, bg = "gray22")
FramePembayaranRuangan.grid(row = 1, column = 2, sticky='news')

FramePembayaranMembership = Frame(root, height = 768, width = 554, bg = "gray22")
FramePembayaranMembership.grid(row = 1, column = 2, sticky='news')


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

ButtonPembayaranRuangan = tkinter.Button(PembayaranMenu, height = 2, width = 20, bg='cyan', text ="Ruangan", command=lambda:raise_frame(FramePembayaranRuangan))
ButtonPembayaranRuangan['font'] = helv12
ButtonPembayaranRuangan.place(x=20, y=20, in_=PembayaranMenu)

ButtonPembayaranMembership = tkinter.Button(PembayaranMenu, height = 2, width = 20, bg='cyan', text ="Membership",  command=lambda:raise_frame(FramePembayaranMembership))
ButtonPembayaranMembership['font'] = helv12
ButtonPembayaranMembership.place(x=20, y=90, in_=PembayaranMenu)


# Frame Ruangan
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

# Frame Membership
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

raise_frame(FramePembayaranRuangan)

root.resizable(0,0)
root.mainloop()