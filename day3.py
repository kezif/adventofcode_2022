

def part_one():
    score = 0
    with open('input\\input3.txt', 'r') as file:
        for line in file:
            line = line.strip()
            compart_1, compart_2 = line[:len(line)//2], line[len(line)//2:]
            same_chars = list(set(compart_1) & set(compart_2))

            sub_score = [ord(ch) - 96 if ord(ch) > 96 else ord(ch) - 38  for ch in same_chars]
            score += sum(sub_score)
        
    print(f'Anwser to day three: `{score}` points ')    


def part_two():
    score = 0
    with open('input\\input3.txt', 'r') as file:
        file = file.readlines()
        for lines in zip(file[0::3],file[1::3],file[2::3]):  # iterate in chunk of 3 lines
            s1, s2, s3 = [set(s.strip()) for s in lines]  # because of \n i got negative score((
            same_chars =  s1 & s2 & s3
      
            sub_score = [ord(ch) - 96 if ord(ch) > 96 else ord(ch) - 38  for ch in same_chars]
            score += sum(sub_score)
    print(f'Anwser to day three p2: `{score}` points ')

def test():

    input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


    score = 0
    inp = input.split('\n')
    for lines in zip(inp[0::3],inp[1::3],inp[2::3]):
        s1, s2, s3 = [set(s) for s in lines]
        same_chars =  s1 & s2 & s3
      
        sub_score = [ord(ch) - 96 if ord(ch) > 96 else ord(ch) - 38  for ch in same_chars]
        score += sum(sub_score)
        print(same_chars, sub_score)
        
    print(f'Anwser to day three: `{score}` points ')


if __name__ == '__main__':
    #test()
    part_one()
    part_two()