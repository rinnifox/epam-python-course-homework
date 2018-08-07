class Graph:
    def __init__(self, E):

        """
        E - dict(<V> : [<V>, <V>, ...])
        """
        self.E = E


class GraphIterator:

    def __init__(self, graph, start_v):
        self.graph = graph
        self.start_v = start_v
        self.used = list()
        self.queue = [start_v]
        self.successors = None

    def __iter__(self):
        return self

    def hasNext(self) -> bool:
        self.successors = self.graph.E.get(self.start_v)
        for elem in self.successors:
            if elem not in self.used:
                if elem not in self.queue:
                    self.queue.append(elem)
        if self.queue:
            return True

    def __next__(self) -> str:
        if self.hasNext():
            a = self.queue.pop(0)
            self.start_v = a
            self.used.append(a)
            return self.start_v
        else:
            raise StopIteration