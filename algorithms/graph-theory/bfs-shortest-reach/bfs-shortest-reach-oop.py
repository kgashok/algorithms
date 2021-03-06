#!/usr/bin/env python

import sys
import pprint
from queue import Queue
from collections import namedtuple, defaultdict
    
# Struct for edges.
Edge = namedtuple('Edge', ['src', 'dest'])

class myQueue(Queue): 
    def __str__(self): 
        return self.queue.__str__()

class Graph(object):
    
    def __init__(self, N):
        '''
        The class implementation uses Adjacency list, one of the 
        two commonly adopted methods (http://j.mp/graphADT)
        '''
        self.N   = N                 # might be useful later
        self.Adj = defaultdict(list) # default the value of any key to a list       
        print("Graph initialized: ", self.Adj)
   
    def isConnected(self):
        return len(self.Adj) == 1 or self.N == len(self.Adj)
    
    def addEdge (self, edge): 
        self.Adj[edge.src ].append(edge.dest)  
        self.Adj[edge.dest].append(edge.src)
    
    def addEdges(self, M): 
        while (M > 0):
            x, y = read_ints()
            self.addEdge (Edge(x, y)) 
            M -= 1
        print ("Graph built: ")
        pprint.pprint (self.Adj, indent=2, width=20)

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
        print ("Distances for ", S)
        pprint.pprint (distances, indent=2, width=10)
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
    graph.addEdges(M)              # process M edges as (src, dest) 
    S = int(sys.stdin.readline())  # Get the Starting node for which distances will be calculated
    distances = graph.compute_distances(S)
    print_distances(S, N, distances)
    print( "Is it a connected graph? ", graph.isConnected() )

def main():
    T = int(sys.stdin.readline())
    count = 1
    while (T > 0):
        print("Running test ", count)
        test_case()
        T -= 1
        count += 1

if __name__ == '__main__':
    main()
