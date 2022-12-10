import numpy as np

test_input ='''30373
25512
65332
33549
35390'''.split('\n')
 

def generate_mask(data):
    # idea is pretty simple. For each side generate mask so that if value 
    data = np.array(data)
    
    left_mask = np.zeros(data.shape, dtype=int)
    for mask_row, row in zip(left_mask, data):
        for i, v in enumerate(row):
            if i == len(row) - 1:
                continue
            mask_row[i+1] = max(v, mask_row[i])
    #print(left_mask)

    right_mask = np.zeros(data.shape, dtype=int)
    for mask_row, row in zip(right_mask, data):
        for i, v in enumerate(reversed(row)):
            if i == len(row) - 1:
                continue
            idx = (len(row) - 1) - i - 1
            mask_row[idx] =  max(v,mask_row[idx + 1 ])
    #print(right_mask)

    top_mask = np.zeros(data.shape, dtype=int)
    for mask_row, row in zip(top_mask.T, data.T):
        for i, v in enumerate(row):
            if i == len(row) - 1:
                continue        
            mask_row[i+1] =  max(v,mask_row[i])
    #print(top_mask)

    bot_mask = np.zeros(data.shape, dtype=int)
    for mask_row, row in zip(bot_mask.T, data.T):
        for i, v in enumerate(reversed(row)):
            if i == len(row) - 1:
                continue
            idx = (len(row) - 1) - i - 1
            mask_row[idx] =  max(v,mask_row[idx + 1 ])
    #print(bot_mask)

    mask = np.zeros(data.shape, dtype=int)
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            mask[i,j] = min(bot_mask[i,j], left_mask[i,j], top_mask[i,j], right_mask[i,j])

    
    return mask


def part_one():
    data = []
    #for line in test_input:
    #    data.append([int(c) for c in list(line)])

    with open('input\\input8.txt', 'r') as file:
        for line in file:
            data.append([int(c) for c in list(line.strip())])
    

    data = np.array(data)
    mask = generate_mask(data)
    outer_edge = np.pad(np.ones((data.shape[0]-2, data.shape[1]-2), dtype=int), 1) == 1  # outer edge is always visible, so this simple boolean mask forces this (if tree on the edge is height 0 then it would be count as invisible without it)
    visible = ((np.minimum(mask, data) == data) & outer_edge )  == False  # check what is taller - mask or actual data. If height doesnt changed (from actual data) then tree is invisible
    print(f'Anwser to day eigth: `{np.sum(visible)}`')  
    

def distance_to_n(i_, j_, data):
    # slow function
    distances = [0,0,0,0] # left top right bottom
    target_tree = data[i_, j_]
    #print(f'{target_tree=}')
    coun = 0
    for coun, j in enumerate(reversed(range(j_))):  # left
        if target_tree <= data[i_,j]:
            break
    distances[0] = coun + 1

    for coun, i in enumerate(reversed(range(i_))):  # top
        if target_tree <= data[i,j_]:
            break
    distances[1] = coun + 1

    for coun, j in enumerate((range(j_+1,len(data)))):  # right
        if target_tree <= data[i_,j]:
            break
    distances[2] = coun + 1

    for coun, i in enumerate((range(i_+1,len(data[0])))):  # bottom
        if target_tree <= data[i,j_]:
            break
    distances[3] = coun + 1
    a,b,c,d = distances
    return a*b*c*d

def part_two():
    data = []
    #for line in test_input:
    #    data.append([int(c) for c in list(line)])

    with open('input\\input8.txt', 'r') as file:
        for line in file:
            data.append([int(c) for c in list(line.strip())])
    

    data = np.array(data)
    mask = generate_mask(data)
    outer_edge = np.pad(np.ones((data.shape[0]-2, data.shape[1]-2), dtype=int), 1) == 1  # outer edge is always visible, so this simple boolean mask forces this (if tree on the edge is height 0 then it would be count as invisible without it)
    visible = ((np.minimum(mask, data) == data) & outer_edge ) == False  # check what is taller - mask or actual data. If height doesnt changed (from actual data) then tree is invisible
    #print(data, '\n')


    

    scenic_score = np.zeros(data.shape, dtype=int)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
                scenic_score[i,j] =  distance_to_n(i,j, data)

    #print(visible)
    print(f'Anwser to day eigth p2: `{np.max(scenic_score * visible)}`' )

    
    
    
    
    
    #print(f'Anwser to day eigth p2: `{np.sum(invisible == False)}`')  # inverse
    



if __name__ == '__main__':
    part_one()
    part_two()