git remote add origin https://github.com/ChinchillaBiiru09/WebApp-Showroom.git

#ASSESSMENT
Buatlah sebuah aplikasi web menggunakan Python Dj untuk mengelola data showroom mobil. Aplikasi ini harus memiliki fungsi-fungsi berikut:
1. Menambah Mobil: Buat halaman/form untuk menambahkan data mobil. Setiap mobil memiliki data seperti: ID (bisa dibuat secara otomatis atau diinput manual), Merk, Model, Tahun, Harga Dasar. Jika mobil dibeli dengan dana bank, tampilkan bagian tambahan di form untuk menginput: Jumlah dana pinjaman dari bank, Suku bunga bank (dalam persen per tahun)
2. Menampilkan Semua Mobil: Halaman utama (homepage) menampilkan daftar semua mobil yang tersedia di showroom. Tampilkan informasi singkat setiap mobil (misalnya, ID, Merk, Model, dan Tahun).
3. Menampilkan Detail Mobil: Buat halaman detail untuk setiap mobil. Saat user meng-klik salah satu mobil dari daftar, tampilkan detail lengkap mobil, termasuk data service (jika ada), serta perhitungan pembiayaan seperti cicilan bulanan jika dana bank digunakan.
4. Menambahkan Service Mobil: Sediakan halaman/form untuk mencatat service mobil. Setiap service dapat memiliki data: ID mobil yang diservice, Tanggal service, Deskripsi service, Biaya service. Data service ini harus dihubungkan ke mobil yang bersangkutan sehingga nantinya setiap mobil bisa memiliki riwayat service
5. Menghitung HPP Mobil: Buat fungsi untuk menghitung HPP (Harga Pokok Produksi) mobil. Rumus sederhana yang dapat digunakan misalnya: HPP = Harga Dasar/(Pinjaman + Suku Bunga) + Total Biaya Service
6. Menghapus Mobil: Sediakan fitur untuk menghapus data mobil dari showroom. Penghapusan bisa dilakukan dari halaman daftar mobil atau halaman detail mobil.