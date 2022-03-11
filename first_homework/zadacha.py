class PseudoArray:
    sled = None
    pred = None

    def __init__(self, length=0):
        self.dim = length
        self.internal = [None] * length

    def __getitem__(self, index):
        return self.internal[index]

    def __setitem__(self, index, value):
        self.internal[index] = value

    def __len__(self):
        return self.dim


class LinkedArray:
    def __init__(self):
        self.head = PseudoArray()
        self.head.pred = self.head
        self.length = 0

    def append(self, value):
        self.length += 1
        now = self.head.pred

        if self.ourind() == 0:
            last = PseudoArray(self.length)
            last.internal[0] = value
            now.sled = last
            last.pred = now
            self.head.pred = last
        else:
            now.internal[self.ourind()] = value

    def delete(self):
        if self.length == 0:
            return 0
        now = self.head.pred
        now.internal[self.ourind()] = None
        if self.ourind() == 0:
            now.pred.sled = None
            self.head.pred = now.pred
        self.length -= 1

    def get(self, index) -> object:
        if index >= self.length:
            raise Exception('Такого элемента не существует')

        now = self.head.pred
        col = self.length - self.ourind() - 1
        while col > index:
            now = now.pred
            col -= len(now)

        return now.internal[index - len(now) + 1]

    def repr(self) -> str:
        if self.length == 0:
            return ''

        now = self.head.sled
        val = [str(now.internal[0])]
        while now.sled is not None:
            val.append(' ')
            now = now.sled
            if now.sled is not None:
                col = len(now)
            else:
                col = self.ourind() + 1
            for ind in range(col):
                val.append(str(now[ind]))

        return ' '.join([j for j in val])

    def ourind(self):
        col = 1
        leng = self.length
        while leng - col > 0:
            leng -= col
            col *= 2

        return leng - 1

    def __getitem__(self, index):
        return self.get(index)

    def __repr__(self):
        return self.repr()

    def __len__(self):
        return self.length


if __name__ == '__main__':
    la = LinkedArray()
    for i in range(1, 20, 3):
        la.append(i)
        print(la)

    for i in range(5):
        la.delete()
        print(la)

    print(la[1], la[6])
