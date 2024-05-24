from tkinter import *     
from tkinter import messagebox 
from tkinter import ttk 
import tkinter as tk 
from tkinter.messagebox import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo
from collections import deque
 

logged_in = False
mytickets = deque()

file_path = None
train_schedule = [
    ("KAI101", "Poncol", "Tugu", "08:21", "16:03"),
    ("KAI201", "Solo Balapan", "Tawang", "18:50", "20:43"),
    ("KAI301", "Kutoarjo", "Kroya", "11:00", "13:00"),
    ("KAI302", "Kutoarjo", "Tawang", "03:20", "07:11"),
    ("KAI501","Lempuyangan","Tawang", "15:24", "18:12"),
    ("KAI401","Klaten","Purwokerto", "13:24", "18:42"),
    ("KAI601","Tawang","Solo Balapan", "21:24", "23:42")
]

def otw_jadwal():
    for widget in window.winfo_children():
        widget.place_forget()
    jadwal_kereta()

def otw_pesan():
    for widget in window.winfo_children():
        widget.place_forget() 
    halaman_pesan()

def jadwal_kereta():
    global no_kereta
    labeljadwal = Label(window,
                        text="JADWAL KEBERANGKATAN KERETA", anchor="center",
                        font=("arial", 16))
    labeljadwal.place(x=120, y=40)
    
    jadwal_tree = ttk.Treeview(window)

    
    jadwal_tree["columns"] = ("No. Kereta", "Stasiun Asal", "Stasiun Tujuan", "Jam Berangkat", "Jam Tiba")

    
    jadwal_tree.heading("#0", text="No.")
    jadwal_tree.heading("No. Kereta", text="No. Kereta")
    jadwal_tree.heading("Stasiun Asal", text="Stasiun Asal")
    jadwal_tree.heading("Stasiun Tujuan", text="Stasiun Tujuan")
    jadwal_tree.heading("Jam Berangkat", text="Jam Berangkat")
    jadwal_tree.heading("Jam Tiba", text="Jam Tiba")

    
    jadwal_tree.column("#0", width=30, anchor="center")
    jadwal_tree.column("No. Kereta", width=70, anchor="center")
    jadwal_tree.column("Stasiun Asal", width=120, anchor="center")
    jadwal_tree.column("Stasiun Tujuan", width=120, anchor="center")
    jadwal_tree.column("Jam Berangkat", width=85, anchor="center")
    jadwal_tree.column("Jam Tiba", width=85, anchor="center")

   
    for i, (no_kereta, st_asal, st_tujuan, jam_berangkat, jam_tiba) in enumerate(train_schedule, 1):
        jadwal_tree.insert("", 'end', text=str(i), values=(no_kereta, st_asal, st_tujuan, jam_berangkat, jam_tiba))

    
    jadwal_tree.place(x=50, y=100)

    buttonback = Button(window,
                        text="Main Menu",
                        command=halaman_utama,
                        font=("Times New Roman", 13),
                        fg="black",
                        state=ACTIVE)
    buttonback.place(x=90, y=360)

