# Pengujian Fitur 4: Pemesanan Ruangan

import pytest
from datetime import date
import sys
sys.path.append('../src')
from  bookingpesanan import *
from pembatalanpesanan import *

def test_cekMembershipCase1():
    value = "kevin@gmail.com"
    assert cekMembership(value) == True

def test_cekMembershipCase2():
    value = "michaelhans777@gmails.com"
    assert cekMembership(value) == False

def test_cekWaktuCase1():
    waktu = "10:00:00"
    tanggal = date.today().strftime("%Y-%m-%d")
    assert cekWaktu(waktu, tanggal) == True

def test_cekWaktuCase2():
    waktu = "02:00:00"
    tanggal = date.today().strftime("%Y-%m-%d")
    assert cekWaktu(waktu, tanggal) == True

def test_getAvailableRoomCase1():
    tipe = "Family A-1"
    waktu = "10:00:00"
    tanggal = date.today().strftime("%Y-%m-%d")
    assert not(getAvailableRoom(tipe,waktu,tanggal) == None)

def test_getAvailableRoomCase2():
    tipe = "Deluxe A-3"
    waktu = "10:00:00"
    tanggal = date.today().strftime("%Y-%m-%d")
    assert not(getAvailableRoom(tipe,waktu,tanggal) == None)

def test_getPriceOfRuanganCase1():
    assert getPriceOfRuangan(1, None) == 2000000
    assert getPriceOfRuangan(1, "kevin@gmail.com") == 18000000

def test_getPriceOfRuanganCase1():
    assert getPriceOfRuangan(8, None) == 75000
    assert getPriceOfRuangan(8, "kevin@gmail.com") == 70000

def test_tambahPesananCase1():
    id_pesanan = getIDPesanan()
    temp = getTotalPesanan()
    nama = "Michael Hans"
    email = None
    tanggal = date.today().strftime("%Y-%m-%d")
    waktu_masuk = "18:00:00"
    no_ruangan = getAvailableRoom("Family A-1", waktu_masuk, tanggal)
    durasi = "60"
    harga_akhir = getPriceOfRuangan(no_ruangan, email)
    tambahPesananRuangan(id_pesanan, nama, email, no_ruangan, tanggal, waktu_masuk, durasi, harga_akhir)
    assert temp+1 == getTotalPesanan()
    setBatal(str(id_pesanan))