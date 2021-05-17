from random import choice

word = choice(["code", "computer", "coder", "programming", "python", "java", "c language", "languages", "science", "tech", "technology", "developer", "website", "web", "tonight", "love", "realtionship", "go", "cry", "forever", "cool", "party"])

guessed = []
wrong = []

tries = 7

while tries > 0:

    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess the word:", out)
    print(tries, "chances left")

    guess = input()

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("Congrats!! You guessed right word: ", word)
else:
    print("Sorry but the correct word is: ", word)
