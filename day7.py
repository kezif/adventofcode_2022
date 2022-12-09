class ContentTree():

    def __init__(self, leaf_name, depth=-1, root=None) -> None:
        self.data = []
        self.leafs = []
        self.name = leaf_name
        self.depth = depth+1
        self.root = root

        parent_folders = []
        finding_root = self
        while finding_root.root is not None:
            parent_folders.append(finding_root.name)
            finding_root = finding_root.root
        
        self.full_name = '\\'.join(parent_folders + [self.name])


    def add_leaf(self, new_leaf):
        #target_leaf = self.find_leaf(leaf_name)
        l = ContentTree(new_leaf, self.depth, self)
        self.leafs.append(l)
        return l


    def populate_leaf(self, data):
        data_n, data_v = data
        self.data.append((data_n, int(data_v)))


    def get_root(self):
        return self.root        


    @property
    def size(self):
        # this value can be calculated when new data is added
        total_size = 0
        for d in self.data:
            total_size += d[1]
        
        for leaf in self.leafs:
            total_size += leaf.size

        return total_size


    def folder_sizes(self, sizes=None):
        if sizes is None:
            sizes = {}

        sizes[self.full_name] = self.size

        for leaf in self.leafs:
            leaf.folder_sizes(sizes)

        return sizes
    

    def __str__(self) -> str:
        output_str = ''
        output_str += "  "* self.depth +  f'- {self.name} (dir)\n'

        for leaf in self.leafs:
            output_str += str(leaf)

        for d in self.data:
            d_name, d_size = d
            output_str += "  "*(self.depth+1) + f'- {d_name} (file, size={d_size})\n'

        return output_str


def parse_command(cur_leaf, line):
    command = line.split(' ')[1:]
    if command[0] == 'cd':
        if command[1] == '..':
            cur_leaf = cur_leaf.get_root()
        else:
            cur_leaf = cur_leaf.add_leaf(new_leaf=command[1])
    elif command[0] == 'ls':
        pass
    else:
        raise ValueError(f'Command {line} is not expected')
    return cur_leaf

def part_one():
    in_file = open('input\\input7.txt', 'r')
    tree = ContentTree('/')
    cur_leaf = tree
    in_file.readline() # skip first command
    for line in in_file:  # test_input[1:]:  # 
        line = line.strip()
        if line.startswith('$'):
            cur_leaf = parse_command(cur_leaf, line)    
        else:
            file = line.split(' ')
            if file[0] != 'dir':
                cur_leaf.populate_leaf((file[1], file[0]))
    in_file.close()


    #print(tree)  
    print(f'Anwser to day seven: `{sum(v for v in tree.folder_sizes().values() if v <= 100_000 )}`')
    return tree

def part_two(tree: ContentTree):
    sizes_sorted = sorted(tree.folder_sizes().values(), reverse=True)

    total_size =    70_000_000
    desired_space = 30_000_000
    used_space = sizes_sorted[0]
    # free_space    27_919_656

    to_free = desired_space - (total_size - used_space)
    #print(f'{to_free=}')
    print(f'Anwser to day seven p2: `{[v for v in sizes_sorted if v >= to_free][-1]}')  # sort out values that are smaller that expected size. Pick last value that is sorted (highest value first, so we need last)


    

if __name__ == '__main__':
    tr = part_one()
    part_two(tr)

