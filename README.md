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
![Autentikasi Pengguna](asset/readme/autentikasipengguna.png)
    - 1.1 Login
        - 1.1.1 Mengisi form login
            - ![Mengisi Form Login](asset/readme/login.png)
        - 1.1.2 Validasi login
            Tidak ada layar
        - 1.1.3 Pesan gagal login
            ![Menampilkan Pesan Gagal Login](asset/readme/gagallogin.png)
    - 1.2 Register
        - 1.2.1 Mengisi form registrasi
            ![Mengisi Form Registrasi](asset/readme/register.png)
        - 1.2.2 Validasi registrasi
            Tidak ada layar
        - 1.2.3 Pesan gagal registrasi
            ![Registrasi dengan email yang sudah ada](asset/readme/gagalregis1.png)
            ![Menampilkan Pesan Gagal Registrasi](asset/readme/gagalregis2.png)
    - 1.3 Forgot password
        ![Menerima email Forgot Password](asset/readme/forgotpassword.png)
        ![Validasi Forgot Password](asset/readme/forgotpassword1.png)

- 2 Homepage
    - 2.1 Pengguna
        ![Menampilkan Homepage Pengguna](asset/readme/homepage.png)
        - 2.1.1 Menampilkan daftar game
            ![Menampilkan Daftar Game](asset/readme/game1.png)
        - 2.1.1.1 Filter
            Hanya diimplementasikan front end nya saja
            ![Menampilkan Filter](asset/readme/filter.png)
        - 2.1.1.2 Search
            - Hanya diimplementasikan front end nya saja
            ![Menampilkan Search](asset/readme/search.png)
        - 2.1.1.3 Menampilkan deskripsi game
            ![Menampilkan Deskripsi Game](asset/readme/deskripsigame.png)
        - 2.1.1.3.1 Membeli game
            ![Membeli Game](asset/readme/validasibeli.png)
        - 2.1.1.3.1.1 Validasi saldo e-wallet
            - Tidak ada layar
        - 2.1.1.3.1.1.1 Menampilkan link download game
            ![Menampilkan link download Game](asset/readme/beligame.png)
            ![Menampilkan link download Game2](asset/readme/beligame2.png)
            ![Homepage setelah membeli game (saldo berkurang)](asset/readme/homepageafterbuygame.png)
        - 2.1.1.3.1.2 Pesan gagal saldo tidak cukup
            ![Gagal Pembelian Game](asset/readme/gagalbeli.png)
            ![Pesan Gagal Saldo Tidak Cukup](asset/readme/gagalbeli1.png)
    - 2.1.2 Menampilkan saldo e-wallet
        - ![Menampilkan Saldo](asset/readme/saldo.png)
    - 2.1.4 Menampilkan profil
        ![Menampilkan Profil](asset/readme/profile.png)
        - 2.1.4.1 Ganti password
            ![Mengganti Password](asset/readme/forgotpassword.png)
            ![Pesan Password Berhasil Diganti](asset/readme/forgotpassword1.png)

- 3 Logout
    - Kembali ke modul Autentikasi Pengguna
    - ![Logout](asset/readme/logout.png)

## Daftar Realisasi Tabel Basis Data

- 1 Tabel Accounts
    - email
    - password
    - full_name
    - date_of_birth
    - nationality
    - phone_number
    - created_on
- 2 Tabel Game
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
- 3 Tabel Ewallet
    - email
    - saldo

## Responsibilities

- 1 Jones Napoleon Autumn
    - Modul utama bulk aplikasi
    - Modul login
    - Modul register
    - Modul forget password
    - Modul change password

- 2 Inka Anindya Riyadi
    - Modul menampilkan deskripsi game
    - Modul membeli game
    - Modul validasi saldo e-wallet
    - Modul menampilkan link download game
    - Modul menampilkan saldo
    - Modul pesan gagal saldo

- 3 Stefanus Gusega Gunawan
    - pytest
    - Modul menampilkan halaman profile

- 4 Fritz Gerald Tjie
    - pytest
    - CI/CD
    - Modul menampilkan daftar game
