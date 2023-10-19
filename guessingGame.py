    print ()

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinking 
                of a number from 1 to {limit}\n.")
    count = 1
    guess = int(input("your guess:  "))
    
    while(guess != number):
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        guess = int(input("Your guess?:  "))
    print(f"You guessed it in {count} tries.\n") 
    
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enter the limit:  "))
        play_game(limit)
        again = input("Play again? Enter yes/no?")
        print()
    print("Later!")
    
if __name__ == "__main__":
    main()