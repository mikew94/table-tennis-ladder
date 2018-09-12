from player import Player

class Leaderboard:

    players = []

    def update_leaderboard(self, winner_name, loser_name):
        if self.get_player_from_list(winner_name) is None and self.get_player_from_list(loser_name) is None:
            self.add_player(winner_name)
            self.add_player(loser_name)
        else:
            if self.get_player_from_list(winner_name) is None:
                self.add_player(winner_name)
            if self.get_player_from_list(loser_name) is None:
                self.add_player(loser_name)
        self.move_players(winner_name, loser_name)

    def move_players(self, winner_name, loser_name):
        loser_index = self.players.index(self.get_player_from_list(loser_name))
        winner_index = self.players.index(self.get_player_from_list(winner_name))

        if (winner_index < loser_index):
            return

        winner_player = self.get_player_from_list(winner_name)

        self.players.remove(winner_player)
        self.players.insert(loser_index, winner_player)

    def get_players(self):
        return self.players

    def set_players(self, players):
        for p in players:
            self.add_player(p)

    def add_player(self, player_name):
        self.players.append(Player(player_name))

    def remove_player(self, player):
        self.players.remove(player)

    def clear_table(self):
        self.players = []

    def get_player_from_list(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None
    
    def get_player_index_from_list(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return self.players.index(player)
        return None