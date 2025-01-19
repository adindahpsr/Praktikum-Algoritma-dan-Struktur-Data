print('\n--- Oleh L200220037 ---') 
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self.qlist) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty()
        k = []
        for i in self.qlist:
            k.append(i.priority)
        x = k.index(min(k))
        return self.qlist.pop(x).item

A = PriorityQueue()
A.enqueue("Jeruk", 4)
A.enqueue("Tomat", 2)
A.enqueue("Mangga", 0)
A.enqueue("Duku", 5)
A.enqueue("Pepaya", 2)

print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
