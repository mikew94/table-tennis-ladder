from leaderboard import Leaderboard
from player import Player
from iocontroller import IOController

class LeaderboardController:

    io_controller = IOController()
    leaderboards = []
    active_leaderboard_name = ""

    ###
    def add_players(self, players):
        success = True
        leaderboard = self.get_active_leaderboard()
        for player_name in players:
            if not leaderboard.get_player_from_list(player_name):
                leaderboard.add_player(player_name)
            else:
                success = False
        return success

    ###
    def remove_players(self, players):
        success = True
        leaderboard = self.get_active_leaderboard()
        for player_name in players:
            player = leaderboard.get_player_from_list(player_name)
            if player:
                leaderboard.remove_player(player)
            else:
                success = False
        return success

    ###
    def submit_score(self, winner_name, loser_name):
        leaderboard = self.get_active_leaderboard()
        if leaderboard.get_player_from_list(winner_name) is None and leaderboard.get_player_from_list(loser_name) is None:
            leaderboard.add_player(winner_name)
            leaderboard.add_player(loser_name)
        else:
            if leaderboard.get_player_from_list(winner_name) is None:
                leaderboard.add_player(winner_name)
            if leaderboard.get_player_from_list(loser_name) is None:
                leaderboard.add_player(loser_name)
        self.update_player_position(leaderboard, winner_name, loser_name)

    def update_player_position(self, leaderboard, winner_name, loser_name):
        loser_index = leaderboard.players.index(leaderboard.get_player_from_list(loser_name))
        winner_index = leaderboard.players.index(leaderboard.get_player_from_list(winner_name))

        if (winner_index < loser_index):
            return

        winner_player = leaderboard.get_player_from_list(winner_name)

        leaderboard.remove_player(winner_player)
        leaderboard.insert_player_at_index(winner_player, loser_index)

    ###
    def find_player(self, player_name):
        return self.leaderboards.get_player_from_list(player_name)

    ###
    def get_leaderboard_players(self):
        return self.get_active_leaderboard().get_players()

    ###
    def initialise_leaderboards(self, leaderboards):
        self.active_leaderboard_name = leaderboards[len(leaderboards)-1].name
        self.leaderboards = leaderboards

    ###
    def get_active_leaderboard_name(self):
        return self.active_leaderboard_name

    ###
    def get_active_leaderboard(self):
        return self.get_leaderboard_by_name(self.active_leaderboard_name)

    ###
    def set_active_leaderboard(self, leaderboard_name):
        self.active_leaderboard_name = leaderboard_name
    
    ###
    def clear_leaderboard(self):
        return self.get_leaderboard_by_name(self.active_leaderboard_name).clear_players()

    ###
    def create_leaderboard(self, leaderboard_name):
        success = True
        if not self.get_leaderboard_by_name(leaderboard_name):
            self.leaderboards.append(Leaderboard(leaderboard_name, []))
            self.active_leaderboard_name = leaderboard_name
        else:
            success = False
        return success

    ###
    def change_active_leaderboard(self, leaderboard_name):
        success = True
        if not self.get_leaderboard_by_name(leaderboard_name):
            self.active_leaderboard_name = leaderboard_name
        else:
            success = False
        return success
        
    def get_leaderboard_by_name(self, leaderboard_name):
        for leaderboard in self.leaderboards:
            if leaderboard_name == leaderboard.name:
                return leaderboard
        return None

    ## IO ##

    ###
    def save_leaderboard(self):
        self.io_controller.write_leaderboard(self.get_active_leaderboard())

    ###
    def load_leaderboards(self):
        self.initialise_leaderboards(self.io_controller.load_leaderboards())

    ###
    def load_active_leaderboard(self):
        self.set_active_leaderboard(self.io_controller.read_active_leaderboard())
