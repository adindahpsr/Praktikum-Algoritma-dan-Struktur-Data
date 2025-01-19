print('\n--- Oleh L200220037 ---') 
class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self.qlist) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty()
        return self.qlist.pop(0)

    def getFrontMost(self):
        return self.qlist.pop(0)

    def getRearMost(self):
        return self.qlist.pop(-1)

A = Queue()
A.enqueue("Jeruk")
A.enqueue("Tomat")
A.enqueue("Mangga")
A.enqueue("Duku")
A.enqueue("Pepaya")
A.enqueue("Kelengkeng")

front = A.getFrontMost()
rear = A.getRearMost()
print("Nilai maksimal = ", front)
print("Nilai minimal = ", rear)
