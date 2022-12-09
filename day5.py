

transpose = lambda l: list(map(list, zip(*l)))

def print_bb(boxes):
    formated_str = []
    for i, v in enumerate(boxes):
            print(i+1 , v)
            formated_str.append(str(i+1) + str(v)) 
    return '\n'.join(formated_str)

def swap(array, col_i = 9):
    # convert from
    # [[_ A _]
    #  [B C D]]
    # to
    # [[_ B]
    #  [A C] 
    #  [_ D]]
    slots = [[] for _ in range(col_i)]
    for row in array:
        for i, value in enumerate(row):
            if value != '':
                slots[i].insert(0, value)
    return slots

def move_boxes(boxes, count, from_i, to_i):
    from_i, to_i = from_i-1, to_i-1
    for _ in range(count):
        to_insert = boxes[from_i].pop()
        boxes[to_i].append(to_insert)

def move_boxes2(boxes, count, from_i, to_i):
    from_i, to_i = from_i-1, to_i-1
    to_insert = boxes[from_i][-count:]
    del boxes[from_i][-count:]    
    boxes[to_i].extend(to_insert)


def part_one():
    with open('input\\input5.txt', 'r') as file:
        initial = []
        for i in range(8):
            line = file.readline()#.replace(' ', '.')
            n= 4
            chunk = [line[i:i+n].replace('[',' ').replace(']',' ').strip() for i in range(0, len(line), n)]  # separate into chunks of 4 charecters wide, remove [] and spaces
            initial.append(chunk)  # so we would get a row with only box labels

        
        stacks = swap(initial)
        
        _ = file.readline() # pass indexes
        _ = file.readline() # pass newline


        for line in file:
            directions = [int(w) for w in line.strip().split(' ') if w.isdigit()]
            move_boxes(stacks, *directions)

        print(f'Anwser to day five: `', end='')
        for column in stacks:
            for v in column:
                continue
            print(v, end='')
        print('`')

def part_two():
    with open('input\\input5.txt', 'r') as file:
        initial = []
        for i in range(8):
            line = file.readline()#.replace(' ', '.')
            n= 4
            chunk = [line[i:i+n].replace('[',' ').replace(']',' ').strip() for i in range(0, len(line), n)]  # separate into chunks of 4 charecters wide, remove [] and spaces
            initial.append(chunk)  # so we would get a row with only box labels

        
        stacks = swap(initial)
        
        _ = file.readline() # pass indexes
        _ = file.readline() # pass newline


        for line in file:
            directions = [int(w) for w in line.strip().split(' ') if w.isdigit()]
            move_boxes2(stacks, *directions)

        print(f'Anwser to day five p2: `', end='')
        for column in stacks:
            for v in column:
                continue
            print(v, end='')
        print('`')


if __name__ == '__main__':
    part_one()
    part_two()