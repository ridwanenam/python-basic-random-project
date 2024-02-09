import random

def main():
    print("Tebak kata (3 huruf)")
    print("max guesses = 3")

    # the words
    words = ["cat", "dog", "bat", "hat", "sun", "pen", "box", "leg", "hop", "top"]
    secret_word = random.choice(words)
    guesses_taken = 0
    max_guesses = 3

    while guesses_taken < max_guesses:
        guess = input("tebak kata: ").lower()

        guesses_taken += 1

        if guess == secret_word:
            print(f"good! berhasil menebak kata {secret_word}!")
            break
        else:
            print("coba lagi")

    if guesses_taken == max_guesses:
        print("susah kan. kata yang benar:", secret_word)

if __name__ == "__main__":
    main()
