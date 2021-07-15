from itertools import combinations
from math import floor, sqrt

def tsp(sub_sets, c, n):
    A = {s: [None for _ in range(n)] for s in sub_sets}
    for s in sub_sets:
        A[s][0] = float("inf")
    for s in sub_sets:
        if s == {0}:
            A[s][0] = 0
            break
    for m in range(1, n+1): # subproblem size
        for s in sub_sets:
            if len(s) == m and 0 in s:
                for j in s:
                    if j != 0:
                        A[s][j] = min(A[s.difference({j})][k] + c[k][j] for k in s if k != j)
    return min(A[frozenset({x for x in range(n)})][j] + c[j][0] for j in range(1, n))
    

def all_subsets(n):
    arr = [x for x in range(n)]
    sub_sets = []
    for i in range(n + 1):
        for element in combinations(arr, i):
            sub_sets.append(frozenset(element))
    assert len(sub_sets) == 2**n
    return sub_sets

def distances(coordinates, n):
    c = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x, y = coordinates[i]
            z, w = coordinates[j]
            c[i][j] = sqrt(((x-z)**2)+((y-w)**2))
    return c

if __name__ == "__main__":
    coordinates = []
    with open("tsp.txt", "r") as f:
        f = f.readlines()
        n = int(f[0])
        for l in f[1:]:
            x, y = [float(i) for i in l.strip().split()]
            coordinates.append((x, y))
    assert len(coordinates) == n
    sub_sets = all_subsets(n)
    c = distances(coordinates, n)
    print(floor(tsp(sub_sets, c, n))) 