def score_word(word):
    score = 0
    for letter in word:
        if (letter != '"'):
            score += ord(letter) - ord('A') + 1
    return score

text_file = open("input/p022_names.txt", "r")
lines = sorted(text_file.read().split(','))
score = 0
position = 0
while (position < len(lines)):
    score += (position + 1) * score_word(lines[position])
    position += 1
print(score)
