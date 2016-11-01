#!/usr/bin/env python

import sys
from queue import Queue
from collections import UserDict 

# https://docs.python.org/2/library/userdict.html
class Graph(object):
    
    def __init__(self, number=4):
        self.adj = {}
        print ("Inside graph creation...")
        for i in range (1,number+1):
            self.adj[i] = []
        print("Graph: ", self.adj)
   
    def build_graph(self, M): 
        while (M > 0):
            (x, y) = read_ints()
            self.adj[x].append(y)  # node_edges[x].append(y)
            self.adj[y].append(x)  # node_edges[y].append(x)
            M -= 1
        print ("Built graph: ", self.adj)

    def compute_distances(self, S):
        distances = {S: 0}  # distance to itself is obviously zero! 
        queue = myQueue()
        queue.put (S)   #  queue.put(S)
        while (not queue.empty()):
            print ("Queue: ", queue)
            element = queue.get() 
            distance = distances[element] + 6    # varies based on levels, 1st level = 0 + 6 
            for neighbor in self.adj[element]:   # iterate through the neighbours
                if (neighbor in distances):
                    continue                     # ignore nodes in a cycles?
                distances[neighbor] = distance   # update distance to starting node  
                print ("Distances: ", distances)   
                queue.put(neighbor)              # so its neighbours get traversed in the while loop 
        print ("Distances: ", distances)
        return distances

def read_ints():
    return [int(x) for x in sys.stdin.readline().split(" ")]


def build_graph(N, M):
    node_edges = [0]
    while (N > 0):
        node_edges.append([])
        N -= 1
    while (M > 0):
        (x, y) = read_ints()
        node_edges[x].append(y)
        node_edges[y].append(x)
        M -= 1
    print ("Edges: ", node_edges)
    return node_edges

class myQueue(Queue): 
    def __str__(self): 
        return self.queue.__str__()

def compute_distances(S, node_edges):
    distances = {S: 0}
    queue = myQueue()
    queue.put(S)
    while (not queue.empty()):
        print ("Queue: ", queue)
        element = queue.get()
        distance = distances[element] + 6
        for neighbor in node_edges[element]:
            if (neighbor in distances):
                continue
            distances[neighbor] = distance
            print ("Distances: ", distances)   
            queue.put(neighbor)
    print ("Distances: ", distances)
    return distances


def print_distances(S, N, distances):
    for i in range(1, N + 1):
        if (i == S):
            continue
        if i in distances:
            print(distances[i], end=" "),
        else:
            print(-1, end=" "),
    print()


def test_case():
    (N, M) = read_ints()
    graph = Graph(N)
    graph.build_graph(M)
    #node_edges = build_graph(N, M)
    S = int(sys.stdin.readline())
    # distances = compute_distances(S, node_edges)
    distances = graph.compute_distances(S)
    print_distances(S, N, distances)


def main():
    T = int(sys.stdin.readline())
    while (T > 0):
        test_case()
        T -= 1

if __name__ == '__main__':
    main()
