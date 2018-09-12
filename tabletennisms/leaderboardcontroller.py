from leaderboard import Leaderboard
from player import Player

class LeaderboardController:
    leaderboard = None
    active_leaderboard_name = ""

    def add_players(self, players):
        success = True
        for player_name in players:
            if not self.leaderboard.get_player_from_list(player_name):
                self.leaderboard.add_player(player_name)
            else:
                success = False
        return success

    def remove_players(self, players):
        success = True
        for player_name in players:
            player = self.leaderboard.get_player_from_list(player_name)
            if player:
                self.leaderboard.remove_player(player)
            else:
                success = False
        return success

    def submit_score(self, winner_name, loser_name):
        if self.leaderboard.get_player_from_list(winner_name) is None and self.leaderboard.get_player_from_list(loser_name) is None:
            self.leaderboard.add_player(winner_name)
            self.leaderboard.add_player(loser_name)
        else:
            if self.leaderboard.get_player_from_list(winner_name) is None:
                self.leaderboard.add_player(winner_name)
            if self.leaderboard.get_player_from_list(loser_name) is None:
                self.leaderboard.add_player(loser_name)
        self.update_player_position(winner_name, loser_name)

    def update_player_position(self, winner_name, loser_name):
        loser_index = self.leaderboard.players.index(self.leaderboard.get_player_from_list(loser_name))
        winner_index = self.leaderboard.players.index(self.leaderboard.get_player_from_list(winner_name))

        if (winner_index < loser_index):
            return

        winner_player = self.leaderboard.get_player_from_list(winner_name)

        self.leaderboard.remove_player(winner_player)
        self.leaderboard.insert_player_at_index(winner_player, loser_index)

    # def get_leaderboard_players(self):
    #     return self.leaderboard.get_leaderboard_players()

    def find_player(self, player_name):
        return self.leaderboard.get_player_from_list(player_name)

    def get_leaderboard_players(self):
        return self.leaderboard.get_players()

    def initialise_leaderboard(self, players, leaderboard_name):
        print(leaderboard_name)
        self.active_leaderboard_name = leaderboard_name
        self.leaderboard = Leaderboard(leaderboard_name, players)

    def get_active_leaderboard_name(self):
        return self.active_leaderboard_name

    def get_active_leaderboard(self):
        return self.leaderboard
    
    def clear_leaderboard(self):
        return self.leaderboard.clear_players()
