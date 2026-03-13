import tkinter as tk                      # Import modul tkinter untuk membuat GUI
from tkinter import messagebox            # Import modul messagebox untuk popup
import random                             # Import random untuk gerakan musuh acak

# ========== JENDELA UTAMA ========== #
root = tk.Tk()                            # Membuat jendela utama
root.title("Login Pac-Man")              # Judul jendela
root.geometry("650x450")                 # Ukuran jendela
root.configure(bg="pink")                # Warna latar belakang

# ========== DATA LOGIN ========== #
valid_username = "fathia"
valid_password = "1234"

# ========== FUNGSI LOGIN ========== #
def login():
    user = username_entry.get()          # Ambil input username
    pw = password_entry.get()            # Ambil input password
    if user == valid_username and pw == valid_password:
        messagebox.showinfo("Login Berhasil", "Silakan isi data diri.")
        login_frame.pack_forget()        # Sembunyikan form login
        form_frame.pack(pady=10)         # Tampilkan form data diri
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah!")

# ========== FUNGSI SUBMIT DATA DIRI ========== #
def submit_data():
    # Validasi semua field harus diisi
    if not all([entry_nama.get(), entry_absen.get(), entry_kelas.get(), entry_tanggal.get(), entry_guru.get()]):
        messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
        return
    messagebox.showinfo("Data Diterima", "Data berhasil disimpan.")
    form_frame.pack_forget()             # Sembunyikan form data diri
    start_game()                         # Mulai game

# ========== FRAME LOGIN ========== #
login_frame = tk.Frame(root, bg="pink")
login_frame.pack(pady=50)

# Judul dan keterangan
tk.Label(login_frame, text="## PROJECT 2 PEMROGRAMAN DASAR SEMESTER 2 TAHUN AJARAN 2024 - 2025 ##",
         font=("Comic Sans MS", 7, "bold"), bg="pink").pack()
tk.Label(login_frame, text="## SELAMAT DATANG DI GAME PAC-MAN BERBASIS GUI TKINTER MENGGUNAKAN BAHASA PEMROGRAMAN PYTHON ##",
         font=("Comic Sans MS", 7, "bold"), bg="pink").pack()
tk.Label(login_frame, text="## KELAS X TEL 8 ##",
         font=("Comic Sans MS", 7, "bold"), bg="pink").pack()

tk.Label(login_frame, text="Login", font=("Comic Sans MS", 16, "bold"), bg="pink").pack(pady=10)

# Form input username dan password
tk.Label(login_frame, text="Username:", bg="pink").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:", bg="pink").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=login).pack(pady=10)

# ========== FRAME FORM DATA DIRI ========== #
form_frame = tk.Frame(root, bg="pink")

tk.Label(form_frame, text="Form Data Diri", font=("Arial", 14, "bold"), bg="pink").pack(pady=10)

# Input data siswa
tk.Label(form_frame, text="Nama Lengkap", bg="pink").pack()
entry_nama = tk.Entry(form_frame, width=40)
entry_nama.pack()

tk.Label(form_frame, text="Absen", bg="pink").pack()
entry_absen = tk.Entry(form_frame, width=40)
entry_absen.pack()

tk.Label(form_frame, text="Kelas", bg="pink").pack()
entry_kelas = tk.Entry(form_frame, width=40)
entry_kelas.pack()

tk.Label(form_frame, text="Hari, Tanggal", bg="pink").pack()
entry_tanggal = tk.Entry(form_frame, width=40)
entry_tanggal.pack()

tk.Label(form_frame, text="Guru Mapel", bg="pink").pack()
entry_guru = tk.Entry(form_frame, width=40)
entry_guru.pack()

tk.Button(form_frame, text="Submit", command=submit_data).pack(pady=20)

