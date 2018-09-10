from leaderboard import Leaderboard
import sys

leaderboard = Leaderboard()

### COMMANDS ###
def add_player(player_name):
   leaderboard.add_player(player_name)

def enter_score(winner_name, loser_name):
    leaderboard.update_leaderboard(winner_name, loser_name)

def show_leaderboard():
    print(leaderboard.get_players())

def main():

   global leaderboard

   leaderboard.set_players(read_leaderboard())

   args = sanitise_input(sys.argv[1:])

   if args[0] == "-add":
       add_player(args[1])
       print("> Added: " + player_name)

   if args[0] == "-score":
       leaderboard = update_leaderboard(args[1], args[2])

   if args[0] == "-show":
       show_leaderboard()

def sanitise_input(input_arr):
    san = []
    for item in input_arr:
        san.append(item.lower())
    return san

def write_leaderboard(leaderboard):
    with open("leaderboard.csv") as f:
        for name in leaderboard.get_players():
            f.write(name + "\n")
    f.close()

def read_leaderboard():
    names = []
    with open("leaderboard.csv") as f:
        for line in f:
            names.append(line.strip())
    return names

if __name__ == '__main__':
   main()