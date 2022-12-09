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