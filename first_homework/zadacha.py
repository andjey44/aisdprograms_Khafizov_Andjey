class PseudoArray:
    sled = pred = None

    def __init__(self, length):
        self.dim = length
        self.internal = [None] * length

    def __getitem__(self, index):
        return self.internal[index]

    def __setitem__(self, index, value):
        self.internal[index] = value

    def __len__(self):
        return self.dim


class LinkedArray:
    sled = pred = None

    def __init__(self):
        self.base = PseudoArray(1)
        self.base.pred = self.base
        self.length = 0

    def ourind(self):
        col, leng = 1, self.length
        while leng - col > 0:
            leng -= col
            col *= 2
        return leng - 1

    def append(self, value):
        self.length += 1
        now = self.base.pred

        if self.ourind() == 0 and self.length != 1:
            last = PseudoArray(self.length)
            last.internal[0] = value
            now.sled = last
            last.pred = now
            self.base.pred = last
        else:
            now.internal[self.ourind()] = value

    def delete(self):
        if self.length == 0:
            return 0

        now = self.base.pred
        now.internal[self.ourind()] = None
        if self.ourind() == 0:
            now.pred.sled = None
            self.base.pred = now.pred
        self.length -= 1

    def get(self, index) -> object:
        now = self.base.pred
        col = self.length - self.ourind() - 1
        while col > index:
            now = now.pred
            col -= len(now)

        return now.internal[index - len(now) + 1]

    def repr(self) -> str:
        now = self.base
        val = [str(self.base.internal[0])]
        while now.sled is not None:
            val.append(' ')
            now = now.sled
            col = len(now) if now.sled is not None else self.ourind() + 1
            for ind in range(col):
                val.append(str(now[ind]))

        return ' '.join([i for i in val])

    def __getitem__(self, index):
        return self.get(index)

    def __repr__(self):
        return self.repr()

    def __len__(self):
        return self.length


arr = LinkedArray()
for i in range(1, 15):
    arr.append(i)
    print(arr)

for i in range(8):
    arr.delete()
    print(arr)