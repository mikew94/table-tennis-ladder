import os
from leaderboard import Leaderboard

class IOController:

    def write_active_leaderboard(self, option):
        with open("../option", "w") as f:
            f.write(option)

    def read_active_leaderboard(self):
        with open("../option", "r") as f:
            return f.read()

    def write_leaderboard(self, leaderboard):
        with open("../leaderboards/" + leaderboard.name + ".sml", "w") as f:
            for player in leaderboard.get_players():
                f.write(str(player.name) + "\n")

    def load_leaderboards(self):
        leaderboards = []
        for filename in os.listdir("../leaderboards"):
            players = []
            if filename.endswith(".sml"):
                with open("../leaderboards/"+ filename) as f:
                    for line in f:
                        players.append(line.strip())
                leaderboards.append(Leaderboard(filename[:-4], players))
        return leaderboards