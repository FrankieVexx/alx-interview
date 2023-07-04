#!/usr/bin/python3


# def canUnlockAll(boxes):
#     """_summary_push

#     Args:
#         boxes (): locked boxes

#     Returns:
#         boxes: unlocked boxes
#     """
#     num_of_boxes = len(boxes)
#     unlocked_boxes = [False] * num_of_boxes
#     unlocked_boxes[0] = True

#     stack = [0]

#     while stack:
#         box = stack.pop()

#         for key in boxes[box]:
#             if key < num_of_boxes and not unlocked_boxes[key]:
#                 unlocked_boxes[key] = True
#                 stack.append(key)

#     return all(unlocked_boxes)
def canUnlockAll(boxes):
    """lock boxes function"""
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # First box is unlocked

    keys_stack = boxes[0]
    while keys_stack:
        key = keys_stack.pop()
        if key < num_boxes and not unlocked_boxes[key]:
            unlocked_boxes[key] = True
            keys_stack.extend(boxes[key])

    return all(unlocked_boxes)
