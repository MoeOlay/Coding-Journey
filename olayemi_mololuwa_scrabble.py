scrabble_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}
while True:
    word = input(":> ").upper()
    points = 0
    if word == 'QUIT' or word =='Q':
        break
    for i in word:
        for key, value in scrabble_points.items():
            if i == key:
                points += value
    print(f'{word} is worth {points} points.')