import json

INPUT_PATH = 'input\\input13.txt'

test_input = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''.split('\n')




def compare(ar1, ar2):
    #print(f'Compare {ar1} vs {ar2}')
    if type(ar1) != type(ar2):  # mixed
        if type(ar1) == int:
            ar1 = [ar1]
        elif type(ar2) == int:
            ar2 = [ar2]
    
    if type(ar1) == type(ar2) == int:
        if ar1 < ar2:
            return True
        elif ar1 > ar2:
            return False
    else:  # lists
        decision = None          # python takes smalest input length for zip. So im checking length of the lists beforehand.
        if len(ar1) < len(ar2):
            decision =  True
        elif len(ar1) > len(ar2):
            decision = False

        for v1, v2 in zip(ar1, ar2):  
            com = compare(v1,v2)
            if com is None:
                continue
            else: 
                return com
        return decision

def part_one(data: list[str]):
    ans = 0
    for i,(ar1, ar2) in enumerate(zip(data[:-1:2],data[1::2])):  # iterate in pairs of two
        if compare(ar1, ar2):
            ans += i+1

    print(f'Anwser to day thirteen: `{ans}`') 


    

def part_two(data: list[str]):

    data.append([[2]])
    data.append([[6]])


    ans = 1
    for i, d1 in enumerate(data):
        count_true = 0
        for d2 in data:
            if compare(d2,d1):  # this compare operation is something like > so if you would compare 1,2,3,4 to 1 you would get 3, for 2 - 2, 3 - 1, 4 - 0 and the resulting number would be an index in sorted array.
                count_true += 1
        if i in [len(data)-2, len(data)-1 ]:  # i'n appending test packets to the and on the list, so they position would be len -1/-2
            ans *= count_true+1  # dont forget about off be one

    print(f'Anwser to day thirteen p2: `{ans}`') 



if __name__ == '__main__':
    data = [json.loads(line.strip()) for line in test_input  if line != '']  # thanks to web developers for buildin library for parsing string input to arrays

    with open(INPUT_PATH, 'r') as file:
        data = [json.loads(line.strip()) for line in file.readlines() if line.strip() != '']
    
    
    part_one(data)
    part_two(data)
        