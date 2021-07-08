from collections import deque

'''
TODO: Let the heuristic automatically determine what nodes there are in a given graph, rather than hard coding them.
TODO: Give an optional heuristic function that can be used to determine the Node weights, with default of 1 for all nodes.
TODO: Test on large graphs.
'''

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # This is the heuristic, which assigns equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 1
        }

        return H[n]
    
    def a_star_search(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])

        # p has present dist from start to all other nodes
        p = {}
        p[start] = 0

        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # finds node with lowest f()
            for v in open_lst:
                if n == None or p[v] + self.h(v) < p[n] + self.h(n):
                    n = v;
            
            if n == None:
                print('Path does not exist')
                return None

            # if curr node is the stop, then start again from start
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)
                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    p[m] = p[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if p[m] > p[n] + weight:
                        p[m] = p[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None


adjac_lis = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 4)],
    'C': [('E', 5), ('F', 5)],
    'D': [('G', 5)],
    'E': [('G', 1)],
    'F': [('G', 4)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_search('A', 'G')