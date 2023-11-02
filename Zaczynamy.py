n=3
for i in range(n):
    print(i)
    for j in range(n):
        print(j)

print("------------\n")


#algorytm brutalnej siły "Cyfrowa Twierdza"

import time
start = time.time()

pin = 000000
n = len(str(pin)) # ile ma cyfr
print(f"pin ma {n} cyfr/y")

for i in range (10**n):
    if i == pin:
        print(f'pin to {i}')

end = time.time()
print(start-end)

# silnia

x = 1
n = 5
for i in range(x, n+1):
    x = x * i

print(x)

