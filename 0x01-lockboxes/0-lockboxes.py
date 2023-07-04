#!/usr/binpython3


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (): locked boxes

    Returns:
        boxes: unlocked boxes
    """
    num_of_boxes = len(boxes)
    unlocked_boxes = [False] * num_of_boxes
    unlocked_boxes[0] = True
    
    stack = [0]
    
    while stack:
        box = stack.pop()
        
        for key in boxes[box]:
            if key < num_of_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)
                
    return all(unlocked_boxes)