
test_input = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
'''.split('\n')


def part_one(data):
    
    cycle = 0
    X = 1
    n20_value = []

    for command in data:
        if command[0] == 'noop':
            cycle += 1
        elif command[0] == 'addx':
            if (21 + cycle) % 40 == 0:
            
                n20_value.append((cycle+1) * X)
            cycle += 2
            
        if (20 + cycle) % 40 == 0:
            n20_value.append(cycle * X)

        if command[0] == 'addx':
            X += int(command[1])
        
    
    print(f'Anwser to day nine: `{sum(n20_value)}`')

def update_crt(cycle, X, crt_row):
    ctr_pos = (cycle-1) % 40
    cur_pixel = '.'
    if X - 1 <= ctr_pos <= X + 1:
        cur_pixel = '#'
    return crt_row + cur_pixel

def part_two(data):
    
    width = 40
        
    log = open('test_log10.txt', 'w')
    cycle = 0
    X = 1
    crt_row = ''
    log.write(f'Sprite position: {"."*(X-1) + "###" + "."*(width-2 - X)}\n\n')
    for command in data:
        cycle += 1
        log.write(f'Start cycle   {cycle}: begin executing {command}\n')
        log.write(f'During cycle  {cycle}: CRT draws pixel in position {(cycle-1) % 40}\n')
        crt_row = update_crt(cycle, X, crt_row)
        log.write(f'Current CRT row: {crt_row}\n')

        if command[0] == 'noop':
            pass
        elif command[0] == 'addx':
            cycle += 1
            log.write(f'\nDuring cycle  {cycle}: CRT draws pixel in position {(cycle-1) % 40}\n')
            crt_row = update_crt(cycle, X, crt_row)
            log.write(f'Current CRT row: {crt_row}\n')
            X += int(command[1])
            log.write(f'End of cycle  {cycle}: finish executing {command} (Register X is now {X})\n')
            log.write(f'Sprite position: {"."*(X-1) + "###" + "."*(width-2 - X)}\n\n')
        
    log.close()
    n = 40
    print(f'Anwser to day nine p2:')
    str_ = '\n'.join(crt_row[i:i+n] for i in range(0, len(crt_row), n))
    print(str_) # split into chunks of 40 chrs and insert \n between
    

if __name__ == '__main__':
    #data = [line.strip().split(' ') for line in test_input]

    with open('input\\input10!!.txt', 'r', encoding='cp1252') as file:
        data = [line.strip().split(' ') for line in file.readlines()]

    part_one(data)
    part_two(data)