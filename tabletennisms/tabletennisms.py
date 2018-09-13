from leaderboard import Leaderboard
from player import Player
from prettytable import PrettyTable
from leaderboardcontroller import LeaderboardController
from iocontroller import IOController
from inputrouter import InputRouter
import sys
import click

leaderboard_controller = LeaderboardController()
io_controller = IOController()
router = InputRouter()

def show_leaderboard():
    leader_table = PrettyTable()
    leader_table.field_names = ["Rank", "Player Name"]

    players = leaderboard_controller.get_leaderboard_players()

    if len(players) == 0:
        leader_table.add_row(["0", "Add Players"])

    for index, player in enumerate(players):
        leader_table.add_row([index + 1, player.name.capitalize()])
        
    print(leader_table)

## IO Commands
def save_leaderboard():
    leaderboard_controller.save_leaderboard()

def load_leaderboards():
    leaderboard_controller.load_leaderboards()

def save_active_leaderboard_name(leaderboard_name):
    io_controller.write_active_leaderboard(leaderboard_name)

def load_active_leaderboard():
    leaderboard_controller.load_active_leaderboard()

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

commands = ["-add", "-remove", "-clear", "-score", "-find", "-show", "-help", "-create", "-change", "-active", "-delete"]

def main():

    load_leaderboards()
    load_active_leaderboard()

    args = sanitise_input(sys.argv[1:])

    if len(args) > 0 and args[0] in commands: 
        command_processor(args)
    else:
        help(None)
        sys.exit(1)

    leaderboard_controller.create_html()    

def command_processor(args):
    if args[0] == "-add":
        response_message = router.add_players(args[1:])
        print(response_message) 
    elif args[0] == "-remove":
        response_message = router.remove_players(args[1:])
        print(response_message) 
    elif args[0] == "-clear":
        response_message = router.clear_leaderboard()
        print(response_message) 
    elif args[0] == "-score":
        response_message = router.submit_players_score(arg[1], args[2])
        show_leaderboard()
        print(response_message) 
    elif args[0] == "-find":
        response_message = router.find_player(args)
        print(response_message) 
    elif args[0] == "-create":
        response_message = router.create_leaderboard(args)
        print(response_message) 
    elif args[0] == "-change":
        response_message = router.change_active_leaderboard(args)
        print(response_message) 
    elif args[0] == "-delete":
        response_message = router.delete_leaderboard(args)
        print(response_message) 
    elif args[0] == "-show":
        show_leaderboard()
    elif args[0] == "-active":
        response_message = router.show_active_leaderboard()
        print(response_message) 
    elif args[0] == "-help":
        if len(args) == 2:
            help(args[1])
        else:
            help(None)

    save_leaderboard()

def sanitise_input(input_arr):
    san = []
    for item in input_arr:
        san.append(item.lower())
    return san

if __name__ == '__main__':
   main()