# PC GAME STORE

Application system about purchasing PC Game

## Prerequisite
- Python 3.7
- Kivy
- SMTPLIB

## How to run
```
python main.py
```

## Contributors
- Inka Anindya Riyadi - 13518038
- Fritz Gerald - 13518065
- Jones Napoleon Autumn - 13518086
- Stefanus Gusega Gunawan - 13518149

## Daftar Modul yand diimplementasikan
- 1 Autentikasi pengguna
![Autentikasi Pengguna](autentikasipengguna.png)
    - 1.1 Login
        - 1.1.1 Mengisi form login
            - ![Mengisi Form Login](login.png)
        - 1.1.2 Validasi login
            Tidak ada layar
        - 1.1.3 Pesan gagal login
            ![Menampilkan Pesan Gagal Login](gagallogin.png)
    - 1.2 Register
        - 1.2.1 Mengisi form registrasi
            ![Mengisi Form Registrasi](register.png)
        - 1.2.2 Validasi registrasi
            Tidak ada layar
        - 1.2.3 Pesan gagal registrasi
            ![Registrasi dengan email yang sudah ada](gagalregis1.png)
            ![Menampilkan Pesan Gagal Registrasi](gagalregis2.png)
    - 1.3 Forgot password
        ![Menerima email Forgot Password](forgotpassword.png)
        ![Validasi Forgot Password](forgotpassword1.png)

- 2 Homepage
    - 2.1 Pengguna
        ![Menampilkan Homepage Pengguna](homepage.png)
        - 2.1.1 Menampilkan daftar game
            ![Menampilkan Daftar Game](game1.png)
        - 2.1.1.1 Filter
            Hanya diimplementasikan front end nya saja
            ![Menampilkan Filter](filter.png)
        - 2.1.1.2 Search
            - Hanya diimplementasikan front end nya saja
            ![Menampilkan Search](search.png)
        - 2.1.1.3 Menampilkan deskripsi game
            ![Menampilkan Deskripsi Game](deskripsigame.png)
        - 2.1.1.3.1 Membeli game
            ![Membeli Game](validasibeli.png)
        - 2.1.1.3.1.1 Validasi saldo e-wallet
            - Tidak ada layar
        - 2.1.1.3.1.1.1 Menampilkan link download game
            ![Menampilkan link download Game](beligame.png)
            ![Menampilkan link download Game2](beligame2.png)
            ![Homepage setelah membeli game (saldo berkurang)](homepageafterbuygame.png)
        - 2.1.1.3.1.2 Pesan gagal saldo tidak cukup
            ![Gagal Pembelian Game](gagalbeli.png)
            ![Pesan Gagal Saldo Tidak Cukup](gagalbeli1.png)
    - 2.1.2 Menampilkan saldo e-wallet
        - ![Menampilkan Saldo](saldo.png)
    - 2.1.4 Menampilkan profil
        ![Menampilkan Profil](profile.png)
        - 2.1.4.1 Ganti password
            ![Mengganti Password](forgotpassword.png)
            ![Pesan Password Berhasil Diganti](forgotpassword1.png)

- 3 Logout
    - Kembali ke modul Autentikasi Pengguna
    - ![Logout](logout.png)

## Daftar Realisasi Tabel Basis Data
- Tabel Accounts
    - email
    - password
    - full_name
    - date_of_birth
    - nationality
    - phone_number
    - created_on
- Tabel Game
    - nama_file
    - nama_game
    - ukuran
    - harga
    - deskripsi
    - os
    - processor
    - graphic
    - storage
    - link
- Tabel Ewallet
    - email
    - saldo



