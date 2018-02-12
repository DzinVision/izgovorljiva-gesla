# Izgovoljiva Gesla
Varna gesla so osnova varnosti računalniških sistemov. Problem takih gesel je, da so velikokrat zelo kompleksna in težka za zapomniti. Ta program generira varna gesla iz slovenskih besed, zaradi česar so lahka za zapomniti. Zgledovan je po projektih:
- [xkcdpass](https://github.com/redacted/XKCD-password-generator)
- [EFF Wordlist](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)
- [Diceware Passphprase](http://world.std.com/~reinhold/diceware.html)

## Uporaba
Potrebuješ `Python 3.6`, ker program uporablja `secrets` modul. Program zaženeš z ukazom `python3 generate_password.py [n]`, kjer je `n` opcijski argument, ki pove koliko besed naj bo geslo dolgo. Torej za geslo dolžine 10 bi uporabil ukaz `python3 generate_password.py 10`. Če si zadovoljen z šestimi besedami, lahko preprosto zaženeš program brez argumenta, torej `python3 generate_password.py`.

Program `download_words.py` iz spletne strani [fran.si](http://fran.si) pridobi vse besede iz SSKJ, ki imajo vsaj 3 znake in jih brez šumnikov ter naglasov (v ASCII obliki) shrani v datoteko `all_words.py`. Za ta progrem potrebuješ pakete:
- [requests](http://docs.python-requests.org/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [unidecode](https://pypi.python.org/pypi/Unidecode/)


 Program `filter_words.py` nato iz te datoteke prebere besede in ohrani samo tiste, ki imajo največ 8 znakov. Te zapiše v datoteko `wordlist.txt`.

## Varnost Gesel
Verjetno si že slišal, da so gesla ki vsebujejo slovarske besede nevarne. To velja za gesla, ki vsebujejo samo eno besedo iz slovarja, ali pa izbirajo med omejenim številom besed. Ta program izbira med vsemi besedami v SSKJ-ju, ki so dolge vsaj 3 znake in ne presegajo 8 znakov. Takih besed je 28 774. Vsaka beseda ima potemtakem 14,8 bitov entropije, kar pomeni da ima geslo sestavljeno iz 6 naključno izbranih besed 88,8 bitov entropije. To pomeni, da bi lahko imeli 100 računalnikov, kjer bi vsak poiskusil milijardo kombinacij vsako sekundo in bi še vedno potrebovali slabih 50 milijonov let, da bi uganili naše geslo.

Več o računanju entropije gesel si lahko prebereš [tule](https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength).

## Licenca
Vsa koda v tem projektu je izdana pod [GNU GPLv3 licenco](https://github.com/DzinVision/izgovorljiva-gesla/blob/master/LICENSE).
