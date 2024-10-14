# BANTUAN KIP


## Studi Kasus
karena kurangnya pemerataan bantuan berupa KIP di kalangan kurang mampu,dimana orang tua yang mampu anaknya dapat bantuan,sedangkan yang kurang mampu malah tidak dapat bantuan.Jadi saya memiliki inisiatif membuat program pemerataan KIP di lingkungan saya.Saya bekerjasama dengan pemerintah setempat untuk melaksanakan program ini supaya bantuan KIP dapat tersalurkan ke yang lebih tepat.


## Proses coding
1. Inisialisasi Data
Program dimulai dengan mendefinisikan tiga biodata pengguna menggunakan dictionary Python. Setiap dictionary berisi informasi tentang nama, umur, pekerjaan, pekerjaan orang tua, dan pendapatan
2. Input Pengguna
Selanjutnya, program meminta input dari pengguna untuk mengisi biodata:

Nama:
Umur:
Pekerjaan:
Pekerjaan orang tua:
Pendapatan:
3. Inisialisasi Variabel dan Set
Variabel mampu dan tidak_mampu diinisialisasi untuk keperluan logika selanjutnya. Set pekerjaan_ortu_yang_tidak_berhak_dapat_KIP berisi pekerjaan orang tua yang tidak berhak menerima bantuan KIP.
4. Logika Penentuan Bantuan KIP
Program kemudian memeriksa beberapa kondisi untuk menentukan apakah pengguna berhak mendapatkan bantuan KIP:

Umur minimal 10 tahun
Pekerjaan tidak termasuk dalam daftar pekerjaan yang tidak berhak
Pendapatan harus kurang dari atau sama dengan 1.500.000
Jika semua kondisi terpenuhi, maka hasilnya adalah "dapat bantuan KIP". Jika tidak, hasilnya adalah "tidak dapat bantuan KIP".
5. Menampilkan Hasil
Terakhir, program mencetak semua informasi biodata yang telah dimasukkan dan klasifikasi apakah pengguna berhak mendapatkan bantuan KIP.

## Kesimpulan
Program ini berfungsi untuk mengumpulkan informasi biodata dari pengguna dan menentukan kelayakan mereka untuk mendapatkan bantuan KIP berdasarkan kriteria yang telah ditentukan.