class BinaryTree:
    def __init__(self, value):
        # Inicjalizuje węzeł drzewa z podaną wartością
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        # Wstawia nowy węzeł jako lewego dziecka
        if self.left_child is None:
            # Jeśli lewy dziecko nie istnieje, tworzy nowe
            self.left_child = BinaryTree(value)
        else:
            # Jeśli lewy dziecko już istnieje, wstawia nowy węzeł jako rodzica dla istniejącego lewego dziecka
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        # Wstawia nowy węzeł jako prawego dziecka
        if self.right_child is None:
            # Jeśli prawe dziecko nie istnieje, tworzy nowe
            self.right_child = BinaryTree(value)
        else:
            # Jeśli prawe dziecko już istnieje, wstawia nowy węzeł jako rodzica dla istniejącego prawego dziecka
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n):
        # Wykonuje przeszukiwanie wszerz (BFS) drzewa, aby znaleźć węzeł z daną wartością
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    # Zwraca True, jeśli znajdzie węzeł z daną wartością
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        # Zwraca False, jeśli nie znajdzie węzła z daną wartością
        return False

    def show_nodes(self):
        # Zwraca listę wszystkich węzłów w drzewie, przechodząc je w porządku wszerz
        current = [self]
        next = []
        nodes = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                nodes.append(node.key)
            current = next
            next = []
        return nodes

    def invert(self):
        # Odwraca drzewo, zamieniając miejscami lewe i prawe dziecko każdego węzła, przechodząc drzewo w porządku wszerz
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                temp = node.left_child
                node.left_child = node.right_child
                node.right_child = temp
            current = next
            next = []

    def invert_rec(self):
        # Rekurencyjnie odwraca drzewo, zamieniając miejscami lewe i prawe dziecko każdego węzła
        if self:
            change = self.left_child
            self.left_child = self.right_child
            self.right_child = change
            if self.left_child:
                self.left_child.invert_rec()
            if self.right_child:
                self.right_child.invert_rec()

    def has_leaf_nodes(self):
        # Sprawdza, czy węzeł ma jakiekolwiek dzieci (liście)
        if self.left_child or self.right_child:
            return True
        else:
            return False

    def in_order_traversal(self, node, node_list):
        # Przechodzenie drzewa w kolejności infiksowej (in-order) i zapisywanie węzłów do listy
        if node:
            self.in_order_traversal(node.left_child, node_list)
            node_list.append(node.key)
            self.in_order_traversal(node.right_child, node_list)

    def balance_tree(self):
        # Przekształcenie drzewa do listy węzłów w kolejności infiksowej
        node_list = []
        self.in_order_traversal(self, node_list)
        # Tworzenie zrównoważonego drzewa binarnego z posortowanej listy
        return self.sorted_list_to_bst(node_list)

    def sorted_list_to_bst(self, node_list):
        # Budowanie zrównoważonego drzewa binarnego z posortowanej listy węzłów
        if not node_list:
            return None
        mid = len(node_list) // 2
        root = BinaryTree(node_list[mid])
        root.left_child = self.sorted_list_to_bst(node_list[:mid])
        root.right_child = self.sorted_list_to_bst(node_list[mid + 1:])
        return root

# Przykład użycia

# Tworzenie drzewa binarnego
bt = BinaryTree(10)
bt.insert_left(5)
bt.insert_right(20)
bt.left_child.insert_left(3)
bt.left_child.insert_right(8)
bt.right_child.insert_left(15)
bt.right_child.insert_right(25)
bt.left_child.left_child.insert_left(2)
bt.left_child.left_child.insert_right(4)
bt.right_child.right_child.insert_right(30)

print("Przed równoważeniem:")
print(bt.show_nodes())

# Równoważenie drzewa
bt = bt.balance_tree()

print("Po równoważeniu:")
print(bt.show_nodes())