def halaman_pesan():
    global stasiun_berangkat, stasiun_tujuan, tanggal_keberangkatan, bulan_keberangkatan, tahun_keberangkatan, no_kereta

    labelpesan = Label(window,
                       text="PESAN TIKET KERETA",
                       font=("arial", 16)).place(x=220, y=20)

    labelasal_pesan = Label(window,
                            text="Stasiun Keberangkatan\t:",
                            font=("times new roman", 10)).place(x=30, y=80)

    
    stasiun_berangkat = StringVar(value='')
    combobox_asal = ttk.Combobox(window, 
                                 textvariable=stasiun_berangkat, 
                                 font=("times new roman", 10),
                                 width=30)
    combobox_asal.place(x=200, y=80)
    stasiun_list = ['Tawang', 'Solo Balapan', 'Kutoarjo','Lempuyangan','Klaten','Purwosari','Poncol','Kroya','Tugu', 'Purwokerto']
    combobox_asal['values'] = stasiun_list

    
    def filter_stasiun(event):
        value = combobox_asal.get().lower()
        if value == '':
            combobox_asal['values'] = stasiun_list
        else:
            filtered_stasiun = [item for item in stasiun_list if value in item.lower()]
            combobox_asal['values'] = filtered_stasiun

    combobox_asal.bind('<KeyRelease>', filter_stasiun)

    labeltujuan_pesan = Label(window,
                            text="Stasiun Tujuan\t:",
                            font=("times new roman", 10)).place(x=30, y=110)
    
    stasiun_tujuan = StringVar(value='')
    combobox_tujuan = ttk.Combobox(window, 
                                 textvariable=stasiun_tujuan, 
                                 font=("times new roman", 10),
                                 width=30)
    combobox_tujuan.place(x=200, y=110)
    combobox_tujuan['values'] = stasiun_list

    
    def filter_stasiun_tujuan(event):
        value = combobox_tujuan.get().lower()
        if value == '':
            combobox_tujuan['values'] = stasiun_list
        else:
            filtered_stasiun = [item for item in stasiun_list if value in item.lower()]
            combobox_tujuan['values'] = filtered_stasiun

    combobox_tujuan.bind('<KeyRelease>', filter_stasiun_tujuan)

    
    labeltanggal_pesan = Label(window,
                               text="Tanggal Keberangkatan\t:",
                               font=("times new roman", 10)).place(x=30, y=140)
    
    tanggal_keberangkatan = StringVar()
    combobox_tanggal = ttk.Combobox(window,
                                    textvariable=tanggal_keberangkatan,
                                    font=("times new roman", 10),
                                    width=10)
    combobox_tanggal.place(x=200, y=140)
    tanggal_list = [str(i) for i in range(1, 32)]
    combobox_tanggal['values'] = tanggal_list

   
    labelbulan_pesan = Label(window,
                             text="Bulan Keberangkatan\t:",
                             font=("times new roman", 10)).place(x=340, y=140)
    
    bulan_keberangkatan = StringVar()
    combobox_bulan = ttk.Combobox(window,
                                  textvariable=bulan_keberangkatan,
                                  font=("times new roman", 10),
                                  width=10)
    combobox_bulan.place(x=510, y=140)
    bulan_list = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    combobox_bulan['values'] = bulan_list

    
    labeltahun_pesan = Label(window,
                             text="Tahun Keberangkatan\t:",
                             font=("times new roman", 10)).place(x=340, y=170)
    
    tahun_keberangkatan = StringVar()
    combobox_tahun = ttk.Combobox(window,
                                  textvariable=tahun_keberangkatan,
                                  font=("times new roman", 10),
                                  width=10)
    combobox_tahun.place(x=510, y=170)
    tahun_list = [str(i) for i in range(2024, 2030)]
    combobox_tahun['values'] = tahun_list

    buttonback = Button(window,
                        text="Kembali",
                        command=halaman_utama,
                        font=("Times New Roman", 13),
                        fg="black",
                        state=ACTIVE).place(x=220, y=380)
    button_cari = Button(window,
                         text="Cari Tiket",
                         command=cari_tiket,
                         font=("Times New Roman", 13),
                         fg="black",
                         state=ACTIVE)
    button_cari.place(x=320, y=380)
