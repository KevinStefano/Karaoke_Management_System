# Pengujian Fitur 4: Pemesanan Ruangan

import pytest
import sys
sys.path.append('../src')
from pembatalanpesanan import *

def test_cekAdmin():
    value1 = "lio"
    value2 = "lio"
    assert dataAdminProcessing(value1,value2)==1

def test_cekIdPemesanan():
    value = "1"
    assert isDataPemesananValid(value)==False