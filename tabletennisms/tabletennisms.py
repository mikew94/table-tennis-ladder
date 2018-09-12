from leaderboard import Leaderboard
from player import Player
from prettytable import PrettyTable
from leaderboardcontroller import LeaderboardController
import os
import sys

leaderboard_controller = LeaderboardController()

### COMMANDS ###
def add_players(players):
    return leaderboard_controller.add_players(players)

def remove_players(players):
    return leaderboard_controller.remove_players(players)

def enter_score(winner_name, loser_name):
    leaderboard_controller.submit_score(winner_name, loser_name)

def show_leaderboard():
    leader_table = PrettyTable()
    leader_table.field_names = ["Rank", "Player Name"]

    players = leaderboard_controller.get_leaderboard_players()

    if len(players) == 0:
        leader_table.add_row(["0", "Add Players"])

    for index, player in enumerate(players):
        leader_table.add_row([index + 1, player.name.capitalize()])
        
    print(leader_table)

def find_player(player_name):
    return leaderboard_controller.find_player(player_name)

def get_leaderboard_players():
    return leaderboard_controller.get_leaderboard_players()

def clear_table():
    leaderboard_controller.clear_table()

def help(command):
    if command == "-score" or command == "score":
        print("usage: -score [winner name] [loser name]")
        print("This will post a score to the leaderboard")
    elif command == "-add" or command == "add":
        print("usage: -add [player name] ... takes up to five players")
        print("This adds one or more players to the leaderboard")
    elif command == "-remove" or command == "remove":
        print("usage: -remove [player name]")
        print("This removes a player from the leaderboard")
    elif command == "-find" or command == "find":
        print("usage: -find [player name]")
        print("This finds the player and returns their rank in the leaderboard")
    elif command == "-clear" or command == "clear":
        print("usage: -clear")
        print("This clears the leaderboard")
    else:      
        print("These are the available options:" + str(commands))
        print("usage: -help [command]")


commands = ["-add", "-remove", "-clear", "-score", "-find", "-show", "-help"]

###############

def main():

    load_leaderboards()

    args = sanitise_input(sys.argv[1:])

    if len(args) > 0 and args[0] in commands: 
        command_processor(args)
    else:
        help(None)
        sys.exit(1)

def command_processor(args):
    if args[0] == "-add":
        if len(args) >= 2 and len(args) < 7:
            success = add_players(args[1:])
            if success:
                if len(args) == 2:
                    print("> Player has been added: " + args[1])
                else:
                    print("> Players have been added: " + str(args[1:]))
            else:
                print("! One or more of the players already exists")
        else:
            help(args[0])
    elif args[0] == "-remove":
        if len(args) >= 2 and len(args) < 7:
            success = remove_players(args[1:])
            if success:
                if len(args) == 2:
                    print("> Player has been removed: " + args[1])
                else:
                    print("> Players have been removed: " + str(args[1:]))
            else: 
                print("! One or more of the players do not exist so couldn't be removed")
    elif args[0] == "-clear":
        clear_table()
        print("> Table cleared")
    elif args[0] == "-score":
        if len(args) == 3 and args[1] != args[2]:
            enter_score(args[1], args[2])
            show_leaderboard()
            print("> Score: %s beat %s" % (args[1], args[2]))
        else:
            help(args[0])
    elif args[0] == "-find":
        if len(args) == 2:
            player_index = find_player(args[1])
            if player_index:
                print("> %s is at rank #%s" % (args[1].capitalize(), player_index))
            else:
                print("! Player %s could not be found in the leaderboard" % (args[1]))
        else:
            help(args[0])
    elif args[0] == "-show":
        show_leaderboard()
    elif args[0] == "-help":
        if len(args) == 2:
            help(args[1])
        else:
            help(None)

    write_leaderboard(leaderboard_controller.get_active_leaderboard())

def sanitise_input(input_arr):
    san = []
    for item in input_arr:
        san.append(item.lower())
    return san

def write_leaderboard(leaderboard):
    with open("../leaderboards/" + leaderboard.name + ".sml", "w") as f:
        for player in leaderboard.get_players():
            f.write(str(player.name) + "\n")

def load_leaderboards():
    for filename in os.listdir("../leaderboards"):
        players = []
        if filename.endswith(".sml"):
            with open("../leaderboards/"+ filename) as f:
                for line in f:
                    players.append(line.strip())
            leaderboard_controller.initialise_leaderboard(players, filename[:-4])

if __name__ == '__main__':
   main()