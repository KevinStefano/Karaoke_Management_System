Teknis Melakukan Testing:
1. Install pytest menggunakan command line sebagai berikut.
```
pip install pytest==2.9.1 
```
2. Buatlah sebuah file test sederhana sebagai berikut. Perhatikan bahwa method test harus diawali oleh test_namaProses atau namaProses_test.
   test_sample1.py
   ```
	import pytest

	@pytest.mark.set1 <--- MarkerName
	def test_file1_method1():
		x=5
		y=6
		assert x+1 == y,"test failed"
		assert x == y,"test failed because x=" + str(x) + " y=" + str(y)

	@pytest.mark.set1 <--- MarkerName
	def test_file1_method2():
		x=5
		y=6
		assert x+1 == y,"test failed" 
	```

3. Jalankan pada command salah satu command berikut ini. Pastikan directory cmd sudah berada pada file test yang dimaksud.

	Berikut ini adalah daftar command yang paling sering digunakan dalam menguji suatu test.py
	- Untuk menjalankan semua file data uji dalam folder
	```
	py.test
	```
	- Untuk menjalankan data uji dengan pendekatan pattern matching pada nama test_method
	```
	py.test -k method -v
	```
	- Untuk menjalankan sebuah file data uji
	```
	py.test <filename>
	```
   - Untuk menjalankan sebuah data uji dengan nama marker tertentu (ditandai dengan @pytest.marker.markername)
   ```
   py.test -m @markername
   ```

Referensi: https://www.guru99.com/pytest-tutorial.html