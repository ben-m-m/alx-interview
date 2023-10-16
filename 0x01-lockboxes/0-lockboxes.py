#!/usr/bin/python3
"""
determines if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    track which boxes are unlocked
    """
    if not boxes:
        return True  # If there are no boxes, they are all unlocked by default

    visited = [False] * len(boxes)  # List to track visited boxes
    stack = [0]  # Initialize stack with the first box(box 0 already unlocked)
    visited[0] = True

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)  # Check if all boxes have been visited
