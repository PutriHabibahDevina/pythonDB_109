import Lanjutan_tkinter as Ltk
import sqlite3
from Lanjutan_tkinter import messagebox

window = Ltk.Tk()
window.geometry("400x300")

#Buat frame
frame = Ltk.Frame(window)
frame.place(relx = 0.5, rely = 0.5, anchor = Ltk.CENTER)

#Fungsi untuk membuat tabel jika belum ada
def create_table():
    connection = sqlite3.connect('Ltk.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXIST nilai_siswa (
                    id INTEGER PRIMARY KEY,
                    nama_siswa TEXT,
                    biologi INTEGER,
                    fisika INTEGER,
                    inggris INTEGER
                   prediksi_prodi TEXT
                    )''')
    connection.commit()
    connection.close()

# Fungsi untuk memasukkan data ke dalam database
def insert_data():
    nama_siswa = entry_nama_siswa.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    connection = sqlite3.connect('Ltk.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO nilai_siswa(siswa, biologi, fisika, inggris)
                   VALUES (?, ?, ?, ?)''', (nama_siswa, biologi, fisika, inggris))
    connection.commit()
    connection.close()

#Menghitung nilai untuk pilihan prodi
    max_nilai = max(biologi, fisika, inggris)
    prediksi = ""
    if max_nilai == biologi:
        prediksi = "Kedokteran"
    elif max_nilai == fisika:
        prediksi = "Teknik"
    elif max_nilai == inggris:
        prediksi = "Bahasa"
    
    hasil.config(text=f"Hasil Prediksi: {prediksi}")

    connection = sqlite3.connect('Ltk.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                   VALUES (?, ?, ?, ?, ?)''', (nama_siswa, biologi, fisika, inggris, prediksi))
    connection.commit()
    connection.close()

#Fungsi untuk menyimpan data setelah tombol "Simpan" ditekan
def simpan_data():
    insert_data()
    entry_nama_siswa.delete(0, Ltk.END)
    entry_biologi.delete(0, Ltk.END)
    entry_fisika.delete(0, Ltk.END)
    entry_inggris.delete(0, Ltk.END)

#Membuat tabel jika belum ada
create_table()

#Membuat GUI menggunakan tkinter
root = Ltk.Tk()
root.title("Input Nilai Siswa")

label_nama_siswa = Ltk.Label(root, text = "Nama Siswa:")
label_nama_siswa.pack()
entry_nama_siswa = Ltk.Entry(root)
entry_nama_siswa.pack()

label_biologi = Ltk.Label(root, text = "Nilai Biologi:")
label_biologi.pack()
entry_biologi = Ltk.Entry(root)
entry_biologi.pack()

label_fisika = Ltk.Label(root, text = "Nilai Fisika:")
label_fisika.pack()
entry_fisika = Ltk.Entry(root)
entry_fisika.pack()

label_inggris = Ltk.Label(root, text = "Nilai Inggris:")
label_inggris.pack()
entry_inggris = Ltk.Entry(root)
entry_inggris.pack()

button_simpan = Ltk.Button(root, text = "Simpan", command = simpan_data)
button_simpan.pack()

hasil = Ltk.Label(root, text = "Hasil Prediksi")
hasil.pack()

root.mainloop()