#!/usr/bin/env python3


def is_out_of_bounds(idx):
    i, j = idx
    if i < 0 and i >= n:
        return True
    if j < 0 and j >= m:
        return True
    return False


def full_neighbors(i, j):
    neighbors = []
    for k in range(3):
        for l in range(3):
            if is_out_of_bounds([i - 1 + k, j - 1 + l]):
                continue
            if [i - 1 + k, j - 1 + l] in ones:
                neighbors.append([i - 1 + k, j - 1 + l])
    return neighbors


def get_region(i, j):
    # we start with one element and add the full neighbors to a stack.
    # when each element is retrieved from the stack it is added to the region.
    # we continue until there are no more elements to process.
    region = []
    stack = [[i, j]]
    while(stack != []):
        idx = stack[0]
        del stack[0]
        region.append(idx)
        neighbors = full_neighbors(idx[0], idx[1])
        for idx in neighbors:
            if idx not in stack and idx not in region:
                stack.append(idx)
    return region


def get_all_regions(M):
    regions = {}
    processed = []
    for i, j in ones:
        # to avoid duplicate regions
        if [i, j] in processed:
            continue
        # process stack
        temp = get_region(i, j)
        processed += temp
        regions[tuple(temp[0])] = len(temp)
    return regions


if __name__ == '__main__':
    # read data
    n = int(input())
    m = int(input())
    M = []
    # lists with all the indexes that are zero and ones respectively
    zeros = []
    ones = []
    for i in range(n):
        temp = map(int, input().split())
        temp = list(temp)
        for j in range(m):
            if temp[j] == 0:
                zeros.append([i, j])
            else:
                ones.append([i, j])
        M.append(temp)
    # get_regions gives us a dictionary with the sizes of regions as
    # values. The key is a (unique) representative according to lexicographic order
    regions = get_all_regions(M)
    print(max(regions.values()))
