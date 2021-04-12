import random



words = []
text_file = open("words.txt")
with open("words.txt") as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(' ')]
        words.append(inner_list)

words_length = len(words)
random_word_index = random.randint(0,words_length)
word_to_string = words[random_word_index]
sentence_of_madness = ""

for i in range(50):

    word = str((words[random_word_index]))
    word = word.replace("[", ' ')
    word = word.replace(']', ' ')
    word = word.replace("'", '')

    sentence_of_madness += word
    random_word_index = random.randint(0,words_length)
    if i == 49:
        print(sentence_of_madness)
