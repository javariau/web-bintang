# Ulangi proses tanpa emoji (karena PDF fpdf default tidak dukung karakter Unicode penuh)
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Panduan Belajar Terstruktur: HTML + CSS + Python (Minggu 1)", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, f"{title}", ln=True)
        self.ln(2)

    def chapter_body(self, text):
        self.set_font("Arial", size=11)
        self.multi_cell(0, 8, text)
        self.ln()

pdf = PDF()
pdf.add_page()

# Hari 1 - HTML Dasar
pdf.chapter_title("Hari 1 – HTML Dasar")
html_day1 = """
Materi:
- Tag dasar: <html>, <head>, <body>, <h1> sampai <h6>, <p>, <img>, <a>
- Struktur HTML
- Cara menulis dan menyimpan file .html

Tugas:
- Buat file index.html
- Tulis nama, deskripsi singkat, dan gambar diri kamu
- Tambahkan link ke profil media sosial (pakai <a>)
"""
pdf.chapter_body(html_day1)

# Hari 2 - CSS Dasar
pdf.chapter_title("Hari 2 – CSS Dasar")
css_day2 = """
Materi:
- Cara hubungkan file CSS ke HTML (<link>)
- Properti dasar: color, background, font-size, padding, margin, border

Tugas:
- Buat file style.css
- Ubah warna background halaman dan font heading
- Tambahkan padding dan border pada gambar
"""
pdf.chapter_body(css_day2)

# Hari 3 - Python Dasar
pdf.chapter_title("Hari 3 – Python Dasar")
python_day3 = """
Materi:
- print()
- input()
- variabel

Tugas:
- Buat program biodata: minta input nama dan umur
- Cetak hasilnya di layar
Contoh:
Nama kamu siapa? > Bintang
Umur kamu? > 19
Halo Bintang, umur kamu 19 tahun.
"""
pdf.chapter_body(python_day3)

# Hari 4 - HTML List & Form
pdf.chapter_title("Hari 4 – HTML List dan Form")
html_day4 = """
Materi:
- Tag <ul>, <ol>, <li> (list)
- Formulir: <form>, <input>, <label>, <button>

Tugas:
- Tambahkan daftar skill kamu ke index.html (pakai list)
- Tambahkan form "Hubungi Saya" (isi: nama, pesan)
"""
pdf.chapter_body(html_day4)

# Hari 5 - CSS Layout (Flexbox)
pdf.chapter_title("Hari 5 – CSS Layout: Flexbox")
css_day5 = """
Materi:
- display: flex
- justify-content, align-items
- Flex direction (row, column)

Tugas:
- Buat layout kartu profil: foto di atas, nama, deskripsi, tombol
- Buat 2 kartu berjajar (pakai flexbox)
"""
pdf.chapter_body(css_day5)

# Hari 6 - Python If-Else & Kalkulasi
pdf.chapter_title("Hari 6 – Python If-Else & Kalkulasi")
python_day6 = """
Materi:
- if, else, elif
- Operasi matematika: +, -, *, /

Tugas:
- Buat program kalkulator sederhana (2 angka + operator)
- Tambahkan pengecekan: jika operator tidak valid, tampilkan error
"""
pdf.chapter_body(python_day6)

# Hari 7 - Recap & Mini Project
pdf.chapter_title("Hari 7 – Review dan Proyek Mini")
summary = """
Gabungkan semua:
- Buat halaman profil sederhana (HTML + CSS)
- Buat program Python interaktif (biodata + kalkulasi)

Checklist:
- HTML: heading, gambar, link, form
- CSS: warna, padding, flexbox
- Python: input, print, if-else

Selamat! Kamu menyelesaikan minggu pertama!
"""
pdf.chapter_body(summary)

# Save PDF
pdf_path = "/mnt/data/Rencana_Belajar_HTML_CSS_Python_Minggu1.pdf"
pdf.output(pdf_path)
pdf_path
