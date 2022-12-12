from typing import Type
from tqdm import tqdm

INPUT_PATH = 'input\\input12.txt'

test_input = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split('\n')

import heapq

class Node():
    def __init__(self, height, i, j) -> None:
        self.height = height
        self.gcost = 0
        self.hcost = 0
        self.pos = i,j
        self.parent = None
    
    @property
    def fcost(self):
        return self.gcost + self.hcost

    def __repr__(self) -> str:
        return f'{self.height} {self.pos}'
    
    def __str__(self) -> str:
        return f'{self.height} {self.pos}'

    def neighbours(self, nodes):
        # return neighbours and check for out of index
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0 or abs(i) + abs(j) > 1:  # second statement to get only left right up down
                    continue 
                nei_i, nei_j = self.pos[0] + i, self.pos[1] + j
                if  0 <= nei_i < len(nodes) and 0 <= nei_j < len(nodes[0]):
                    yield  nodes[nei_i][nei_j]
        return self

    def walkable(self, other):
        return self.height - 1 <= other.height

    def distance(self, other):
        s_i, s_j = self.pos
        o_i, o_j = other.pos
        return abs(s_i - o_i) + abs(s_j - o_j)

    def __gt__(self, other):
        return other.fcost < self.fcost or (other.fcost == self.fcost and other.fcost < self.fcost)
         

def retrace_path(start_node, end_node):
    path = []
    current = end_node
    while current != start_node:
        path.append(current)
        current = current.parent
        
    return path


def astar(nodes, start_pos, target_pos):
    def get(arr, idx):
        return arr[idx[0]][idx[1]]

    start = get(nodes,start_pos)
    target = get(nodes,target_pos)
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, start)
    
    while len(open_set) > 0 :
        current = heapq.heappop(open_set)
        closed_set.add(current)
    
        if current.pos == target.pos:
            return retrace_path(start, target)

        for neighbour in  current.neighbours(nodes):
            if  (not neighbour.walkable(current)) or (neighbour in closed_set):
                continue

            new_cost_to_neighbour = current.gcost + current.distance(neighbour)
            if new_cost_to_neighbour < neighbour.gcost or not (neighbour in open_set):
                neighbour.gcost = new_cost_to_neighbour
                neighbour.hcost = neighbour.distance(target)

                neighbour.parent = current
                if not (neighbour in open_set):
                    heapq.heappush(open_set, neighbour)
              


def part_one(data: list[str]):
    elevation = []
    start_pos = 0,0
    target_pos = 0,0
    for i, line in enumerate(data):
        if 'S' in line:
            start_pos = i, line.index('S')
            line = line.replace('S', 'a')
        if 'E' in line:  
            target_pos = i, line.index('E')  
            line = line.replace('E', 'z')
        
        elevation.append([Node(ord(c) -97, i, j) for j, c in enumerate(line)])

    res = astar(elevation, start_pos, target_pos)

    print(f'Anwser to day twelve: `{len(res)}`') 


    

def part_two(data):
    import re
    elevation = []
    start_poses = []
    target_pos = 0,0
    for i, line in enumerate(data):
        if 'S' in line:
            #start_pos = i, line.index('S')
            line = line.replace('S', 'a')
        if 'E' in line:  
            target_pos = i, line.index('E')  
            line = line.replace('E', 'z')
        if 'a' in line:
            pos = [(i, m.start()) for m in re.finditer('a', line)]  # find position of all a's
            start_poses.extend(pos)
        
        elevation.append([Node(ord(c) -97, i, j) for j, c in enumerate(line)])


    results = []
    for pos in tqdm(start_poses):
        res = astar(elevation, pos, target_pos)
    
        if res is not None:
            results.append((len(res), res))

    results = sorted(results, key=lambda lv: lv[0])
    print(results[0])
    print(f'Anwser to day twelve p2: `{results[0][0]}`') 


if __name__ == '__main__':
    data = [line.strip() for line in test_input]

    with open(INPUT_PATH, 'r') as file:
        data = [line.strip() for line in file.readlines()]

    
    part_one(data)
    part_two(data)
        