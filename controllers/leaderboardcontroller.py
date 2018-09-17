from models.leaderboard import Leaderboard
from models.player import Player
from controllers.iocontroller import IOController

class LeaderboardController:

    io_controller = IOController()
    leaderboards = []
    active_leaderboard_name = ""

    ###
    def add_players(self, players):
        players_not_added = []
        leaderboard = self.get_active_leaderboard()
        for player_name in players:
            if not leaderboard.get_player_from_list(player_name):
                leaderboard.add_player(player_name)
            else:
                players_not_added.append(player_name)
        return players_not_added

    ###
    def remove_players(self, players):
        players_not_removed = []
        leaderboard = self.get_active_leaderboard()
        for player_name in players:
            player = leaderboard.get_player_from_list(player_name)
            if player:
                leaderboard.remove_player(player)
            else:
                players_not_removed.append(player_name)
        return players_not_removed

    ###
    def submit_score(self, winner_name, loser_name):
        leaderboard = self.get_active_leaderboard()
        winner_player = leaderboard.get_player_from_list(winner_name)
        loser_player = leaderboard.get_player_from_list(loser_name)
        if winner_player is None:
            leaderboard.add_player(winner_name)
        if loser_player is None:
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
        self.set_active_leaderboard(leaderboards[len(leaderboards)-1].name)
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
        if not self.get_leaderboard_by_name(leaderboard_name):
            self.leaderboards.append(Leaderboard(leaderboard_name, []))
            self.active_leaderboard_name = leaderboard_name
            return True
        return False

    ###
    def change_active_leaderboard(self, leaderboard_name):
        if self.get_leaderboard_by_name(leaderboard_name):
            self.active_leaderboard_name = leaderboard_name
            return True
        return False

    ###
    def delete_leaderboard(self, leaderboard_name):
        leaderboard = self.get_leaderboard_by_name(leaderboard_name)
        if leaderboard:
            self.leaderboards.remove(leaderboard)
            self.delete_leaderboard_file(leaderboard.name)
            self.set_active_leaderboard(self.leaderboards[0].name)
            self.io_controller.write_active_leaderboard(self.leaderboards[0].name)
            return True
        return False
        
    def get_leaderboard_by_name(self, leaderboard_name):
        for leaderboard in self.leaderboards:
            if leaderboard_name == leaderboard.name:
                return leaderboard
        return None


    ## HTML TABLE CREATOR ##
    def create_html(self):
        leaderboard = self.get_active_leaderboard()
        html = "<html><body><div align=\"center\" style=\"margin-top:4rem\"><h3>" + leaderboard.name + "</h3>"
        html += "<table border=1><tr><th style=\"padding:0.5rem\">Rank</th><th style=\"padding:0.5rem\">Name</th></tr>"

        for index, player in enumerate(leaderboard.players):
            html += "<tr><td style=\"padding:0.5rem\">" + str(index+1) + "</td><td style=\"padding:0.5rem\">" + player.name + "</td></tr>"

        html += "</table></div></body></html>"

        self.io_controller.write_html_file(html, leaderboard.name)

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

    def delete_leaderboard_file(self, filename):
        self.io_controller.delete_file(filename)
