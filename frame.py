# Karaoke Management System
# IF2250 - Rekayasa Perangkat Lunak
# K2 - Kelompok 11 - Modul Pemesanan Ruangan

from tkinter import *
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog

def raise_frame(frame):
    frame.tkraise()

# Frame-Frame dalam GUI
def LoadFrame(FramePilihWaktu):
    # Objek-objek dalam FramePilihWaktu
    LabelBookingPesanan = Label(FramePilihWaktu, text="Booking Pesanan", bg = "gray22", fg= "white")
    LabelBookingPesanan['font'] = tkinter.font.Font(family='Helvetica', size=16)
    LabelBookingPesanan.place(x=355, y=20, in_=FramePilihWaktu)

    LabelPilihanWaktu = Label(FramePilihWaktu, text="Pilihan Waktu", bg = "gray22", fg= "white")
    LabelPilihanWaktu['font'] = tkinter.font.Font(family='Helvetica', size=16)
    LabelPilihanWaktu.place(x=50, y=100, in_=FramePilihWaktu)

    PilihanWaktuInfo = Entry(FramePilihWaktu, bd =2, width = 23)
    PilihanWaktuInfo['font'] = tkinter.font.Font(family='Helvetica', size=16)
    PilihanWaktuInfo.place(x=240, y=100, in_=FramePilihWaktu)

    var1 = IntVar()
    Checkbox11 = Checkbutton(FramePilihWaktu, variable = var1, text="11.00", bg = "gray22", fg= "white")
    Checkbox11['font'] = tkinter.font.Font(family='Helvetica', size=14)
    Checkbox11.place(x=60, y=150, in_=FramePilihWaktu)

    Checkbox12 = Checkbutton(FramePilihWaktu, variable = var1, text="12.00", bg = "gray22", fg= "white")
    Checkbox12['font'] = tkinter.font.Font(family='Helvetica', size=14)
    Checkbox12.place(x=60, y=180, in_=FramePilihWaktu)

    Checkbox13 = Checkbutton(FramePilihWaktu, variable = var1, text="13.00", bg = "gray22", fg= "white")
    Checkbox13['font'] = tkinter.font.Font(family='Helvetica', size=14)
    Checkbox13.place(x=60, y=210, in_=FramePilihWaktu)
    
    ButtonCekWaktu = tkinter.Button(FramePilihWaktu, height = 2, width = 10, bg='green', text ="Book Now!")
    ButtonCekWaktu['font'] = tkinter.font.Font(family='Helvetica', size=14)
    ButtonCekWaktu.place(x=405, y=400, in_=FramePilihWaktu)

    ButtonReset = tkinter.Button(FramePilihWaktu, height = 2, width = 10, bg='yellow', text ="Clear All", command=lambda:raise_frame(rightMenu))
    ButtonReset['font'] = tkinter.font.Font(family='Helvetica', size=14)
    ButtonReset.place(x=265, y=400, in_=FramePilihWaktu)