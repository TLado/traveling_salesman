from math import floor, sqrt
from bitarray import bitarray

def tsp(sub_sets, c, n):
    A = {s: [None for _ in range(n)] for s in sub_sets}
    for s in sub_sets:
        A[s][0] = float("inf")
    for s in sub_sets:
        if s == "1" + "0"*(n-1):
            A[s][0] = 0
            break
    for m in range(1, n+1): # subproblem size 
        print(f"{n+1-m} iteration(s) remaining")
        for s in sub_sets:
            s_nodes =  {int(i):int(i) for i, j in enumerate(s) if int(j)} # internal nodes
            if len(s_nodes) == m and 0 in s_nodes:
                for i in s_nodes:
                    if i != 0:
                        s_prime = "".join(b if j!=i else "0" for j, b in enumerate(s))
                        A[s][i] = min(A[s_prime][k] + c[k][i] for k in s_nodes if k != i)
    return min(A["1"*n][j] + c[j][0] for j in range(1, n))
    
def bitmasks(n, m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield bitarray([1]) + x
            for x in bitmasks(n-1,m):
                yield bitarray([0]) + x
        else:
            yield n * bitarray('0')
    else:
        yield n * bitarray('1')

def all_subsets(n):
    sub_sets = []
    for i in range(n+1):
        for b in bitmasks(n, i):
            sub_sets.append(b.to01())
    assert len(sub_sets) == 2**n
    print("Computed subsets...")
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