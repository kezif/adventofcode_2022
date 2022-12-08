

def visualisation(lower, upper, max=100):
    # from 2, 5
    # return string .2345...--to max--...
    vis = ''
    for _ in range(1, lower):
        vis += '.'
    for digit in range(lower, upper+1):
        vis += '!'
    for _ in range(upper, max):
        vis += '.'
    return vis


def part_one():
    overlapin = 0
    log = open('test_log4.txt', 'w')
    with open('input\\input4.txt', 'r') as file:
        for line in file:
        
            
            first_elf, second_elf = line.strip().split(',')
            first_t1, first_t2 =  [int(v) for v in first_elf.split('-')]
            second_t1, second_t2 = [int(v) for v in  second_elf.split('-')]
            
            log.write('\n')
            log.write('\n'+ line.strip())
            log.write('\n' + visualisation(first_t1, first_t2))
            log.write('\n' + visualisation(second_t1, second_t2))
            log.write('\n')


            if first_t2 - first_t1 >= second_t2 - second_t1:
                smaller_t1, smaller_t2 = second_t1, second_t2
                bigger_t1, bigger_t2 = first_t1, first_t2
            else:
                smaller_t1, smaller_t2 = first_t1, first_t2
                bigger_t1, bigger_t2 = second_t1, second_t2

            if (bigger_t1 <= smaller_t1 <= bigger_t2) and (bigger_t1<= smaller_t2 <= bigger_t2):
                overlapin += 1
                log.write('!overlap')


            '''if (second_t1 <= first_t1 <= second_t2) and (second_t1<= first_t2 <= second_t2):
                overlapin += 1
                log.write('!overlap')
            
            # this if statement is mirrored from above but for second elf time window. Probably it would make sense to make one if statement and compare if smaller window is overlapped
            elif (first_t1 <= second_t1 <= first_t2) and (first_t1 <= second_t2 <= first_t2):
                overlapin += 1
                log.write('!overlap')
            '''
    print(f'Anwser to day four: `{overlapin}` pairs ')
    log.close()        


def part_two():
    overlapin = 0
    log = open('test_log4.txt', 'w')
    with open('input\\input4.txt', 'r') as file:
        for line in file:
            first_elf, second_elf = line.strip().split(',')
            first_t1, first_t2 =  [int(v) for v in first_elf.split('-')]
            second_t1, second_t2 = [int(v) for v in  second_elf.split('-')]
            
            log.write('\n')
            log.write('\n'+ line.strip())
            log.write('\n' + visualisation(first_t1, first_t2))
            log.write('\n' + visualisation(second_t1, second_t2))
            log.write('\n')


            if first_t2 - first_t1 >= second_t2 - second_t1:
                smaller_t1, smaller_t2 = second_t1, second_t2
                bigger_t1, bigger_t2 = first_t1, first_t2
            else:
                smaller_t1, smaller_t2 = first_t1, first_t2
                bigger_t1, bigger_t2 = second_t1, second_t2


            partical_overlap = False
            bigger_range = range(bigger_t1, bigger_t2+1)
            for i in range(smaller_t1, smaller_t2+1):
                if i in bigger_range: # simular to double loop, but python have built in feature to check if value is in collection
                    partical_overlap = True

            if (bigger_t1 <= smaller_t1 <= bigger_t2) and (bigger_t1<= smaller_t2 <= bigger_t2):
                overlapin += 1
                log.write('!overlap')
            elif partical_overlap:
                overlapin += 1
                log.write('!partical overlap')
    print(f'Anwser to day four p2: `{overlapin}` pairs ')
    log.close()  


if __name__ == '__main__':
    #part_one()
    part_two()
        




'''for line in """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split('\n'):'''