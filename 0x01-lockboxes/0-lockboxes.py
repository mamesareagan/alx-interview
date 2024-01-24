#!/usr/bin/python3
'''Working with Lockboxes module
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    whyte_boxes = set([0])
    kal_boxes = set(boxes[0]).difference(set([0]))
    while len(kal_boxes) > 0:
        boxId = kal_boxes.pop()
        if not boxId or boxId >= n or boxId < 0:
            continue
        if boxId not in whyte_boxes:
            kal_boxes = kal_boxes.union(boxes[boxId])
            whyte_boxes.add(boxId)

    return n == len(whyte_boxes)
