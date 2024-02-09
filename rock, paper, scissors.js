import random

def main():
    print("pilih pilihannya (batu, gunting, atau kertas):")
    choices = ["batu", "gunting", "kertas"]

    while True:
        user_choice = input("pilihan user: ").lower()

        if user_choice == "keluar":
            print("ty!")
            break
        elif user_choice not in choices:
            print("pilihan tidak ada.")
            continue

        computer_choice = random.choice(choices)

        print(f"komputer milih: {computer_choice}")

        if user_choice == computer_choice:
            print("hasil: seri")
        elif (user_choice == "batu" and computer_choice == "gunting") or \
             (user_choice == "gunting" and computer_choice == "kertas") or \
             (user_choice == "kertas" and computer_choice == "batu"):
            print("hasil: user menang!")
        else:
            print("hasil: user kalah!")

        print("game selesai!\n")
        print("ketik 'keluar' untuk keluar game")

if __name__ == "__main__":
    main()
