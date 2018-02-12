from unidecode import unidecode
from bs4 import BeautifulSoup
import requests

base_url = 'http://fran.si/iskanje?page={}&View=1&Query=*&All=*&FilteredDictionaryIds=133'

words = set()


def save(words):
    with open('all_words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')


for i in range(1, 4885):
    if i % 10 == 0:
        save(words)
        print(i)

    url = base_url.format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('span', 'font_xlarge')
    for link in links:
        if link.a is None:
            continue
        word = unidecode(link.a.text)
        if len(word) >= 3 and word.isalpha():
            words.add(word)
