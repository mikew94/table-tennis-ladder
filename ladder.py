
import sys

ladder = []

## Appends new player to the end of the ladder
def new_player(player_name):
    ladder.append(player_name)
    print("> Added: " + player_name)
    return

def update_ladder(winner_name, loser_name):

    if winner_name not in ladder and loser_name not in ladder:
        print("AAAAAA")
        new_player(winner_name)
        new_player(loser_name)
        return ladder
    else:
        if winner_name not in ladder:
            new_player(winner_name)
        if loser_name not in ladder:
            new_player(loser_name)

        return move_players(winner_name, loser_name)

def move_players(winner_name, loser_name):
    new_ladder = []
    loser_position = ladder.index(loser_name)
    winner_position = ladder.index(winner_name)

    if (winner_position < loser_position):
        return ladder

    if loser_position > 0:
        new_ladder = ladder[:loser_position]

    new_ladder.append(winner_name)
    new_ladder.append(loser_name)
    
    ladder.remove(winner_name)

    new_ladder.extend(ladder[loser_position+1:])

    print("> Score: %s beat %s" % (winner_name, loser_name))

    return new_ladder

def main():
    
    global ladder

    ladder.append("Mike")
    ladder.append("Sandeep")
    ladder.append("Adolf")
    ladder.append("Bob")

    print(ladder)

    args = sys.argv[1:]

    if args[0] == "add":
        new_player(args[1])

    if args[0] == "score":
        ladder = update_ladder(args[1], args[2])

    new_player("Dan")

    ladder = update_ladder("Dan", "Mike")

    print(ladder)

if __name__ == '__main__':
    main()