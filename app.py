import random
import nltk

print("Downloading the words corpus from nltk...")
nltk.download('words', quiet=True)
print("Done!")


def get_random_word():
    word_list = [word for word in nltk.corpus.words.words() if len(word) == 5]
    random_word = random.choice(word_list)

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
    get_random_word()
    play_again = input("Do you want to play again? (yes/no)\n -> ")
    if play_again.lower() != 'yes':
        print("Goodbye!")
        break
