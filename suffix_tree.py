def indent(depth):
    for i in xrange(depth):
        print(' ',)

class Edge:
    # string should be a slice of a string (so that no copy is made)
    def __init__(self, string, source=None, dest=None):
        self.string = string
        self.source = source
        self.dest = dest

    def split(self, edge_offset):
        e_a = Edge(self.string[:edge_offset])
        e_b = Edge(self.string[edge_offset:])
        intermediate_node = Node(parent_edge=self,character_depth=self.source.character_depth+edge_offset)
        # self.source --> intermediate_node (via e_a)
        e_a.source = self.source
        e_a.dest = intermediate_node
        # intermediate_node --> self.dest (via e_b)
        e_b.source = intermediate_node
        e_b.dest = self.dest
        self.dest.parent_edge = e_bintermediate_node.set_edge_by_leading_character(e_b)
        e_b.dest.parent_edge = e_b# overwrite self so that anything that references this edge stayscurrent:
        self.source = e_a.source
        self.dest = e_a.dest
        self.string = e_a.string
        return self,e_b

    def print_helper(self, depth):
        indent(depth)
        print('-->',self.string)
        self.dest.print_helper(depth+1)

class Node:
    number_nodes=0
    def __init__(self, parent_edge=None, character_depth=None):
        self.parent_edge = parent_edge
        self.character_depth = character_depth
        self.first_char_to_edge = {}
        self.unique_id = Node.number_nodes
        Node.number_nodes += 1

    def parent(self):
        return self.parent_edge.source

    def set_edge_by_leading_character(self, edge):
        first_edge_char = edge.string[0]
        self.first_char_to_edge[first_edge_char] = edge
        edge.source = self
    def print_helper(self, depth):
        indent(depth)
        print ('@',self.character_depth)
        for e in self.first_char_to_edge.values():
            e.print_helper(depth+1)

    def is_root(self):
        return self.parent() == self

    def label(self):
        result = ""
        if not self.is_root():
            result = self.parent().label()
            result += self.parent_edge.string
        return result
