class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

class SimpleIterator2:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 100
        else:
            raise StopIteration



s_iter1 = SimpleIterator(3)
try:
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
except StopIteration:
    print('Ой, больше не могу!')

s_iter2 = SimpleIterator2(5)
for i in s_iter2:
    print(i)
    
