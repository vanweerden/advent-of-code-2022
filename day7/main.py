from file_node import FileNode
import re

# (1) use input to map file system onto a TREE structure
def file_tree_from(file):
    with open(file) as f:
        lines = f.read().splitlines()
    
    root = FileNode("/", True)
    current = root

    for line in lines:
        # NOTE: ignores `cd /` and `ls`
        if re.match(r"\$ cd \w+", line):
            current = get_child(current, argument_from(line))
        # if "cd .." set pointer to parent of current node
        elif re.match(r'\$ cd \.\.', line):
            current = current.parent
        # else if file (<number string>): add file as child of current node (if it doesn't already have a child of that name)
        elif re.match(r"\d+ \w+", line):
            current.add_child(file_from(line, current))
        
        # else if directory (<dir string>): add dir as child
        elif re.match(r"dir .+", line):
            current.add_child(dir_from(line, current))

    return root

def argument_from(line):
    # expects command in form `$ command arg`
    result = re.search(r"\$ cd (.+)", line)
    return result.group(1)

def file_from(line, parent):
    # expects `1234 filename.txt`
    parsed = re.search(r"(\d+) (.+)", line)
    size = int(parsed.group(1))
    name = parsed.group(2)
    file = FileNode(name, False, parent, size)
    return file

def dir_from(line, parent):
    # expects `1234 filename.txt`
    parsed = re.search(r"dir (.+)", line)
    name = parsed.group(1)
    d = FileNode(name, True, parent)
    return d

def get_child(current, child_name):
    for child in current.children:
        if child.name == child_name:
            # print(f"ACTION: Moving to child '{child.name}'")
            return child
    else: # eww
        Exception(f"{child_name}' is not a child of '{current.name}'")

file_name = "test_input.txt"
tree = file_tree_from(file_name)

# (2) add up all directories whose size is greater than 10000
tree.print_children(0)
# print("Answer:", tree.find_sub_directories())