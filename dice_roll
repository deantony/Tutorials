from random import randint

def roll():
    return randint(1, 6)
def play():
    player = roll()
    cpu = roll()
    if player > cpu:
        winner = "Player"
    if cpu > player:
        winner = "CPU"
    if player == cpu:
        winner = "nobody"
    print(f"Player: {player}\nCPU: {cpu}\n{winner} wins!")

play()