# ========== GAME PAC-MAN ========== #
def start_game():
    win = tk.Toplevel()                      # Buat jendela baru untuk game
    win.title("Pac-Man Game")

    canvas = tk.Canvas(win, width=400, height=400, bg="black")  # Area permainan
    canvas.pack()

    # Tampilkan skor
    score = tk.IntVar(value=0)
    tk.Label(win, text="Score:", font=("Arial", 12)).pack()
    tk.Label(win, textvariable=score, font=("Arial", 12)).pack()

    cell = 20  # Ukuran setiap sel grid

    # Desain labirin
    maze = [
        "####################",
        "#........#.........#",
        "#.####...#...####..#",
        "#........#.........#",
        "#.####.#####.####..#",
        "#........#.........#",
        "####.###.#.###.#####",
        "#........P.........#",
        "####################"
    ]

    # Variabel game
    pacman = None
    foods = []
    dir_x, dir_y = 0, 0  # Arah gerak awal Pac-Man
    pac_x = pac_y = 0

    # Gambar labirin, makanan, dan Pac-Man
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            px, py = x * cell, y * cell
            if char == "#":
                canvas.create_rectangle(px, py, px + cell, py + cell, fill="blue")
            elif char == ".":
                food = canvas.create_oval(px+7, py+7, px+13, py+13, fill="white")
                foods.append((x, y, food))
            elif char == "P":
                pacman = canvas.create_oval(px+2, py+2, px+18, py+18, fill="yellow")
                pac_x, pac_y = x, y

    # ========== Musuh (Hantu) ========== #
    enemies = [
        {"id": canvas.create_rectangle(5*cell+2, 1*cell+2, 5*cell+18, 1*cell+18, fill="red"), "x": 5, "y": 1},
        {"id": canvas.create_rectangle(10*cell+2, 5*cell+2, 10*cell+18, 5*cell+18, fill="green"), "x": 10, "y": 5},
        {"id": canvas.create_rectangle(15*cell+2, 2*cell+2, 15*cell+18, 2*cell+18, fill="orange"), "x": 15, "y": 2},
    ]

    # Fungsi gerak Pac-Man
    def move_pacman():
        nonlocal pac_x, pac_y
        nx, ny = pac_x + dir_x, pac_y + dir_y
        if maze[ny][nx] != "#":
            canvas.move(pacman, dir_x * cell, dir_y * cell)
            pac_x, pac_y = nx, ny
            eat_food()         # Periksa makanan
            check_collision()  # Periksa tabrakan
        win.after(200, move_pacman)

    # Fungsi makan makanan
    def eat_food():
        for f in foods:
            if f[0] == pac_x and f[1] == pac_y:
                canvas.delete(f[2])
                foods.remove(f)
                score.set(score.get() + 10)
                break
        if not foods:
            messagebox.showinfo("Menang", "Selamat! Kamu menang!")
            win.destroy()

    # Fungsi gerak musuh secara acak
    def move_enemy():
        for enemy in enemies:
            arah = random.choice([(0,1), (0,-1), (1,0), (-1,0)])  # Acak arah
            nx, ny = enemy["x"] + arah[0], enemy["y"] + arah[1]
            if maze[ny][nx] != "#":
                canvas.move(enemy["id"], arah[0] * cell, arah[1] * cell)
                enemy["x"], enemy["y"] = nx, ny
        check_collision()
        win.after(400, move_enemy)

    # Fungsi cek tabrakan dengan musuh
    def check_collision():
        for enemy in enemies:
            if pac_x == enemy["x"] and pac_y == enemy["y"]:
                messagebox.showinfo("Game Over", f"Kamu tertangkap! Skor: {score.get()}")
                win.destroy()
                break

    # Fungsi arah panah keyboard
    def on_key(e):
        nonlocal dir_x, dir_y
        if e.keysym == "Up":
            dir_x, dir_y = 0, -1
        elif e.keysym == "Down":
            dir_x, dir_y = 0, 1
        elif e.keysym == "Left":
            dir_x, dir_y = -1, 0
        elif e.keysym == "Right":
            dir_x, dir_y = 1, 0

    win.bind("<Key>", on_key)   # Bind keyboard
    move_pacman()               # Jalankan Pac-Man
    move_enemy()                # Jalankan musuh

# ========== JALANKAN PROGRAM ========== #
root.mainloop()
 