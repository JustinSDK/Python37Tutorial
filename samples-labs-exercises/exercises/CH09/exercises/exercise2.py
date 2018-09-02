from collections import deque

def is_reversed_word(word: str) -> bool:
    d = deque(word)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True

words = ['RADAR', 'WARTER START', 'MILK KLIM', 'RESERVERED','IWI', "ABBA"]
for word in words:
    if is_reversed_word(word):
        print(word)