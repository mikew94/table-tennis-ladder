from leaderboard import Leaderboard
from player import Player
from prettytable import PrettyTable
import sys

leaderboard = Leaderboard()

### COMMANDS ###
def add_player(player_name):
   leaderboard.add_player(player_name)

def enter_score(winner_name, loser_name):
    leaderboard.update_leaderboard(winner_name, loser_name)

def show_leaderboard():
    leader_table = PrettyTable()
    leader_table.field_names = ["Rank", "Player Name"]

    for index, player in enumerate(get_leaderboard_players()):
        leader_table.add_row([index + 1, player.get_name().capitalize()])
        
    print(leader_table)

def get_leaderboard_players():
    return leaderboard.get_players()

commands = ["-add", "-score", "-show", "-help"]

def main():

    global leaderboard

    load_leaderboard()

    args = sanitise_input(sys.argv[1:])

    if len(args) > 0 and args[0] in commands: 
        command_processor(args)
    else:
        help(None)
        sys.exit(1)

def command_processor(args):
    if args[0] == "-add":
        if len(args) == 2:
            add_player(args[1])
            print("> Added: " + args[1])
        else:
            help(args[0])
    elif args[0] == "-score":
        if len(args) == 3:
            enter_score(args[1], args[2])
            print("> Score: %s beat %s" % (args[1], args[2]))
        else:
            help(args[0])
    elif args[0] == "-show":
        show_leaderboard()
    elif args[0] == "-help":
        help(None)

    write_leaderboard()

def help(command):
    if command == "-score":
        print("score: incorrect usage")
        print("usage: -score [winner name] [loser name]")
    elif command is None:      
        print("These are the available options:" + str(commands))
    elif command == "-add":
        print("add: incorrect usage")
        print("usage: -add [player name]")
        
def sanitise_input(input_arr):
    san = []
    for item in input_arr:
        san.append(item.lower())
    return san

def load_leaderboard():
    leaderboard.set_players(read_leaderboard())

def write_leaderboard():
    with open("leaderboard.csv", "w") as f:
        for player in leaderboard.get_players():
            f.write(str(player.name) + "\n")

def read_leaderboard():
    names = []
    with open("leaderboard.csv") as f:
        for line in f:
            names.append(line.strip())
    return names

if __name__ == '__main__':
   main()