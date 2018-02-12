import sys
import secrets

n = 6

if len(sys.argv) > 1:
    n = int(sys.argv[1])

words = []
with open('wordlist.txt') as f:
    for word in f.readlines():
        words.append(word)

selected = []
while len(selected) < n:
    word = secrets.choice(words)
    if word not in selected:
        selected.append(word)

print(' '.join(map(lambda x: x.replace('\n', ''), selected)))
