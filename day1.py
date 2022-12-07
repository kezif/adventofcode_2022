


backpack = {}

elf_id = 1
with open('input\\input1.txt', 'r') as file:
    chunk_total = 0
    for line in file:
        if line == '\n':
            backpack[elf_id] = chunk_total
            elf_id += 1
            chunk_total = 0
        else:
            chunk_total += int(line)

#sorted(backpack.items, key=lambda kv: kv.value)
sorted_backpack = sorted(backpack.items(), key=lambda kv: kv[1], reverse=True)

print(f'Anwser to day one: `{sorted_backpack[0][1]}` calories ')


top_three = sum([v for k,v in sorted_backpack[:3]]) #get the values for first three elements and then sum it
print(f'Anwser to day one p2: `{top_three}` calories ')