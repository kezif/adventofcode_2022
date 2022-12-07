# A for Rock
# B for Paper
# C for Scissors
# 
# X for Rock
# Y for Paper
# Z for Scissors

# Score: the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)



shape_scoring = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
win_outcome = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}
lose_outcome = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
} 
draw_outcome = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}   

def part_one():
    score = 0
    with open('input\\input2.txt', 'r') as file:
        for line in file:
            opponent, you = line.split()
            score += shape_scoring[you]  # score for choicing shape

        
            if draw_outcome[opponent] == you:  # score for outcome
                score += 3
            elif win_outcome[opponent] == you:
                score += 6
            elif lose_outcome[opponent] == you:
                score += 0
                
    print(f'Anwser to day two: `{score}` points ')
    return score

def part_two():
    # X means you need to lose
    # Y means you need to end the round in a draw
    # Z means you need to win

    score = 0
    with open('input\\input2.txt', 'r') as file:
        for line in file:
            opponent, you = line.split()

            if you == 'X':
                you = lose_outcome[opponent]
            elif you == 'Y':
                you = draw_outcome[opponent]
            elif you == 'Z':
                you = win_outcome[opponent]
                

            score += shape_scoring[you]  # score for choicing shape

            #print(opponent, you)
            if draw_outcome[opponent] == you:  # score for outcome
                score += 3
            elif win_outcome[opponent] == you:
                score += 6
            elif lose_outcome[opponent] == you:
                score += 0
                
    print(f'Anwser to day two p2: `{score}` points ')
    return score

if __name__ == '__main__':
    part_one()
    part_two()

