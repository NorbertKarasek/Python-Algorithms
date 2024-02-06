#Tablica asocjacyjna, to taka która przechowuje pary klucz-wartość

a_dict = {} # słownik
a_dict[1776] = 'Dzień niepodległośći' # ustalamy że w indeksie 1776 jest ten łańcuch znaków <--

print(a_dict[1776])

class Actor:
    def __init__(self, name, surname, age, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.profession = profession

    def __str__(self):
        return f'My name is {self.name} {self.surname}, and im {self.age} years old. I am an {self.profession}.'

indiana = Actor('Indiana', 'Jones', 38, "Actor")

a_dict['Indiana'] = indiana
print(a_dict['Indiana'])

def count_string(a_string):
    count_dict = {}
    for char in a_string.upper():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    print(count_dict)

any_string = 'Witam pana prezesa'
count_string(any_string)

one_list = [10,20,30,40,50]
for index, n in enumerate(one_list):
    print(f'index {index} to n = {n}')

def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n #ustalamy poszukiwaną liczbę która po dodaniu do obecnie sprawdzanej da target
        if rem in a_dict: #jeżeli jest ona w słowniku to zwraca
            return index, a_dict[rem] #aktualnie sprawdzany index oraz index który jest zapisany pod poszukiwaną wartością rem w a_dict
        else:
            a_dict[n] = index #jeżeli nie to zapisuje wartość elementu pod swoim idexem

print(two_sum(one_list, 40)) # zwraca index 2 i 0 bo 30+10 = 30

doubled_word_string = 'Jako programista samouk poszukuję pracy jako programista jako'
words = doubled_word_string.split()
print(words)

def remove_doubled(a_string):
    words = a_string.split()
    sentence = []
    for word in words:
        if word not in sentence:
            sentence.append(word)
    return ' '.join(sentence) # The join() method takes a list of strings and concatenates them into a single string, separated by the specified delimiter (in this case, a space).

print(remove_doubled(doubled_word_string))

a_list = ["Cześć", "Bydlaku"]
list_to_string = ' to dorzuca między elementy listy '.join(a_list)
print(list_to_string)

def matches(a_list):
    dict = {}
    for a in a_list:
        if type(a) == str:
            dict[a] = str
        elif type(a) == int:
            dict[a] = int
        elif type(a) == float:
            dict[a] = float
        elif type(a) == bool:
            dict[a] = bool
    return dict


list = ['Cześć', 4, 2.21, True, 0b100101, bin(20)]
print(matches(list))