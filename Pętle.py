# Kilka podstawowych pętli w Pythonie

# Pętla for

for i in range(5): # od 0 do`
    print(i)

for i in range(1, 5): # od 1 do 4
    print(i)

for i in range(1, 10, 2): # od 1 do 9 co 2
    print(i)

name = "Python" # można iterować po stringach
for i in name:
    print(i)

people = ["John", "Paul", "George", "Ringo"]

for person in people:  # można iterować po listach, nazywamy zmienną dowolnie
    print(person.upper())  # z dowolnymi operacjami

for i,person in enumerate(people):  # w ten sposób w zmiennej i przechowujemy indeks listy
    changed = person.upper()
    people[i] = changed  # i dokonaliśmy trwałej zmiany w liście

print(people)

names = ["Britanny", "Ted", "Willy", "Albatros"]

all_names = []

for i in names:
    all_names.append(i)

for i in people:
    i = i.lower()
    i = i.capitalize()
    all_names.append(i)

print(all_names)

print('-------------------------------------')

# Pętla while

i = 0
while i < 5: # powtarza póki spełnia warunek
    print(i)
    i += 1

# break - przerywa pętlę
qs = ["What is your name?", "What is your favorite color?", "What is your quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3  # modulo zapewnia, że n będzie zawsze w zakresie 0-2

# continue - przechodzi do kolejnej iteracji

for i in range(10):
    if i % 2 == 0: # pomija liczby parzyste
        continue
    print(i)

# pass - nie robi nic, używane do zastąpienia pustego bloku
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)

print('-------------------------------------')

while input('Kontynuować ? t/n ').lower() != 'n':  # po ludzku, dopóki input jest różny od 'n'
     for i in range(1,6):
         print(i)

print('-------------------------------------')

numbers = [12,32,11,5,3,7,9,10]

while True:
        check = input('Aby wyjśc wpisz q, jeżeli nie to zgaduj liczbę od 0 do 50: ').lower()
        if check == 'q':
            break
        else:
            guess = int(check)
            if guess in numbers:
                print('Brawo, zgadłeś')
                break
            else:
                print('Spróbuj jeszcze raz')

