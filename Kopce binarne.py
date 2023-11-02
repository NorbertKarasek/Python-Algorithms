from heapq import heapify, heappop, heappush

import Drzewa_binarne

a_list = ['R','C','T','H','E','D','L']
heap = heapify(a_list)
print(a_list)
# ['C', 'E', 'D', 'H', 'R', 'T', 'L']

print('pobieramy element')
heappop(a_list)
print(a_list)
#['D', 'E', 'L', 'H', 'R', 'T']

print('pobieramy wszystkie klucze')
while len(a_list) > 0:
    print(heappop(a_list))

print('\nDrugi kopiec')
b_list = ['D','E','L','H','R','T']
heapify(b_list)
print(b_list)
heappush(b_list, 'Z')
print(b_list)

print('\nZadanie')
#to długośći lin, trzeba je wszystkie połączyć a za każdym razem koszt łączenia jest taki jak suma długośći lin.
lenght = [5,4,2,8]
def find_min_cost(ropes):
    heapify(ropes)
    cost = 0
    while len(ropes) > 1: # powtarza aż zostanie jedna długość
        sum = heappop(ropes) + heappop(ropes) # zabiera dwa najmniejsze klucze
        heappush(ropes, sum) # spowrotem do kopca dorzuca sumę najmniejszych kluczy
        cost += sum # dodaje koszt każdej operacji do kosztu łącznego
    return cost

print(find_min_cost(lenght))

#WYZWANIE, napisz funkcje która zwraca true jeżeli drzewo binarne jest kopcem minimalnym, false jezeli nie!

tree = Drzewa_binarne.BinaryTree(1)
tree.insert_left(4)
tree.insert_left(2)
tree.insert_right(6)
tree.insert_right(3)
tree.right_child.insert_left(5)
tree.right_child.left_child.insert_left(7)


def isheap_min(tree):
    atree = tree.show_nodes()
    tree = tree.show_nodes()
    heapify(tree)
    if atree == tree:
        return True
    else:
        return False

print(isheap_min(tree))
print(type(isheap_min(tree)))