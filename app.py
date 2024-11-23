import random
from collections import Counter


import nltk

print("Fetching the words corpus from nltk...")
nltk.download('words', quiet=True)
nltk.download('brown', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
brown_words = nltk.corpus.brown.words()
word_freq = Counter(brown_words)
all_words = nltk.corpus.words.words()
common_words = [word for word, _ in word_freq.most_common() if word in all_words]

# Filtering the words to only include nouns
tagged_words = nltk.pos_tag(common_words)
nouns = [word for word, pos in tagged_words if pos.startswith == 'NN']

common_nouns = [word for word, _ in word_freq.most_common() if word in nouns]
print("Done!")


def word_game():
    print("Choose a difficulty level: "
          "\n1. Easy (100 most common nouns)"
          "\n2. Medium (10000 most common nouns)"
          "\n3. Hard (Almsot every noun in the English language)")
    difficulty = input("Enter the number of the difficulty level: ")
    if difficulty == '1':
        word_selection = common_nouns[:100]
    elif difficulty == '2':
        word_selection = common_nouns[:10000]
    else:
        word_selection = common_nouns

    random_word = random.choice(word_selection)

    word_length = str(len(random_word))

    print("Welcome to the app!")
    print("The length of the word is " + word_length)

    guesscount = 1
    while guesscount < 5:
        while True:
            guess = input(f"Take your {guesscount} guess!\n -> ")
            if len(guess) != 5:
                print("Please enter a 5-letter word.")
            else:
                break
        if guess == random_word:
            print("You guessed it right!")
            win = True
            guesscount = 5
            break
        else:
            feedback = []
            for i in range(len(guess)):
                if i < len(random_word) and guess[i] == random_word[i]:
                    feedback.append(guess[i])
                elif guess[i] in random_word:
                    feedback.append(f"({guess[i]})")
                else:
                    feedback.append('_')
            print("Not quite right. Here are the correct characters so far: " + ''.join(feedback))
            guesscount += 1
            print("Number of guesses:", guesscount)
            if guesscount == 5:
                print("You lost! The word was:", random_word)
                win = False


while True:
    word_game()
    play_again = input("Do you want to play again? (yes/no)\n -> ")
    if play_again.lower() != 'yes':
        print("Goodbye!")
        break
