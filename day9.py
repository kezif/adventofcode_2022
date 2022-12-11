from math import copysign

test_input = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.split('\n')
    
def update_tail(head_pos, tail_pos):
    head_pos_x, head_pos_y = head_pos
    tail_pos_x, tail_pos_y = tail_pos
    distance = abs(head_pos_x - tail_pos_x), abs(head_pos_y - tail_pos_y)
    if sum(distance) > 2:  # if distance is more or eq 3 than thats mean that we are in the diagonal situation
        #print('   diagonal')
        tail_pos_x = tail_pos_x + int(copysign(1, (head_pos_x - tail_pos_x))) 
        tail_pos_y = tail_pos_y + int(copysign(1, (head_pos_y - tail_pos_y)))
    elif distance[0] > 1:
        tail_pos_x = tail_pos_x + (head_pos_x - tail_pos_x) //2
    elif distance[1] > 1:
        tail_pos_y = tail_pos_y + (head_pos_y - tail_pos_y) //2
    
    return tail_pos_x, tail_pos_y

def part_one():
    data = [line.strip().split(' ') for line in test_input]

    with open('input\\input9.txt', 'r') as file:
        data = [line.strip().split(' ') for line in file.readlines()]
    
    history_pos = []
    head_pos = 0,0
    tail_pos = 0,0
    for dire, coun in data:
        #print( dire, coun )
        for _ in range(int(coun)):
            if dire == 'R':
                head_pos = (head_pos[0], head_pos[1]+1)
            if dire == 'U':
                head_pos = (head_pos[0]+1, head_pos[1])
            if dire == 'L':
                head_pos = (head_pos[0], head_pos[1]-1)
            if dire == 'D':
                head_pos = (head_pos[0]-1, head_pos[1])

            tail_pos = update_tail(head_pos, tail_pos)
            history_pos.append(tail_pos)

    print(f'Anwser to day nine: `{len(set(history_pos))}`')

    

def part_two():
    data = [line.strip().split(' ') for line in test_input]

    with open('input\\input9.txt', 'r') as file:
        data = [line.strip().split(' ') for line in file.readlines()]
    
    history_pos = []
    head_pos = 0,0
    tails_pos = [(0,0) for _ in range(9)]
    for dire, coun in data:
        #print( dire, coun )
        for _ in range(int(coun)):
            if dire == 'R':
                head_pos = (head_pos[0], head_pos[1]+1)
            if dire == 'U':
                head_pos = (head_pos[0]+1, head_pos[1])
            if dire == 'L':
                head_pos = (head_pos[0], head_pos[1]-1)
            if dire == 'D':
                head_pos = (head_pos[0]-1, head_pos[1])

                
            tails_pos[0] = update_tail(head_pos, tails_pos[0])
            for i in range(1,9):
                tails_pos[i] = update_tail(tails_pos[i-1], tails_pos[i])

            history_pos.append(tails_pos[i])

    print(f'Anwser to day nine p2: `{len(set(history_pos))}`')

if __name__ == '__main__':
    part_one()
    part_two()