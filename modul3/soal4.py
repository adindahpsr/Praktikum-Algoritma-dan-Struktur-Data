print('\n--- Oleh L200220037 ---')

class Simpul:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DaftarBerantaiGanda:
    def __init__(self):
        self.head = None

#Membuat simpul awal (poin2)
    def tambah_di_awal(self, data):
        # Membuat simpul baru
        new_node = Simpul(data)
        
        # Jika daftar kosong
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

#Membuat simpul akhir (poin 3)
    def tambah_di_akhir(self, data):
        # Membuat simpul baru
        new_node = Simpul(data)

        # Jika daftar kosong
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # Menemukan simpul terakhir
            while current.next:
                current = current.next
            # Menambahkan simpul baru setelah simpul terakhir
            current.next = new_node
            new_node.prev = current

#(poin 1)
    def cetak_maju(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def cetak_mundur(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

# Contoh penggunaan
daftar = DaftarBerantaiGanda()
daftar.tambah_di_awal(1)
daftar.tambah_di_awal(2)
daftar.tambah_di_awal(3)
daftar.tambah_di_akhir(4)
daftar.tambah_di_akhir(5)

print("Doubly Linked List dari depan:")
daftar.cetak_maju()

print("Doubly Linked List dari belakang:")
daftar.cetak_mundur()

