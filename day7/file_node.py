class FileNode:
    def __init__(self, name, is_directory, parent=None, size=None):
        self.name = name
        self.is_directory = is_directory
        self.parent = parent
        self.size = size
        self.children = None if not self.is_directory else []

    def add_child(self, node):
        if self.is_directory and not node.name in self.children:
            node.parent = self
            self.children.append(node)
        else:
            raise Exception("Only directories can have child nodes")
    
    def get_size(self):
        if self.is_directory:
            total_size = 0
            for child in self.children:
                total_size += child.get_size()
            return total_size
        else:
            return self.size

    def print_children(self, level):
        if self.is_directory:
            print('--' * level + ' ' + self.name + ' (dir: ' + str(self.get_size()) +')')
        else: 
            print('--' * level + ' ' + self.name + ' (file: ' + str(self.get_size()) +')')
        if self.is_directory and len(self.children) > 0:
            for child in self.children:
                child.print_children(level+1)

    def find_sub_directories(self):
        total = 0
        if self.is_directory:
            for child in self.children:
                if child.is_directory and child.get_size() <= 100000:
                    total += child.get_size() + child.find_sub_directories()
                else:
                    total += child.find_sub_directories()
        return total
