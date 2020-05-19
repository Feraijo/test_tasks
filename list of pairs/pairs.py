# Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
# где None - id корневого узла.

class Node(dict):
    
    def __init__(self,*arg,**kw):
        super(Node, self).__init__(*arg, **kw)        

    def add_node(self, node_parent, node_value):
        if not node_parent:
            self.update(Node({node_value: Node({})}))
            return True
        nodes = []
        finished = []
        nodes.append(self)
        while len(nodes) > 0:
            flag = 0            
            if nodes[-1].values(): 
                parent = nodes[-1]            
            else: 
                nodes.pop()
                continue
            if node_parent in parent.keys():
                parent[node_parent].update({node_value: Node({})})
                return True
            else:
                for child in parent: 
                    if parent[child] and child not in finished: 
                        flag = 1
                        nodes.append(parent[child]) 
                        finished.append(child) 
                        break; 
            if flag == 0: 
                nodes.pop() 
        return False        

source = [
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('q', 'xcv'),
    ('b', 'b1'),
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
]

def to_tree(source):
    root = Node({})
    s = source.copy()    
    while len(s) > 0:
        s1 = s.copy()
        for val in s1:
            if root.add_node(val[0], val[1]):
                s.remove(val)
        if len(s) == len(s1):
            print(f"There is missing parent for {s1} nodes in the list. It is not possible to connect them.")
            break
    return root

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

assert to_tree(source) == expected
