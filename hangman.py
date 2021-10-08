# HANGMAN

import random

word_hints = {
    'elephant': 'Land big animal',
    'rohit': 'the name of the developer who develop this game',
    'washington': 'the city of USA',
    'tiger': 'carnivorous wild animal'
}

word = random.choice(list(word_hints.keys()))  # -> choosing the random words.
hint = word_hints.get(word)
li = ['*'for i in word]  # to print * instead of letters of word
count = 6
string = ""  # initial declaration
w = []  # -> to store the characters that are already guessed

print("This game is called hangman. You need to guess word correctly. "
      "If you type multiple character. Only the first one will be selected. And you have 6 chances.")
print()
print("Hint: {}".format(hint))
print()

while True:
    c = string  # -> to store the string of previous loop
    character = input("Enter your guess:").lower()[0]
    for i in range(len(word)):
        if character == word[i].lower():
            li[i] = word[i]  # -> store the letter instead of *
            break

    print("Guessed word: {}".format(character))
    string = "".join(li)  # - > convert list into string
    print(string)

    if word == string:
        print("You guess the word correctly.")
        break

    if character not in w:  # -> same character typed.
        w.append(character)  # -> to store the characters that are already guessed
        if c == string:
            count -= 1
    else:
        print("character already guessed.")

    print(f"Chances remain: {count}")
    print()
    if count == 0:
        print("You are hung.")
        break
