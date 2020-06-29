import pytest
import sys
sys.path.append('../src')
from pengolahanruangan import *

def test_isInDataAdminCase1():
    #Test case berhasil untuk user dan password yang benar
    user = 'kevin'
    pasw = 'kevin'
    assert isInDataAdmin(user,pasw)==1

def test_isInDataAdminCase2():
    #Test case menghasilkan nilai gagal untuk masukkan user ATAU password salah
    user = 'kevin'
    pasw = 'hans'
    assert isInDataAdmin(user,pasw)==0

def test_isNomorAvailableCase1():
    nomorruangan = 1
    while nomorruangan<=8:
        assert isNomorAvailable(nomorruangan)==0
        nomorruangan +=1

def test_isNomorAvailableCase2():
    nomorruangan = 99999999
    assert isNomorAvailable(nomorruangan)==1

def test_isTipeAvailableCase1():
    tipe_dasar = ['Family A-1','Family A-2', 'Deluxe A-3', 'Deluxe A-4', 'Reguler B-1', 'Reguler B-2', 'Reguler B-3', 'Reguler B-4']
    for tipe in tipe_dasar: 
        assert isTipeAvailable(tipe)==0

def test_isTipeAvailableCase2():
    tipe = 'KMS'
    assert isTipeAvailable(tipe)==1

def test_deleteTipeRuanganCase1():
    #Test case berhasil untuk tipe yang benar
    tipe = 'Family A-1'
    assert isTipeAvailable(tipe) ==0
    deleteTipeRuangan(tipe)
    assert isTipeAvailable(tipe) ==1
    addTipeRuangan('Family A-1',30, 2000000, 18000000,1,'kevin')

def test_deleteTipeRuanganCase2():
    #Test case menghasilkan nilai gagal untuk tipe yang salah
    tipe = 'Family A-11111111'
    assert isTipeAvailable(tipe) ==1
    deleteTipeRuangan(tipe)
    assert isTipeAvailable(tipe) ==1


def test_deleteNomorRuanganCase1():
    #Test case berhasil untuk nomor yang benar
    Nomor = 1
    assert isNomorAvailable(Nomor) ==0
    deleteNomorRuangan(Nomor,'Family A-1')
    assert isNomorAvailable(Nomor) ==1
    addDaftarRuangan('Family A-1',1,'kevin')

def test_deleteNomorRuanganCase2():
    #Test case menghasilkan nilai gagal untuk nomor yang salah
    Nomor = '99'
    assert isNomorAvailable(Nomor) ==1
    deleteNomorRuangan(Nomor,'Family A-1')
    assert isNomorAvailable(Nomor) ==1

def test_addTipeRuanganCase1():
    tipe = 'Family-99999'
    assert isTipeAvailable(tipe) ==1
    addTipeRuangan(tipe,1,1,1,9999,'kevin')
    assert isTipeAvailable(tipe) ==0
    deleteTipeRuangan(tipe)

def test_addDaftarRuanganCase1():
    assert isTipeAvailable('Family A-1')==0
    assert isNomorAvailable(888)==1
    addDaftarRuangan('Family A-1',888,'kevin')
    assert isTipeAvailable('Family A-1')==0
    assert isNomorAvailable(888)==0
    deleteNomorRuangan(888,'Family A-1')





