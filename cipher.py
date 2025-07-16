cipher = {
    'a': '@',
    'b': '8',
    'c': 'c',
    'd': 'd',
    'e': '3',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': '!',
    'j': 'j',
    'k': 'k',
    'l': '1',
    'm': 'm',
    'n': 'N',
    'o': '0',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': '$',
    't': '7',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': '%',
    'y': 'y',
    'z': '2'
}

def encode(word):
    encoded = ""
    for letter in word:
        encoded += cipher[letter]
    return encoded

def game():
    print("Welcome to the game")

    words = ['hello', 'quick', 'smart', 'value', 'brave']
    score = 0
    word_number = 1

    for word in words:
        encoded = encode(word)
        print("Word", word_number, ":", encoded)
        attempts = 3
        while attempts > 0:
            guess = input("Guess the word: ")
            if guess == word:
                print("Correct!")
                score+= 1
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Incorrect, try again")
                else:
                    print("Incorrect, no more attempts. You lose")
        word_number += 1
    print("Game Over! Your score is ", score, "out of", len(words))

game()
