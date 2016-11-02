#!/usr/bin/env python

import sys
from queue import Queue
from collections import namedtuple, defaultdict

# Struct for edges.
Edge = namedtuple('Edge', ['src', 'dest'])

class myQueue(Queue): 
    def __str__(self): 
        return self.queue.__str__()

# https://docs.python.org/2/library/userdict.html
class Graph(object):
    
    def __init__(self, N=4):
        '''
        The class implementation uses Adjacency list, one of the 
        two commonly adopted methods (http://j.mp/graphADT)
        '''
        self.N   = N                 # might be useful later
        self.Adj = defaultdict(list) # default the value of any key to a list       
        print("Graph initialized: ", self.Adj)
   
    def build_graph(self, M): 
        while (M > 0):
            x, y = read_ints()
            edge = Edge(x,y)
            self.Adj[edge.src ].append(edge.dest)  
            self.Adj[edge.dest].append(edge.src)
            M -= 1
        print ("Graph built: ", self.Adj)

    def compute_distances(self, S):
        distances = {S: 0}  # distance to itself is obviously zero! 
        queue = myQueue()
        queue.put (S)   #  queue.put(S)
        while (not queue.empty()):
            print ("Queue: ", queue)
            element = queue.get() 
            distance = distances[element] + 6    # varies based on levels, 1st level = 0 + 6 
            for neighbor in self.Adj[element]:   # iterate through the neighbours
                if (neighbor in distances):
                    continue                     # ignore nodes in a cycles?
                distances[neighbor] = distance   # update distance to starting node  
                print ("Distances: ", distances)   
                queue.put(neighbor)              # so its neighbours get traversed in the while loop 
        print ("Distances: ", distances)
        return distances

def read_ints():
    return [int(x) for x in sys.stdin.readline().split(" ")]

def print_distances(S, N, distances):
    for i in range(1, N + 1):
        if (i == S):
            continue  # to mute the printing of distance (aka 0) to itself
        if i in distances:
            print(distances[i], end=" "),
        else:
            print(-1, end=" "),
    print()


def test_case():
    (N, M) = read_ints()
    graph = Graph(N)               # with placeholders for N vertices
    graph.build_graph(M)           # process M edges as (src, dest) 
    S = int(sys.stdin.readline())  # Get the Starting node for which distances will be calculated
    distances = graph.compute_distances(S)
    print_distances(S, N, distances)


def main():
    T = int(sys.stdin.readline())
    while (T > 0):
        test_case()
        T -= 1

if __name__ == '__main__':
    main()
