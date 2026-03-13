import tkinter as tk
from tkinter import messagebox

# Maksimal percobaan login
max_attempt = 3
attempt = 0

# Fungsi login
def submit_form():
    global attempt
    username = entry_name.get()
    password = entry_password.get()

    if username != 'yaya' or password != 'ok':
        attempt += 1
        if attempt >= max_attempt:
            messagebox.showerror("Gagal", "Percobaan login habis. Program akan keluar.")
            root.destroy()
        else:
            messagebox.showerror("Error", f"Username atau password salah!\nSisa percobaan: {max_attempt - attempt}")
    else:
        form_frame.pack_forget()
        show_cashier()

# Fungsi untuk menampilkan form kasir
def show_cashier():
    cashier_frame = tk.Frame(root, padx=40, pady=30)
    cashier_frame.pack()

    title = tk.Label(cashier_frame, text="APLIKASI KASIR", font=("Arial", 16, "bold"))
    title.pack(pady=20)

    # Form input
    tk.Label(cashier_frame, text='Nama Pembeli:', font=("Arial", 12)).pack(anchor="w", pady=3)
    nama_pembeli = tk.Entry(cashier_frame, width=40)
    nama_pembeli.pack(pady=5)

    tk.Label(cashier_frame, text='Nama Barang:', font=("Arial", 12)).pack(anchor="w", pady=3)
    nama_barang = tk.Entry(cashier_frame, width=40)
    nama_barang.pack(pady=5)

    tk.Label(cashier_frame, text='Jumlah Produk (Angka):', font=("Arial", 12)).pack(anchor="w", pady=3)
    jumlah_produk = tk.Entry(cashier_frame, width=40)
    jumlah_produk.pack(pady=5)

    tk.Label(cashier_frame, text='Harga Produk (Angka):', font=("Arial", 12)).pack(anchor="w", pady=3)
    harga_produk = tk.Entry(cashier_frame, width=40)
    harga_produk.pack(pady=5)

    tk.Label(cashier_frame, text='Uang Pembeli (Angka):', font=("Arial", 12)).pack(anchor="w", pady=3)
    uang_pembeli = tk.Entry(cashier_frame, width=40)
    uang_pembeli.pack(pady=5)

    # Fungsi tombol Total
    def show_result():
        try:
            jumlah = int(jumlah_produk.get())
            harga = int(harga_produk.get())
            uang = int(uang_pembeli.get())
            total = jumlah * harga
            kembali = uang - total

            if kembali < 0:
                messagebox.showwarning("Kurang", "Uang pembeli kurang!")
                return

            message = f'''
======= STRUK PEMBAYARAN =======

Nama Pembeli  : {nama_pembeli.get()}
Nama Barang   : {nama_barang.get()}
Jumlah Barang : {jumlah}
Harga Satuan  : Rp. {harga}

--------------------------------
Total         : Rp. {total}
Uang Tunai    : Rp. {uang}
Kembalian     : Rp. {kembali}
--------------------------------

Terima Kasih Telah Berbelanja!
            '''
            messagebox.showinfo("Invoice", message)

        except ValueError:
            messagebox.showerror("Error", "Input jumlah, harga, dan uang harus berupa angka!")

    tk.Button(
        cashier_frame,
        text='Total',
        command=show_result,
        width=20,
        height=2
    ).pack(pady=25)

# GUI Utama
root = tk.Tk()
root.title("Aplikasi Kasir SMK Telkom Jakarta")
root.geometry("450x550")  # ukuran dibuat lebih panjang

# Frame login
form_frame = tk.Frame(root, padx=40, pady=30)
form_frame.pack(pady=60)

title = tk.Label(form_frame, text="LOGIN KASIR", font=("Arial", 16, "bold"))
title.pack(pady=20)

tk.Label(form_frame, text="Username", font=("Arial", 12)).pack(anchor="w")
entry_name = tk.Entry(form_frame, width=35)
entry_name.pack(pady=8)

tk.Label(form_frame, text="Password", font=("Arial", 12)).pack(anchor="w")
entry_password = tk.Entry(form_frame, show="*", width=35)
entry_password.pack(pady=8)

submit_button = tk.Button(form_frame, text="Login", command=submit_form, width=18, height=1)
submit_button.pack(pady=20)

root.mainloop()