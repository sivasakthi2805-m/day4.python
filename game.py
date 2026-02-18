import random

def stone_paper_scissors(rounds=1, player_wins=0, computer_wins=0):
    if rounds > 3:
        print(f"\nGame Over! Player: {player_wins}, Computer: {computer_wins}")
        return
    
    print(f"\n--- Round {rounds} ---")
    player_choice = input("Enter stone, paper, or scissors: ").lower()
    
    if player_choice not in ["stone", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        return stone_paper_scissors(rounds, player_wins, computer_wins)
    
    computer_choice = random.choice(["stone", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
        result_player_wins = player_wins
        result_computer_wins = computer_wins
    elif (player_choice == "stone" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "stone") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        result_player_wins = player_wins + 1
        result_computer_wins = computer_wins
    else:
        print("Computer wins this round!")
        result_player_wins = player_wins
        result_computer_wins = computer_wins + 1
    
    stone_paper_scissors(rounds + 1, result_player_wins, result_computer_wins)

stone_paper_scissors()
 
   


