from collections import deque
bank=deque(['a','b','c'])
print(bank)
bank.popleft()
print(bank)
if not bank:
    print('empty')