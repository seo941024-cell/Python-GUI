class Graph():
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def isEmpty(self):
        return len(self.vertices) == 0

    def countVertex(self):
        return len(self.vertices)

    def countEdge(self):
        count = 0
        for v in self.edges:
            count += len(self.edges[v])
        return count // 2

    def getEdge(self, u, v):
        if u in self.edges and v in self.edges[u]:
            return (u, v)
        return None

    def degree(self, v):
        if v in self.edges:
            return len(self.edges[v])
        return 0

    def adjacent(self, v):
        if v in self.edges:
            return set(self.edges[v])
        return set()

    def insertVertex(self, v):
        self.vertices.add(v)
        if v not in self.edges:
            self.edges[v] = []

    def insertEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges[u].append(v)
            self.edges[v].append(u)

    def deleteVertex(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            del self.edges[v]
            for u in self.edges:
                if v in self.edges[u]:
                    self.edges[u].remove(v)

    def deleteEdge(self, u, v):
        if u in self.edges and v in self.edges[u]:
            self.edges[u].remove(v)
            self.edges[v].remove(u)