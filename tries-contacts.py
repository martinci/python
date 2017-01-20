# Tries is a data structure to store dictionaries.
# The root is a special character, say *, its children are all
# the possible first letters of words in the dictionary,
# their children are all the possible next letters and so on.
# Finally, at the end of each word we include the character '*''
# to denote that the end of a word. (not needed in this problem)
class TriesNode:
    __slots__ = ["data", "children", "children_data", "word_count"]
    def __init__(self, data):
        self.data = data
        self.children = []
        self.children_data = []
        self.word_count = 0
    
    def add_child(self, node):
        if node in self.children:
            return
        else:
            self.children.append(node)
            self.children_data.append(node.data)
        

def add(string):
    global root
    current = root
    for c in string:
        try:
            idx = current.children_data.index(c)
            current = current.children[idx]
            current.word_count+=1
        except ValueError:
            temp = TriesNode(c)
            current.add_child(temp)
            current = temp
            current.word_count+=1


def find(string):
    global root
    current = root
    for c in string:
        try:
            idx = current.children_data.index(c)
            current = current.children[idx]
        except ValueError:
            return 0
    return current.word_count

                
if __name__ == '__main__':
    n = int(input().strip())
    root = TriesNode('*')
    for _ in range(n):
        op, contact = input().strip().split()
        if op == 'add':
            add(contact)
        elif op == 'find':
            print(find(contact))
        else:
            print('Operation not recognized.')
            continue 
