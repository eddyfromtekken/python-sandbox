from typing import List


def process(arr: List[int]):
    max_val = 1
    asc = None
    current_val = 0
    current_asc = None
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_asc = True
        elif arr[i] < arr[i - 1]:
            current_asc = False
        else:
            current_asc = None

        if current_asc is None:
            current_val = 0
        elif current_asc == asc:
            current_val += 1
        else:
            current_val = 2
            
        asc = current_asc
        if current_val > max_val:
            max_val = current_val
    return max_val


print(process([1, 2, 3, 3, 2, 1, 0]))
