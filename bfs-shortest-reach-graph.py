#!/usr/bin/env python3


class Graph:
    def __init__(self, n):
        self.size = n
        # indices are 0, ..., n-1
        # initialize a grid of connections
        # default is that  nodes are connected to themselves
        self.grid = [[0] * i + [1] + [0] * (n - 1 - i) for i in range(n)]
        # auxiliary memory for distaces in number of edges.
        self.distances = {}

    def connect(self, x, y):
        self.grid[x][y] = 1
        self.grid[y][x] = 1

    def find_all_distances(self, s):
        # we need to keep track of the nodes we already visited. (Maybe we can do this with )
        processed = []
        current_layer = [s]
        layer = 0
        while True:
            next_layer = []
            # process the current layer unti it is empty
            while(current_layer != []):
                temp = current_layer.pop()
                processed.append(temp)
                # the distance from s is the curent layer
                self.distances[s, temp] = layer
                self.distances[temp, s] = layer
                # add elements to the next layer that have not been added/processed before

                def not_proc(i):
                    return i not in processed and i not in current_layer and i not in next_layer
                next_layer += [i for i in range(n) if self.grid[temp][i] and not_proc(i)]
            # next layer becomes current layer
            current_layer = next_layer
            # we have gone one level further in the graph
            layer += 1
            # if there are no elements in the next layer, it means that we are done.
            if next_layer == []:
                break
        # the result is contained in the distances dictionary.
        return None

    def print_distances(self, s, w):
        temp = []
        for i in (i for i in range(n) if i != s):
            if (s, i) in self.distances:
                temp.append(str(self.distances[s, i] * w))
            else:
                temp.append("-1")
        print(" ".join(temp))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(x) for x in input().split()]
            # indeces start at 0
            graph.connect(x - 1, y - 1)
        s = int(input())
        graph.find_all_distances(s - 1)
        # weight of edges is 6
        graph.print_distances(s - 1, 6)