def cari_tiket():
    global jadwal_tree
    for widget in window.winfo_children():
        widget.place_forget()

    
    label_pencarian = Label(window, text="PENCARIAN TIKET", font=("arial", 16))
    label_pencarian.place(x=220, y=20)

    
    keberangkatan = stasiun_berangkat.get()
    tujuan = stasiun_tujuan.get()
    tanggal = tanggal_keberangkatan.get()
    bulan = bulan_keberangkatan.get()
    tahun = tahun_keberangkatan.get()
    
    if not keberangkatan or not tujuan or not tanggal or not bulan or not tahun:
        messagebox.showerror("Error", "Lengkapi data pencarian")
        halaman_pesan()
        return


    hasil_pencarian = f"Stasiun Keberangkatan  : {keberangkatan}         "
    hasil_pencarian += f"Stasiun Tujuan  : {tujuan}\n"
    hasil_pencarian += f"Tanggal Keberangkatan: {tanggal} {bulan} {tahun}\n"
        
    filtered_schedule = [train for train in train_schedule if train[1] == keberangkatan and train[2] == tujuan]
    
    if filtered_schedule:
        hasil_pencarian += "Jadwal yang tersedia:"

        
        jadwal_tree = ttk.Treeview(window)
        jadwal_tree["columns"] = ("No. Kereta", "Stasiun Asal", "Stasiun Tujuan", "Jam Berangkat", "Jam Tiba")
        jadwal_tree.heading("#0", text="No.")
        jadwal_tree.heading("No. Kereta", text="No. Kereta")
        jadwal_tree.heading("Stasiun Asal", text="Stasiun Asal")
        jadwal_tree.heading("Stasiun Tujuan", text="Stasiun Tujuan")
        jadwal_tree.heading("Jam Berangkat", text="Jam Berangkat")
        jadwal_tree.heading("Jam Tiba", text="Jam Tiba")

        jadwal_tree.column("#0", width=30, anchor="center")
        jadwal_tree.column("No. Kereta", width=70, anchor="center")
        jadwal_tree.column("Stasiun Asal", width=120, anchor="center")
        jadwal_tree.column("Stasiun Tujuan", width=120, anchor="center")
        jadwal_tree.column("Jam Berangkat", width=85, anchor="center")
        jadwal_tree.column("Jam Tiba", width=85, anchor="center")
        
        for i, (no_kereta, st_asal, st_tujuan, jam_berangkat, jam_tiba) in enumerate(filtered_schedule, 1):
            jadwal_tree.insert("", 'end', text=str(i), values=(no_kereta, st_asal, st_tujuan, jam_berangkat, jam_tiba))

        
        jadwal_tree.place(x=50, y=145)

        
        def select_schedule():
            global selected_data, selected_index
    
            selected_index = jadwal_tree.selection()[0]
    
            selected_data = jadwal_tree.item(selected_index)['values']
    
            response = askokcancel("Jadwal Terpilih", f"Nomor Kereta: {selected_data[0]}\nStasiun Asal: {selected_data[1]}\nStasiun Tujuan: {selected_data[2]}\nJam Berangkat: {selected_data[3]}\nJam Tiba: {selected_data[4]}")
            if response: form()
                
            
        select_button = Button(window, text="Pilih Jadwal", command=select_schedule, font=("Times New Roman", 13), fg="black", state=ACTIVE)
        select_button.place(x=300, y=380)
    else:
        hasil_pencarian += "Tidak ada jadwal kereta yang sesuai."

    label_hasil = Label(window, text=hasil_pencarian, font=("times new roman", 12))
    label_hasil.place(x=50, y=70) 



    
    button_back = Button(window, text="Kembali", command=otw_pesan, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_back.place(x=220, y=380)
def form():
    global entry_nama, entry_hp, entry_email, entry_nomor_id,jenis_id, kelas_tiket
    for widget in window.winfo_children():
        widget.place_forget()
    label_form = Label(window, text="DATA PENUMPANG", font=("arial", 16))
    label_form.place(x=220, y=20)

    
    label_nama = Label(window, text="Nama", font=("times new roman", 12))
    label_nama.place(x=50, y=80)
    entry_nama = Entry(window, font=("times new roman", 12))
    entry_nama.place(x=240, y=80)

    
    label_hp = Label(window, text="Nomor HP", font=("times new roman", 12))
    label_hp.place(x=50, y=110)
    entry_hp = Entry(window, font=("times new roman", 12))
    entry_hp.place(x=240, y=110)

    
    label_email = Label(window, text="Email", font=("times new roman", 12))
    label_email.place(x=50, y=140)
    entry_email = Entry(window, font=("times new roman", 12))
    entry_email.place(x=240, y=140)

    
    label_nomor_id = Label(window, text="Nomor KTP/NIK/Passport:", font=("times new roman", 12))
    label_nomor_id.place(x=50, y=170)
    entry_nomor_id = Entry(window, font=("times new roman", 12))
    entry_nomor_id.place(x=240, y=170)

    
    label_jenis_id = Label(window, text="Jenis Nomor ID:", font=("times new roman", 12))
    label_jenis_id.place(x=50, y=200)

    
    jenis_id = IntVar()
    
    
   
    def set_jenis_id(value):
        jenis_id.set(value)

    
    radio_ktp = Radiobutton(window, text="KTP", variable=jenis_id, value=1, font=("times new roman", 10), command=lambda: set_jenis_id(1))
    radio_ktp.place(x=240, y=200)

    radio_nik = Radiobutton(window, text="NIK", variable=jenis_id, value=2, font=("times new roman", 10), command=lambda: set_jenis_id(2))
    radio_nik.place(x=300, y=200)

    radio_passport = Radiobutton(window, text="Passport", variable=jenis_id, value=3, font=("times new roman", 10), command=lambda: set_jenis_id(3))
    radio_passport.place(x=360, y=200)

    
    label_kelas = Label(window, text="Kelas Tiket:", font=("times new roman", 12))
    label_kelas.place(x=50, y=230)

    kelas_tiket = ttk.Combobox(window, font=("times new roman", 12), width=25)
    kelas_tiket['values'] = ("Eksekutif", "Bisnis", "Ekonomi", "Premium", "Luxury", "Sleeper")
    kelas_tiket.current(0) 
    kelas_tiket.place(x=240, y=230)

   
    label_harga = Label(window, text="Harga Tiket:", font=("times new roman", 12))
    label_harga.place(x=50, y=260)

    
    def update_harga():
        
        kelas = kelas_tiket.get()
        harga = 0
        if kelas == "Eksekutif":
            harga = 250000
        elif kelas == "Bisnis":
            harga = 120000
        elif kelas == "Ekonomi":
            harga = 70000
        elif kelas == "Premium":
            harga = 100000
        elif kelas == "Luxury":
            harga = 600000
        elif kelas == "Sleeper":
            harga = 1000000

        label_harga.config(text="Harga Tiket: Rp " + str(harga))

    
    kelas_tiket.bind("<<ComboboxSelected>>", lambda event: update_harga())

    
    update_harga()

   
    terms_text = """Ketentuan Pemesanan Tiket:
    1. Tiket yang sudah dibeli tidak dapat dibatalkan.
    2. Penukaran jadwal hanya dapat dilakukan maksimal 24 jam sebelum keberangkatan di stasiun asal.
    3. Tiket dapat dipesan maksimal 1 jam sebelum keberangkatan kereta."""
    label_terms = Label(window, text=terms_text, font=("times new roman", 10), justify=LEFT)
    label_terms.place(x=50, y=300)


    button_back = Button(window, text="Kembali", command=cari_tiket, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_back.place(x=220, y=380)

    
    button_continue = Button(window, text="Lanjut", command=lanjut_proses, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_continue.place(x=320, y=380)

def lanjut_proses():
    global entry_nama, entry_email, entry_nomor_id, entry_hp
    for widget in window.winfo_children():
        widget.place_forget()

    
    nama = entry_nama.get()
    hp = entry_hp.get()
    email = entry_email.get()
    nomor_id = entry_nomor_id.get()
    jenis_id_value = jenis_id.get()

     
    if jenis_id_value == 1:
        jenis_id_text = "KTP"
    elif jenis_id_value == 2:
        jenis_id_text = "NIK"
    elif jenis_id_value == 3:
        jenis_id_text = "Passport"
    else:
        jenis_id_text = "Unknown"

    
    kelas = kelas_tiket.get()

    
    harga = 0
    if kelas == "Eksekutif":
        harga = 250000
    elif kelas == "Bisnis":
        harga = 120000
    elif kelas == "Ekonomi":
        harga = 70000
    elif kelas == "Premium":
        harga = 100000
    elif kelas == "Luxury":
        harga = 600000
    elif kelas == "Sleeper":
        harga = 1000000

    
    keberangkatan = stasiun_berangkat.get()
    tujuan = stasiun_tujuan.get()
    tanggal = tanggal_keberangkatan.get()
    bulan = bulan_keberangkatan.get()
    tahun = tahun_keberangkatan.get()

    label_konfirmasi = Label(window, text="HALAMAN KONFIRMASI", font=("arial", 16))
    label_konfirmasi.place(x=210, y=20)
    
    confirmation_text = f"""Konfirmasi Data:
    Nama: {nama}
    Nomor HP: {hp}
    Email: {email}
    Nomor {jenis_id_text}: {nomor_id}
    Kelas Tiket: {kelas}
    Harga Tiket: Rp {harga}

    Informasi Perjalanan:
    Stasiun Asal: {keberangkatan}
    Stasiun Tujuan: {tujuan}
    Tanggal Keberangkatan: {tanggal} {bulan} {tahun}
    """
    if not nama or not hp or not email or not nomor_id or not jenis_id_value or not kelas or not harga:
        messagebox.showerror("Error", "Lengkapi data penumpang")
        form()
        return
    
    label_confirmation = Label(window, text=confirmation_text, font=("times new roman", 12), justify=LEFT)
    label_confirmation.place(x=50, y=100)
    def konfirmasi():
        yesno = askyesno("Konfirmasi","Apakah data yang anda masukan sudah benar?")
        if yesno: pembayaran()
    
    button_lanjut = Button(window, text="Lanjut", command= konfirmasi, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_lanjut.place(x=320, y=380)

    
    button_kembali = Button(window, text="Kembali", command=form, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_kembali.place(x=220, y=380)

def update_info_pembayaran(event):
    metode = metode_pembayaran.get()
    if metode == "ShopeePay":
        info_pembayaran.config(text="Nomor ShopeePay:                085640485743 a/n PT KAI Indonesia")
    elif metode == "BRI":
        info_pembayaran.config(text="Nomor Rekening BRI:             82828282828 a/n PT KAI Indonesia")

def pembayaran():
    global metode_pembayaran, info_pembayaran, harga, label_narekentry, label_norekentry
    for widget in window.winfo_children():
        widget.place_forget()
    
    label_pembayaran = tk.Label(window, text="HALAMAN PEMBAYARAN", font=("arial", 16))
    label_pembayaran.place(x=210, y=20)

    label_pilih_metode = tk.Label(window, text="Pilih Metode Pembayaran:", font=("times new roman", 12))
    label_pilih_metode.place(x=50, y=100)

    metode_pembayaran = ttk.Combobox(window, font=("times new roman", 12), width=25)
    metode_pembayaran['values'] = ("ShopeePay", "BRI")
    metode_pembayaran.current(0)  
    metode_pembayaran.place(x=240, y=100)
    metode_pembayaran.bind("<<ComboboxSelected>>", update_info_pembayaran)
    
    info_pembayaran = tk.Label(window, text="", font=("times new roman", 12))
    info_pembayaran.place(x=50, y=140)
    
    update_info_pembayaran(None)  # Initialize the info label with the current combobox selection

    label_norek = tk.Label(window, text="Nomor Rekening Anda :", font=("Times New Roman", 12))
    label_norek.place(x=50, y=170)

    label_norekentry = tk.Entry(window, font=("Times New Roman",12))
    label_norekentry.place(x=240, y=170)
    
    label_narek = tk.Label(window, text="Nama Rekening Anda :", font=("Times New Roman", 12))
    label_narek.place(x=50, y=200)

    label_narekentry = tk.Entry(window, font=("Times New Roman",12))
    label_narekentry.place(x=240, y=200)

    kelas = kelas_tiket.get()

    harga = 0
    if kelas == "Eksekutif":
        harga = 250000
    elif kelas == "Bisnis":
        harga = 120000
    elif kelas == "Ekonomi":
        harga = 70000
    elif kelas == "Premium":
        harga = 100000
    elif kelas == "Luxury":
        harga = 600000
    elif kelas == "Sleeper":
        harga = 1000000
    label_nominal = tk.Label(window, text="Nominal yang harus ditransfer : Rp ", font=("Times New Roman", 12))
    label_nominal.place(x=50, y=230)
    label_nominallabel = tk.Label(window,text= harga, font=("Times New Roman",12))
    label_nominallabel.place(x=270, y=230)

    terms_text = """Tata Cara Pembayaran:
    1. Sistem Pembayaran yang digunakan yaitu metode transfer ke Nomor Rekening kami.
    2. Pemesan menuliskan Nama dan Nomor Rekening yang digunakan untuk melakukan transfer.
    3. Setelah transfer selesai akan muncul ID Transfer / ID Pembayaran.
    4. Screenshot Bukti Pembayaran dan Simpan ID Transfer / ID Pembayaran."""
    label_terms = Label(window, text=terms_text, font=("times new roman", 10), justify=LEFT)
    label_terms.place(x=50, y=280)

    button_lanjut = tk.Button(window, text="Bayar", command=buktibayar, font=("Times New Roman", 13), fg="black", state=tk.ACTIVE)
    button_lanjut.place(x=320, y=380)

    button_kembali = tk.Button(window, text="Kembali", command=lanjut_proses, font=("Times New Roman", 13), fg="black", state=tk.ACTIVE)
    button_kembali.place(x=220, y=380)

def buktibayar():
    global label_file_path, label_identry
    def upload_file():
        global file_path
        file_path = filedialog.askopenfilename(
            filetypes=[("All Files", "*.*"), ("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            label_file_path.config(text=file_path)

    for widget in window.winfo_children():
        widget.place_forget()

    norek = label_norekentry.get()
    narek = label_narekentry.get()


    
    if not norek or not narek :
        messagebox.showerror("Error", "Lengkapi data pembayaran")
        pembayaran()
        return
    
    label_buktibayar = Label(window, text="BUKTI PEMBAYARAN", font=("arial", 16))
    label_buktibayar.place(x=215, y=20)

    button_upload = Button(window, text="Upload Bukti Pembayaran", command=upload_file, font=("Times New Roman", 13), fg="black", state=tk.ACTIVE)
    button_upload.place(x=220, y=150)
    
    label_file_path = Label(window, text="", font=("times new roman", 12))
    label_file_path.place(x=220, y=200)

    label_id        = Label(window,
                     text="ID Pembayaran / Transfer",
                     font=("Times New Roman",12))
    label_id.place(x=215, y=230)
    label_identry = Entry(window,
                          font=("Times New Roman",12))
    label_identry.place(x=215, y=260)

    button_lanjut = Button(window, text="Lanjut", command=cekupload, font=("Times New Roman", 13), fg="black", state=tk.ACTIVE)
    button_lanjut.place(x=320, y=380)
    
    button_kembali = Button(window, text="Kembali", command=pembayaran, font=("Times New Roman", 13), fg="black", state=tk.ACTIVE)
    button_kembali.place(x=220, y=380)

def cekupload():
    
    if not file_path : showwarning("UPLOAD","Mohon Upload Bukti Pembayaran"), buktibayar() 
    else : cekid()
def cekid():
    entryid = label_identry.get()
    if not entryid : showwarning("Error","Masukkan ID Pembayaran")
    else :invoice()
    
def invoice():
    
    for widget in window.winfo_children():
        widget.place_forget() 

    showinfo("Pembayaran Berhasil","Pembayaran berhasil, Terimakasih atas pemesanan anda, tiket dapat diakses di halaman My Ticket")

    natik = entry_nama.get()
    tatik = tanggal_keberangkatan.get()
    tatik2 = bulan_keberangkatan.get()
    tatik3 = tahun_keberangkatan.get()
    ketik = kelas_tiket.get()


    atik = stasiun_berangkat.get()
    tutik = stasiun_tujuan.get()
    if natik and tutik and atik and tatik and tatik2 and tatik3 and ketik  :
        mytickets.append({'name': natik ,'asal': atik,'tatik': tatik,'tatik2': tatik2,'tatik3': tatik3,'tujuan': tutik,'kelas':ketik})
        entry_nama.delete(0,END)


    
    global img
    img = PhotoImage(file="Logo4.png")  
    label_img = Label(window, image=img)
    label_img.place(x=160, y=60)  
    
    button_kembali = Button(window, text="Kembali ke Halaman Utama", command=halaman_utama, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_kembali.place(x=150, y=380)

    button_ticket = Button(window, text="Lihat Tiket", command=myticket, font=("Times New Roman",13), fg="black", state=ACTIVE)
    button_ticket.place(x=370, y=380)

def myticket():
    for widget in window.winfo_children():
        widget.place_forget()
        
    label_tiket = Label(window, text="HALAMAN TIKET", font=("arial", 16))
    label_tiket.place(x=220, y=20)
    

    if not mytickets:
        label_no_ticket = Label(window, text="Tidak ada tiket", font=("times new roman", 12))
        label_no_ticket.place(x=250, y=60)
        buttonpesan = Button(window,
                         text="Pesan Tiket Sekarang",
                         command=otw_pesan,
                         font=("Times New Roman", 13),
                         fg="black",
                         state=ACTIVE).place(x=220, y=90)

    else:
        for i, ticket in enumerate(mytickets):
            label_ticket = Label(window, text=f"Tiket {i + 1}: {ticket['name']} - {ticket['asal']} - {ticket['tujuan']} - {ticket['tatik']} {ticket['tatik2']} {ticket['tatik3']} - {ticket['kelas']}", font=("times new roman", 12))
            label_ticket.place(x=34, y=60 + (i * 60))
            
            buttondetail = Button(window,
                                  text="Detail",
                                command= detaildalam,
                                font=("Times New Roman", 13),
                                fg="black",
                                state=ACTIVE).place(x=34, y=85 + (i * 60))
            buttonpesan = Button(window,
                         text="Pesan Tiket Sekarang",
                         command=otw_pesan,
                         font=("Times New Roman", 13),
                         fg="black",
                         state=ACTIVE).place(x=34, y=380)
    
    

    button_kembali = Button(window, text="Kembali ke Halaman Utama", command=halaman_utama, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_kembali.place(x=210, y=380)

    
def detaildalam():
    
            selected_index = jadwal_tree.selection()[0]
            selected_data = jadwal_tree.item(selected_index)['values']
            nama = entry_nama.get()
    
            showinfo("Informasi Tiket", f"Nomor Kereta: {selected_data[0]}\nStasiun Asal: {selected_data[1]}\nStasiun Tujuan: {selected_data[2]}\nJam Berangkat: {selected_data[3]}\nJam Tiba: {selected_data[4]}")


class userService: 
    def __init__(self, email, password): 
        self.email = email
        self.password = password 
        self.data = { 
            "farhan@gmail.com" : { 
                "email"    : "farhan@gmail.com", 
                "password"  : "0000", 
                
            }, 
            "nasrullah@gmail.com" : { 
                "email"    : "nasrullah@gmail.com", 
                "password"  : "1234", 
                 
            } 
        } 
    
    def checkCredentials(self): 
        for value in self.data: 
            if value == self.email: 
                get_data_user = self.data[value] 
                if self.password == get_data_user['password']: 
                    return get_data_user 
                else: 
                    return False
    

    def login(self): 
        get_data = self.checkCredentials() 
        if get_data: 
            berhasillogin()
        else: 
            erorrr()

def erorrr():
    showerror("Error", "Password atau Email salah")
    halaman_login()

def halaman_login():
    global entry_password
    for widget in window.winfo_children():
        widget.place_forget()
    label_log = Label(window, text="HALAMAN LOGIN", font=("arial", 16))
    label_log.place(x=220, y=20)
    def login():
        email = entry_email.get()
        password = entry_password.get()
        user = userService(email, password)
        user.login()

    label_email = Label(window, text="Email:", font=("times new roman", 12))
    label_email.place(x=150, y=150)
    entry_email = Entry(window, font=("times new roman", 12))
    entry_email.place(x=250, y=150)

    label_password = Label(window, text="Password:", font=("times new roman", 12))
    label_password.place(x=150, y=180)
    entry_password = Entry(window, font=("times new roman", 12), show="*")
    entry_password.place(x=250, y=180)

    button_login = Button(window, text="Login", command=login, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_login.place(x=240, y=220)

    button_signup = Button(window, text="Sign Up", command=signup, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_signup.place(x=300, y=220)

def signup():
    global entry_namak, entry_hp, entry_email, entry_password
    for widget in window.winfo_children():
        widget.place_forget()
    label_sign = Label(window, text="HALAMAN SIGN UP", font=("arial", 16))
    label_sign.place(x=220, y=20)

    label_nama = Label(window, text="Nama:", font=("times new roman", 12))
    label_nama.place(x=150, y=120)
    entry_namak = Entry(window, font=("times new roman", 12))
    entry_namak.place(x=250, y=120)

    label_hp = Label(window, text="Nomor HP:", font=("times new roman", 12))
    label_hp.place(x=150, y=150)
    entry_hp = Entry(window, font=("times new roman", 12))
    entry_hp.place(x=250, y=150)

    label_email = Label(window, text="Email:", font=("times new roman", 12))
    label_email.place(x=150, y=180)
    entry_email = Entry(window, font=("times new roman", 12))
    entry_email.place(x=250, y=180)

    label_password = Label(window, text="Password:", font=("times new roman", 12))
    label_password.place(x=150, y=210)
    entry_password = Entry(window, font=("times new roman", 12), show="*")
    entry_password.place(x=250, y=210)
    button_signup = Button(window, text="Sign Up", command=berhasilsignup, font=("Times New Roman", 13), fg="black", state=ACTIVE)
    button_signup.place(x=270, y=240)
def berhasilsignup():
    namak = entry_namak.get()
    nohp = entry_hp.get()
    emil = entry_email.get()
    pw = entry_password.get()

    if not namak or not nohp or not emil or not pw :
        messagebox.showerror("Error", "Lengkapi data sign up")
        signup()
    else : berhasilsignedup()
def berhasilsignedup():
    showinfo("Signed Up","Selamat anda telah berhasil Sign Up")
    halaman_utama()
def berhasillogin():
    showinfo ("INFO","Selamat anda telah berhasil login") 
    halaman_utama()
def halaman_utama():
    for widget in window.winfo_children():
        widget.place_forget()
    buat_halaman_utama()
def error():
    showwarning ("INFO","Error, Fitur Pembatalan Tiket belum tersedia")
def about():
    showinfo("Info","Program ini merupakan Tugas Akhir Praktikum DKP oleh Farhan Nasrullah (21120123120039)")
def logout():
    response = askokcancel("Log out", "Anda yakin ingin log out dari akun ini?")
    if response : halaman_login()
def buat_halaman_utama():

    menu = Menu(window)
    itemhome = Menu(menu, tearoff=0)
    itemhelp = Menu(menu, tearoff=0)
    itemview = Menu(menu, tearoff=0)

    itemhome.add_command(label='Halaman Utama', command=halaman_utama)
    itemhome.add_command(label='Pesan Tiket', command=otw_pesan)
    itemhome.add_command(label='Batalkan Tiket', command=error)
    itemhome.add_command(label='Log out', command=logout)
    itemhelp.add_command(label='About', command= about)
    itemview.add_command(label='Jadwal Kereta', command=otw_jadwal)

    menu.add_cascade(label='Home', menu=itemhome)
    menu.add_cascade(label='View', menu=itemview)
    menu.add_cascade(label='Setting')
    menu.add_cascade(label='Help', menu=itemhelp)
    window.config(menu=menu)


    
    homepage = Label(window,
                     text="SELAMAT DATANG DI KAI JAWA",
                     font=("arial", 18))
    homepage.place(x=140, y=40)
    
    global img
    img = PhotoImage(file="train2.png")  
    label_img = Label(window, image=img)
    label_img.place(x=60, y=-50)  
    homepage = Label(window,
                     text="SELAMAT DATANG DI KAI JAWA",
                     font=("arial", 18))
    homepage.place(x=130, y=40)
    buttonsubmit = Button(window,
                          text="Lihat Jadwal Kereta",
                          command=otw_jadwal,
                          font=("Times New Roman", 13),
                          fg="black",
                          state=ACTIVE).place(x=350, y=320)

    
    buttonpesan = Button(window,
                         text="Pesan Tiket Sekarang",
                         command=otw_pesan,
                         font=("Times New Roman", 13),
                         fg="black",
                         state=ACTIVE).place(x=90, y=320)
    buttontiket = Button(window,
                         text="My Ticket",
                         command=myticket,
                         font=("Times New Roman", 13),
                         fg="black",
                         state=ACTIVE).place(x=90, y=360)


window =tk.Tk()
window.geometry("620x440")
window.title("KAI JAWA")
window.resizable(width=0, height=0)


strnama = StringVar()

halaman_login()
window.mainloop()
