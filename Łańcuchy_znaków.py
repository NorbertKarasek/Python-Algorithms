# Podstawa podstaw: String - Łańcuchy znaków

author = "Kafka"
print(author[0])  # 'K'
print(author[1])  # 'a'
print(author[2])  # 'f'
print(author[3])  # 'k'
print(author[4])  # 'a'
print(author[-1]) # 'a' - ostatni znak itd.

print('Kot' + ' ' + 'ma' + ' ' + 'Alę') # 'Kot ma Alę' - Konkatencja łańcuchów
print('Kot' * 3) # 'KotKotKot'

print(''' 
Tak możemy 
pisać w kilku 
liniach 
''')

print("Tak możemy \npisać w kilku \nliniach")
print('Aby użyć apostrofu w tekście, należy go poprzedzić znakiem \'np\'')
print('Albo poprostu używając apostrofu dla stringa, użyć "cudzysłowia" wewnątrz stringa i na odwrót')

anystring = "Ala ma kota"
print(anystring.upper()) # 'ALA MA KOTA'
print(anystring.lower()) # 'ala ma kota'
print(anystring.title()) # 'Ala Ma Kota'
print(anystring.capitalize()) # 'Ala ma kota'
print(anystring.swapcase()) # 'aLA MA KOTA'
spacestring = "    Ala ma kota    "
nospacestring = spacestring.strip() # usuwa białe znaki z początku i końca stringa
print(nospacestring) # 'Ala ma kota'
print(nospacestring) # 'Ala ma kota'

anystring1 = anystring.replace("kota", "psa")
print(anystring1) # 'Ala ma psa'

print('psa' in anystring) # False
print('kota' in anystring) # True
print('psa' in anystring1) # True
print('Potter' not in 'Harry') # True - można używać poprostu na stringu nie na zmiennych
print(anystring.startswith('A')) # True
print(anystring.startswith('Ala')) # True
print(anystring.startswith('Zbyszek')) # False
print(anystring.endswith('ta')) # True
print(anystring.index('a')) # 1 - zwraca indeks pierwszego wystąpienia podanego znaku
print(anystring.index('k')) # 7
print(anystring.find('ma')) # 4 - zwraca indeks pierwszego wystąpienia podanego stringa
print(anystring.find('kota')) # 7
try:
    print(anystring.index('q')) # ValueError: substring not found
except ValueError:
    print('substring not found')


stringlist = "Apple Banana Strawberry Onion".split() # dzieli string na listę
print(stringlist)  # ['Apple', 'Banana', 'Strawberry', 'Onion']
print(stringlist[0]) # 'Apple'
print(stringlist[1]) # 'Banana' itd.

ff = "Dwa zdania. oddzielone kropką".split(".") # w tym przypadku split() dzieli string na listę rozdzielając elementy w miejscu znaku '.'
print(ff)  # ['Dwa zdania', ' oddzielone kropką']

print(" ; ".join(stringlist)) # 'Apple ; Banana ; Strawberry ; Onion'

questions = 'Gdzie teraz? Kto teraz? Kiedy, teraz?'
# Dzielimy łańcuch po znaku zapytania, a następnie dodajemy znak zapytania z powrotem jeżeli jest co strippować
sentences = [q.strip() + '?' for q in questions.split('?') if q.strip()]

print(sentences)


name = 'William {}'
print(name)
print(name.format('Shakespeare')) # 'William Shakespeare' - metoda format() wstawia argumenty w miejsce {} w stringu
lastname = 'Shakespeare'
print(name.format(lastname)) # 'William Shakespeare'
WShakespeare = name.format(lastname)
print(WShakespeare) # 'William Shakespeare'

sentence = 'William {} urodził się w {} roku'
print(sentence.format('Shakespeare', '1564')) # 'William Shakespeare urodził się w 1564 roku'
print(sentence.format(lastname, '1564')) # 'William Shakespeare urodził się w 1564 roku'

sentence1 = 'William {1} urodził się w {0} roku' # można podać indeksy argumentów
print(sentence1.format('1564', 'Shakespeare')) # 'William Shakespeare urodził się w 1564 roku'

sentence2 = 'William {lastname} urodził się w {year} roku' # można podać nazwy argumentów
print(sentence2.format(lastname='Shakespeare', year='1564')) # 'William Shakespeare urodził się w 1564 roku'

""" {} urodził się w {} roku """\
    .format(WShakespeare, '1564') # 'William Shakespeare urodził się w 1564 roku'

inpname = input('Podaj imie: ')
inplastname = input('Podaj naziwsko: ')
inpage = input('Podaj wiek: ')

sentc = '{} {} is {} years ols'.format(inpname.capitalize(), inplastname.capitalize(), inpage)
print(sentc)

phrase = 'To długie i bardzo mądre zdanie'
print(phrase[3:9]) # 'długie' - wycina znaki od 3 do 9 - z 3 włącznie do 9 nie włącznie
print(phrase[:9]) # 'To długie' - wycina znaki od początku do 9 nie włącznie
print(phrase[9:]) # 'długie i bardzo mądre zdanie' - wycina znaki od 9 do końca włącznie
phrase_list = phrase.split() # ['To', 'długie', 'i', 'bardzo', 'mądre', 'zdanie']
print(phrase_list[2:4]) # ['i', 'bardzo'] - to samo się tyczy list, wycina elementy od 2 do 4 nie włącznie
print(phrase[:]) # 'To długie i bardzo mądre zdanie' - wycina cały string
print(phrase_list[:]) # ['To', 'długie', 'i', 'bardzo', 'mądre', 'zdanie'] - wycina całą listę
print(phrase[::2]) # 'Tdgiei bad aeezae' - wycina co drugi znak
print(phrase[::-1]) # 'einadz erdąm ozdram i eigid oT' - odwraca string
print(phrase[::-2]) # 'eia rą ozaiii T' - odwraca string i wycina co drugi znak
print(phrase_list[::-1]) # ['zdanie', 'mądre', 'bardzo', 'i', 'długie', 'To'] - odwraca listę
print(phrase_list[::-2]) # ['zdanie', 'bardzo', 'długie'] - odwraca listę i wycina co drugi element
print(phrase_list[::2]) # ['To', 'i', 'mądre'] - wycina co drugi element
print(phrase_list[::3]) # ['To', 'bardzo'] - wycina co trzeci element
print(len(phrase)) # 32 - długość stringa
print(phrase[1:32:2]) # 'odęi ad eęzne' - wycina znaki od 1 do 32 nie włącznie co drugi znak
print(phrase[0:phrase.index(' i ')]) # 'To długie' - wycina znaki od początku do indeksu ' i ' nie włącznie
print(phrase[phrase.index(' i '):]) # ' i bardzo mądre zdanie' - wycina znaki od indeksu ' i '