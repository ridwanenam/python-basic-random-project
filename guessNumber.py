import random

def main():
    print("Uji Keberuntungan")
    print("Permainan Tebak Angka!")
    print("Tebak Angka 1-100")

    secret_number = random.randint(1, 100)
    guesses_taken = 0

    while True:
        guess = int(input("Tebak angka: "))

        guesses_taken += 1

        if guess < secret_number:
            print("Angka terlalu kecil!")
        elif guess > secret_number:
            print("Angka terlalu besar!")
        else:
            print(f"Congrats! angka {secret_number} berhasil ditebak dalam {guesses_taken}x")
            break

if __name__ == "__main__":
    main()
