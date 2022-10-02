# use a set to keep track of nodes visited
# if node repeated -> loop, not a tree
# if num of nodes = num of nodes visited: is tree

def is_tree(n, edges):
    if not n:
        return True

    # make adjacency list
    adjacency_list = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adjacency_list[n1].append(n2)
        adjacency_list[n2].append(n1)

    visited = set()
    def dfs(i, prev):
        if i in visited:  # loop situation
            return False
        visited.add(i)
        for j in adjacency_list[i]:
            if j == prev:  # to detect false negative
                continue
            if not dfs(j, i):
                return False
        return True

    return dfs(0, -1) and n == len(visited)

# Time and memory : O(e + v)

