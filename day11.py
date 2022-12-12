test_input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''.split('\n')


class Monkey():
    def __init__(self, id, items, operation_str, test, test_true_n, test_false_n, bored_action) -> None:
        self.id = id
        self.items = items
        self.bored_action = bored_action
        self.operation_str = operation_str #parser.expr(operation).compile()  # sneaky exploit str
        self.test = lambda x: x % test == 0
        self.test_true_n = test_true_n
        self.test_false_n = test_false_n
        self.inspected_n = 0


    def __str__(self) -> str:
        return f'{self.id=}\n {self.items=}\n {self.bored_action(1)=}\n {self.operation_str=}\n {self.test(1)=}\n { self.test_true_n=}\n {self.test_false_n=}'

    def __repr__(self) -> str:
        return f'Monkey: {self.id} items: {self.items}'

    def operation(self, number):
        _, operand, number2 = self.operation_str

        def base(n1, n2):
            if operand == '*':
                return n1 * n2
            elif operand == '+':
                return n1 + n2
            else:
                raise ValueError(f'Operator `{operand}` is not defined')
        

        if number2 == 'old':
            return base(number, number)
        else:
            return base(number, int(number2))
        
    @staticmethod    
    def compress_number(number):
        n = 3 * 11 * 19 * 5 * 2 * 7 * 17 * 13  # hardcoded values from mokeys divisibles
        # to be hones i forget about modulo arigphiticts and tried to divide by number. To make it small. That didng worked
        return number % n


    def simulate(self, monkeys_list: list, worries=True):
        while len(self.items) != 0:
            self.inspected_n += 1
            item = self.items.pop(0)
            item = self.operation(item)
            
            if worries:
                item = self.bored_action(item)
            else:
                item = Monkey.compress_number(item)
            if self.test(item):
                monkeys_list[self.test_true_n].items.append(item)
            else:
                monkeys_list[self.test_false_n].items.append(item)
            

def parse_operation(operation_str):
    _, operation, number = operation_str.split(' ')
    
    def base(n1, n2):
        if operation == '*':
            return n1 * n2
        elif operation == '+':
            return n1 + n2
        else:
            raise ValueError(f'Operator `{operation}` is not defined')
        
    if number == 'old':
        return lambda x: base(x, x)
    else:
        return lambda x: base(x, int(number))

def parse_monkeys(data) -> list[Monkey]:
    monkey_data = []
    monkey_list = []
    bored_action = lambda x: x // 3
    for line in data:
        
        if line[0].startswith('Monkey'):
            monkey_data.append(int(line[1][:-1]))  # remove last `:` and parse as int
        if line[0].startswith('Starting'):
            items_str = [int(v) for v in ''.join(line[2:]).split(',')]
            monkey_data.append(items_str)
        if line[0].startswith('Operation'):
            operation_str = line[3:] #' '.join(line[3:])
            monkey_data.append(operation_str)
        if line[0].startswith('Test'):  # all test are if number is divisible by n. So we need only number
            divisible_n = int(line[-1])
            monkey_data.append(divisible_n)
        if line[0].startswith('If'):
            if line[1].startswith('true'):
                test_true_n = int(line[-1])
                monkey_data.append(test_true_n)
            if line[1].startswith('false'):
                test_false_n = int(line[-1])
                monkey_data.append(test_false_n)

                monkey_data.append(bored_action)
                monkey_list.append(Monkey(*monkey_data))
                monkey_data = []

    return monkey_list

def part_one(data: list):
    monkey_list = parse_monkeys(data)

    for _ in range(20):
        for m in monkey_list:
            m.simulate(monkey_list)
        print(_, end='\r')

    
    a = sorted(m.inspected_n for m in monkey_list)[-2:]
    
    print(f'Anwser to day eleven: `{a[0] * a[1]}`')  # 182293
    #assert a[0] * a[1] == 182293, 'incorrect solution'

    

def part_two(data):
    monkey_list = parse_monkeys(data)
   
    for _ in range(10_000 ):
        for m in monkey_list:
            m.simulate(monkey_list, worries=False)
        print(_, end='\r')
    a = sorted(m.inspected_n for m in monkey_list)[-2:]   

    print(f'Anwser to day eleven p2: `{a[0] * a[1]}`')

if __name__ == '__main__':
    from math import sqrt
    data = [line.strip().split(' ') for line in test_input]

    with open('input\\input11.txt', 'r') as file:
        data = [line.strip().split(' ') for line in file.readlines()]

    
    
    part_one(data)
    part_two(data)
        