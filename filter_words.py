out = open('wordlist.txt', 'w')

with open('all_words.txt') as f:
    for word in f.readlines():
        if len(word) <= 8:
            out.write(word)

out.close()
