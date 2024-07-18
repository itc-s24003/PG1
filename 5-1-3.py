form collections import deque
queue = deque([1, 2])
queue.append(3)
queue.append(4)
print('queue:', queue)
print('popleft from queue 1st value:', queue.popleft())
print('popleft from queue 2nd value:', queue.popleft())
print('queue:', queue)
