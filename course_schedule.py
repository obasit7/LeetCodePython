from typing import List

prereqs = [[0,1], [0,2], [1,3], [1,4], [3,4]]

# DFS method
# base cases: where some course doesn't have any prereqs
# hash map of course(key) and pre reqs as values
# Time: O(n x p) where n=num of nodes and p=num of prereqs

def can_finish(numCourses: int, prerequisites: List[List[int]]):
    prereqMap = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        prereqMap[course].append(prereq)

    # visitSet that stores all course on the current DFS path
    # to avoid loops
    visitedSet = set()
    def dfs(course):
        # base cases
        if course in visitedSet: # loop condition
            return False
        if prereqMap[course] == []: # doesn't have pre reqs so can be taken
            return True

        visitedSet.add(course)  # add to currently visiting set
        for pre in prereqMap[course]:
            if not dfs(pre): return False  # if any pre req returns false, means can't be done so return False

        visitedSet.remove(course)  # if dfs doesn't return false, means can be taken so remove from curr visiting set
        prereqMap[course] = []  # set prereqs of that course to []
        return True

    # to check for disjoint graphs
    for course in range(numCourses):
        if not dfs(course): return False
    return True

print(can_finish(5, prereqs))

