# contact_manager.py

# Dictionary untuk menyimpan kontak
contacts = {}

def display_contacts():
    """Menampilkan semua kontak"""
    if not contacts:
        print("Tidak ada kontak yang tersedia.")
    else:
        print("\nDaftar Kontak:")
        for name, phone in contacts.items():
            print(f"Nama: {name}, Telepon: {phone}")

def add_contact(name, phone):
    """Menambahkan kontak baru"""
    if name in contacts:
        print("Kontak sudah ada.")
    else:
        contacts[name] = phone
        print(f"Kontak {name} berhasil ditambahkan.")

def delete_contact(name):
    """Menghapus kontak berdasarkan nama"""
    if name in contacts:
        del contacts[name]
        print(f"Kontak {name} berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def main():
    while True:
        print("\n=== Manajemen Kontak Sederhana ===")
        print("1. Tambah Kontak")
        print("2. Tampilkan Kontak")
        print("3. Hapus Kontak")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            name = input("Masukkan nama kontak: ")
            phone = input("Masukkan nomor telepon: ")
            add_contact(name, phone)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Masukkan nama kontak yang ingin dihapus: ")
            delete_contact(name)
        elif choice == '4':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
