#Lab #7
#Due Date: 04/10/2021, 11:59PM
'''
# Collaboration Statement:

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

# ============================= COPY/PASTE your Stack class from HW3 HERE =================================

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        return self.top == None

    def __len__(self):
        l = []
        top = self.top
        while top != None:
            l.append(top)
            top = top.next
        return len(l)


    def push(self,value):
        if self.isEmpty():
            newNode = Node(value)
            self.top = newNode
        else:
            newNode = Node(value)
            newNode.next = self.top
            self.top = newNode


    def pop(self):
        if self.isEmpty():
            return None
        else:
            value = self.top.value
            self.top = self.top.next
            return value

    def peek(self):
        return self.top.value

# ============================= Section 1 =================================
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> len(x)
        2
        >>> x
        Head:Node(2)
        Tail:Node(3)
        Queue:2 -> 3
    '''
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        return self.head == None

    def enqueue(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def dequeue(self):
        if self.head == None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
        return value


    def __len__(self):
        count = 0
        temp = self.head
        while temp != None:
            temp = temp.next
            count += 1
        return count


# ============================= Section 2 =================================
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            Method uses an instance of the Queue class to process nodes

            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g = Graph(g3)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'C', 'E', 'F']

            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.bfs('Apr')
            ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
        '''
        Q = Queue()
        Q.enqueue(start)
        visited = []
        visited.append(start)
        while not Q.isEmpty():
            node = Q.dequeue()
            for x in sorted(self.vertList[node]):
                if isinstance(x, tuple):
                    x = x[0]
                if not x in visited:
                    Q.enqueue(x)
                    visited.append(x)
        return visited


    def dfs(self, start):
        '''
            Method uses an instance of the Stack class to process nodes

            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g = Graph(g3)
            >>> g.dfs('A')
            ['A', 'B', 'C', 'F', 'E', 'D']

            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.dfs('Apr')
            ['Apr', 'Bran', 'Cap', 'Flor', 'East', 'Dec']
        '''
        s = Stack()
        s.push(start)
        visited = []
        while not s.isEmpty():
            node = s.pop()
            if node not in visited:
                visited.append(node)
                newList = []
                for m in sorted(self.vertList[node]):
                    if isinstance(m, tuple):
                        m = m[0]
                    newList.append(m)
                newList = newList[::-1]
                for x in newList:
                    if x not in visited:
                        s.push(x)
        return visited
