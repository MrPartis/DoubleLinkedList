import random

class Node:
    def __init__(self, value, left = None, right = None):
        self.__dat = value
        self.r = right
        self.l = left
    def getDat(self):
        return self.__dat

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0
    def add(self, value, _at = None):
        if _at is None:
            _at = self.__size
        if _at == self.__size:
            if (_at == 0):
                self.head = Node(value)
                self.tail = self.head
            else: 
                self.tail.r = Node(value, self.tail)
                self.tail = self.tail.r
        else:
            n = self.head
            for i in range(_at):
                n = n.r
            n.l.r = Node(value, n.l, n)
            n.l = n.l.r
        self.__size += 1
    def __del__(self):
        at = self.tail
        while (at != None and at != self.head):
            at = at.l
            sac = at.r
            del sac
        del at
        self.head = None
        self.tail = None
        self.__size = 0
    def remove(self, _at):
        if _at >= self.__size:
            return
        if _at == 0:
            self.head = self.head.r
            self.head.l = None
        elif _at == self.__size - 1:
            self.tail = self.tail.l
            self.tail.r = None
        else:
            n = self.head
            for i in range(_at):
                n = n.r
            n.l.r = n.r
            n.r.l = n.l
        self.__size -= 1
    def sort(self):
        if self.__size <= 1:
            return

        # Find the maximum number to know the number of digits
        max_val = self.head.getDat()
        current = self.head.r
        while current is not None:
            if current.getDat() > max_val:
                max_val = current.getDat()
            current = current.r

        exp = 1
        while max_val // exp > 0:
            self.__counting_sort(exp)
            exp *= 10

    def __counting_sort(self, exp):
        output = [0] * self.__size
        count = [0] * 10

        current = self.head
        while current is not None:
            index = (current.getDat() // exp) % 10
            count[index] += 1
            current = current.r

        for i in range(1, 10):
            count[i] += count[i - 1]

        current = self.tail
        while current is not None:
            index = (current.getDat() // exp) % 10
            output[count[index] - 1] = current.getDat()
            count[index] -= 1
            current = current.l

        current = self.head
        for i in range(self.__size):
            current._Node__dat = output[i]
            current = current.r

    def __getitem__(self, index):
        if index >= self.__size or index < 0:
            raise IndexError("OUT_OF_RANGE")
        current = self.head
        for i in range(index):
            current = current.r
        return current.getDat()

    def __setitem__(self, index, value):
        if index >= self.__size or index < 0:
            raise IndexError("OUT_OF_RANGE")
        current = self.head
        for i in range(index):
            current = current.r
        current._Node__dat = value
    def getHead(self):
        return self.head
    def getTail(self):
        return self.tail
    def getSize(self):
        return self.__size
    def print(self):
        n = self.head
        print('(',end = '')
        for i in range(self.__size):
            print(n.getDat(), end = '')
            n = n.r 
            if (n != None):
                print(', ',end = '')
        print(')')
