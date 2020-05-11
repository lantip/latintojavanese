Transliterasi Aksara Latin ke Aksara Jawa
===
Ini adalah script untuk mengubah kalimat dengan aksara latin menjadi aksara Jawa.
Pipeline script ini adalah:
1. Membagi kalimat menjadi kata per kata
2. Memecah kata menjadi suku kata dan suku ucapan
3. Mengubah masing-masing suku kata dan suku ucapan menjadi aksara Jawa, lalu menggabungkan
4. Menggabungkan masing-masing kata menjadi kalimat asli

Metode
---
Saya tidak menggunakan regex untuk script transliterasi ini. 
Secara `best-practice` untuk transliterasi akan lebih singkat dan lebih cepat menggunakan regex, 
tapi saya memilih cara ini supaya lebih mudah dibaca. 

Sumonggo pull dan push jika panjenengan ingin mengubah memakai metode regex. Tapi mohon jadikan script dengan nama file baru,
supaya script ini tetap bisa jadi acuan.

Update
---
Menambahkan flask app

Kebutuhan
---
- Python
- Flask

Instalasi
---
- `git clone https://github.com/lantip/latintojavanese.git`
- Jalankan `pip3 install  pipenv`
- Jalankan `pipenv install`


Penggunaan
---
Command line:
    $ cd latintojavanese
    $ python latintojavanese.py
    
    > masukkan kalimat di cursor input

Web based:
    $ cd latintojavanese
    $ python app.py
    
    > buka  browser, http://127.0.0.1:5000/form



Thanks To
---
- Mas Bekel Setya Amrih Prasaja
- Mas Arif
- Tim K.A.J I Jogja