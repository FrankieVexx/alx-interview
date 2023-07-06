#!/usr/bin/python3
'''returns true if lockboxes can all be opened and false if not'''


def join(list1, list2):
    results = []
    for numb in list2:
        results += list1[numb]
    return results


def canUnlockAll(boxes):
    '''returns true of locboxes can all be opened and false if not'''
    index = 0
    total = list(set(boxes[0]) | {0})
    new = True
    while new:
        new = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                new = True
        return len(total) == len(boxes)
    