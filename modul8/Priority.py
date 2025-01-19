print('\n--- Oleh L200220037 ---') 
import heapq

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self.qlist) == 0

    def enqueue(self, data, prior):
        heapq.heappush(self.qlist, (prior, data))
        self.qlist.sort()

    def dequeue(self):
        return self.qlist.pop(-1)

    def getFrontMost(self):
        return self.qlist[-1]

    def getRearMost(self):
        return self.qlist[0]

A = PriorityQueue()
A.enqueue("Jeruk", 4)
A.enqueue("Tomat", 2)
A.enqueue("Mangga", 0)
A.enqueue("Duku", 5)
A.enqueue("Pepaya", 2)

print(A.qlist)
A.dequeue()
print(A.qlist)

