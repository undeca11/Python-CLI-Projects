class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.len = 0
    
    def set_head(self, data):
        _new_node = Node(data)
        if self.head != None:
            _new_node.next = self.head
        self.head = _new_node
        self.len += 1
    
    def append(self, data):
        if self.head == None:
            self.sethead(data)
        else:
            _new_node = Node(data)
            _current_node = self.head
            while _current_node.next != None:
                _current_node = _current_node.next
            _current_node.next = _new_node
            self.len += 1
    
    def insert(self, data, index: int):
        if index == 0:
            self.sethead(data)
        else:
            _new_node = Node(data)
            pos = 0
            _current_node = self.head
            while pos+1 != index and _current_node != None:
                _current_node = _current_node.next
                pos += 1
            if _current_node != None:
                _new_node.next = _current_node.next
                _current_node.next = _new_node
                self.len += 1
            else: raise IndexError('Index out of range')
    
    def update(self, data, index):
        pos = 0
        _current_node = self.head
        while pos != index:
            if _current_node != None:
                _current_node = _current_node.next
                pos += 1
            else: raise IndexError('Index out of range')
        _current_node.data = data

    def index(self, data):
        index = 0
        _current_node = self.head
        while _current_node != None:
            if _current_node.data == data:
                return index
            else:
                _current_node = _current_node.next
                index += 1
        raise IndexError('Index out of range')

    def node(self, index):
        pos = 0
        _current_node = self.head
        while pos != index:
            _current_node = _current_node.next
            pos += 1
        if _current_node != None:
            return _current_node.data 

    def count(self, value):
        _current_node = self.head
        count = 0
        while _current_node != None:
            if _current_node.data == value:
                count += 1
            _current_node = _current_node.next
        return count

    def pop(self, index = -1):
        if self.head == None:
            raise IndexError('List is empty')
        if index < -1:
            raise IndexError('No negative index allowed')
        if index > self.len:
            raise IndexError('Index out of range')
        elif index == self.len:
            index = -1
        match index:
            case 0:
                head = self.head
                self.head = self.head.next
                head.next = None
                self.len -= 1
            case -1:
                _current_node = self.head
                while _current_node.next.next != None:
                    _current_node = _current_node.next
                _current_node.next = None
                self.len -= 1
            case _:
                _current_node = self.head
                pos = 0
                while pos+1 != index and _current_node != None:
                    _current_node = _current_node.next
                    pos += 1
                if _current_node != None:
                    target = _current_node.next
                    _current_node.next = _current_node.next.next
                    target.next = None
                else: raise IndexError('Index out of range')

    def extend(self, iterable):
        for i in iterable:
            self.append(i)
    
    def clear(self):
        if self.head == None:
            raise IndexError('List is already empty')
        while self.len > 1:
            self.pop()
        self.pop(0)

    def remove(self, data):
        index = self.index(data)
        if isinstance(index, int):
            self.pop(index)
        
    def __len__(self):
        return self.len

    def __iter__(self):
        _current_node = self.head
        return _current_node.data
    
    def __next__(self):
        if _current_node.next != None:
            _current_node = _current_node.next
            return _current_node.data
    
    def __str__(self):
        _current_node = self.head
        list = []
        while _current_node != None:
            list.append(_current_node.data)
            _current_node = _current_node.next
        return str(list)
    
test = LinkedList()
test.clear()