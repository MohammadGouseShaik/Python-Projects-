import random

def play():
    user = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if user == computer:
        return 'It\'s a tie!'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
