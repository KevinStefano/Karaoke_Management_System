# Pengujian Fitur 4: Pemesanan Ruangan

import pytest
import sys
sys.path.append('../src')
from pembatalanpesanan import *
from bookingpesanan import *

def test_cekAdmin():
    value1 = "lio"
    value2 = "lio"
    assert dataAdminProcessing(value1,value2)==1

def test_cekIdPemesanan1():
    value = 1
    assert isDataPemesananValid(value)

def test_cekIdPemesanan2():
    value = 2
    assert isDataPemesananValid(value)

def test_cekIdPemesanan3():
    value = getTotalPesanan()+1
    assert not isDataPemesananValid(value)

def test_setBatal():
    count = getTotalPesanan()+1
    setBatal(str(count-1))
    assert getTotalPesanan() == count-1
    tambahPesananRuangan(count-1, "Michael Hans", None, 1, "2020-03-03", "10:00:00", 60, 400000)