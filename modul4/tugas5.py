print('\n--- Oleh L200220037 ---')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_depan(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def cari_item(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def cetak_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Membuat linked list
linked_list = LinkedList()
linked_list.tambah_di_depan(3)
linked_list.tambah_di_depan(7)
linked_list.tambah_di_depan(9)
linked_list.tambah_di_depan(2)

# Mencetak linked list
print("Linked List:")
linked_list.cetak_list()

# Mencari item di dalam linked list
item_dicari = 7
if linked_list.cari_item(item_dicari):
    print(f"Item {item_dicari} ditemukan di dalam linked list.")
else:
    print(f"Item {item_dicari} tidak ditemukan di dalam linked list.")
