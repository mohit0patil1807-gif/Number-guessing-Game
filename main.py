import random
import art

def compare(g, r):
    if g > r:
        return "too high"
    elif g < r:
        return "too low"
    else:
        return 0


def game():
    rnum = random.randint(1, 100)
    print(art.logo)

    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if choice == "easy":
        turns = 10
    else:
        turns = 5

    while turns > 0:
        print(f"You have {turns} turns left")

        gnum = int(input("Make a guess: "))

        if compare(gnum, rnum) == 0:
            print(f"You got it! The answer was {gnum}")
            break

        print(compare(gnum, rnum))
        turns -= 1

        if turns == 0:
            print(f"You've run out of turns. The answer was {rnum}.")


game()