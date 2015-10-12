class element(object):
    def __init__(self, val, part):
        self.part = part
        self.val  = val

class elemIter(object):
    def __init__(self, elems, part):
        self.elems  = elems
        self.idx    = 0
        self.part   = part
        self.length = len(elems)

    def get_next(self):
        try:
            for i in xrange(self.idx, self.length):
                if self.elems[i].part == self.part:
                    next = self.elems[i]
                    self.idx = i + 1
                    break
            return next
        except UnboundLocalError:
            return element(-1, self.part)

    def has_next(self):
        for i in xrange(self.idx, self.length):
            if self.elems[i].part == self.part:
                return True
        return False

if __name__ == "__main__":
    elems = [element(1, 'l'), element(2, 'r'), element(3, 'l'),                \
             element(4, 'r'), element(5, 'l'), element(7, 'r')]

    it = elemIter(elems, 'l')
    while it.has_next():
        print it.get_next().val

    it = elemIter(elems, 'r')
    while it.has_next():
        print it.get_next().val


