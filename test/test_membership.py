# Pengujian Fitur 4: Pemesanan Ruangan

import pytest
from datetime import date
import sys
sys.path.append('../src')
from  membership import *

def test_tambahmember1():
    email = "eRPeLer@santuy.com"
    nama = "Johnny Sins"
    umur = "69"
    alamat = "Jl. Brazzers No.69"
    notelp = "086969696969"
    paket = "Gold"
    time = datetime.now() + timedelta(days=30)
    updateTableMembership(email, nama, umur, alamat, notelp, paket, time)
    assert True
    mycursor = mydb.cursor()
    formula = "DELETE FROM membership WHERE nama = 'Johnny Sins'"
    mycursor.execute(formula)
    mydb.commit()
    