print('\n--- Oleh L200220037 ---') 
class Stack(object):
    def __init__ (self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self,data):
        self.items.append(data)

def cetakHexa(d):
    f = Stack()
    bil_hexa = ['A','B','C','D','E','F']
    if d==0: f.push(0);
    while d!=0:
        sisa = d%16
        if (sisa>9):
            sisa = sisa-10
            sisa = bil_hexa[sisa]
           
        d=d//16
        f.push(sisa)
    st = ""
    for i in range(len(f)):
        st = st+str(f.pop())
    return st

print(cetakHexa(12))
print(cetakHexa(31))
print(cetakHexa(229))
print(cetakHexa(225))
print(cetakHexa(31519))