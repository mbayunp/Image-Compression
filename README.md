# Image-Compression
Penamaan Sertifikat di data exel

Program untuk membuat sertifikat menggunakan data dari file CSV dengan menggunakan pilihan font dan template sertifikat yang ditentukan oleh pengguna. Berikut adalah penjelasan dan tahapan proses dalam kode tersebut:

Import Library: Pertama, kita mengimpor beberapa library yang diperlukan yaitu pandas untuk membaca file CSV, PIL (Python Imaging Library) untuk memanipulasi gambar, matplotlib.pyplot untuk menampilkan gambar, dan os untuk mengakses sistem operasi.

Membaca File CSV: Kode dimulai dengan membaca file CSV menggunakan pd.read_csv('Book1.csv') dan menyimpannya dalam variabel data.

Menampilkan Daftar Font: Kode mencetak daftar font yang tersedia berdasarkan kolom pertama dari file CSV (Book1.csv). Nama-nama font disimpan dalam list font_names.

Memilih Font: Pengguna diminta untuk memasukkan nomor font pilihan mereka dari daftar font yang tersedia dengan menggunakan input(). Nomor font yang dipilih disimpan dalam variabel user_choice. Font yang sesuai dengan pilihan pengguna ditentukan oleh selected_font = font_names[user_choice - 1].

Memilih Template Sertifikat: Pengguna juga diminta untuk memilih template sertifikat yang akan digunakan melalui input(). Pilihan pengguna disimpan dalam variabel template_choice. Nama file template sertifikat yang sesuai ditentukan oleh template_filename = f"sertifikat{template_choice}.png".

Fungsi Pembuatan Sertifikat: Kode mendefinisikan fungsi create_certificate() untuk membuat sertifikat. Fungsi ini membuka template sertifikat, menambahkan nama peserta dengan menggunakan font dan ukuran yang ditentukan, dan menyimpan sertifikat dengan nama file yang sesuai.

Fungsi Kompresi Gambar: Kode mendefinisikan fungsi compress_image() untuk mengompresi gambar. Fungsi ini membuka gambar, menyesuaikan ukurannya sesuai dengan batas maksimum yang ditentukan, dan menyimpan gambar yang sudah dikompresi.

Melakukan Perulangan: Selama perulangan, program akan menampilkan contoh sertifikat menggunakan nama dari baris pertama data. Contoh sertifikat akan dibuat menggunakan font yang dipilih dan template sertifikat yang dipilih. Selanjutnya, program akan menanyakan apakah pengguna ingin melanjutkan dengan font tersebut atau memilih font lain. Jika pengguna memilih untuk melanjutkan, program akan membuat sertifikat untuk setiap baris data dan menyimpannya dalam daftar image_files.

Kompresi dan Tampilkan Gambar: Setelah selesai membuat sertifikat, program akan mengompresi gambar-gambar tersebut dengan batasan ukuran yang ditentukan. Ukuran file sebelum dan setelah kompresi akan dicetak, dan gambar yang sudah dikompresi akan ditampilkan menggunakan matplotlib.pyplot.

Setelah semua proses selesai, program akan keluar dari perulangan dan berakhir.

Demikian penjelasan tentang kode program yang diberikan. Kode tersebut membantu untuk membuat sertifikat dengan memanfaatkan data dari file CSV, memilih font dan template sertifikat, serta mengompresi gambar-gambar yang dihasilkan.






