
with open('input\\input6.txt', 'r') as file:
    line = file.readline()


def position_of_n_unique_ch(line, n):
    for i in range(len(line)):
        chunk = line[i:i+n]
        #print(set(chunk))
        if len(set(chunk)) == n:
            return i+n
            

print(f'Anwser to day six: `{position_of_n_unique_ch(line, 4)}`')
print(f'Anwser to day six p2: `{position_of_n_unique_ch(line, 14)}`')
