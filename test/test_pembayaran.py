from datetime import date

import pytest
import sys
sys.path.append('../src')

from bookingpesanan import getIDPesanan, getAvailableRoom, tambahPesananRuangan, getPriceOfRuangan
from membership import updateTableMembership
from pembayaran import doesMemberExist, findUnpaidBookingTransaction, updateBookingTransaction, \
    findUnpaidMembershipTransaction, updateMembershipTransaction


def test_doesMemberExist():
    value = 'kevin@gmail.com'
    assert doesMemberExist(value) == True


def test_doesMemberNotExist():
    value = 'thisisrandomemail@example.com'
    assert doesMemberExist(value) == False


def test_findUnpaidMembershipTransaction():
    email = "testemail@test.com"
    nama = "TestName"
    umur = "12"
    alamat = "Test Address"
    notelp = "0812191919191"
    paket = "Gold"
    due_date = date.today().strftime("%Y-%m-%d")
    updateTableMembership(email, nama, umur, alamat, notelp, paket, due_date)
    res = findUnpaidMembershipTransaction(email)
    assert res != 0


def test_bayar_membership():
    updateMembershipTransaction('testemail@test.com', 2000000)
    assert findUnpaidMembershipTransaction('testemail@test.com') == 0


def test_findUnpaidBookingTransaction():
    id_pesanan = getIDPesanan()
    nama = 'TestName'
    email = 'testemail@test.com'
    tanggal = date.today().strftime("%Y-%m-%d")
    waktu_masuk = '20:00:00'
    no_ruangan = getAvailableRoom('Reguler B-1', waktu_masuk, tanggal)
    tambahPesananRuangan(id_pesanan, nama, email, no_ruangan, tanggal, waktu_masuk, '60',
                         getPriceOfRuangan(no_ruangan, email))
    res = findUnpaidBookingTransaction(email)
    assert res != 0


def test_bayar_ruangan():
    res = findUnpaidBookingTransaction('testemail@test.com')
    id_pesanan = res[0]
    updateBookingTransaction(id_pesanan)
    assert findUnpaidBookingTransaction('testemail@test.com') == 0
