from player import Player

class Leaderboard:

    def __init__(self, name, players):
        self.name = name
        self.players = []
        for player in players:
            self.players.append(Player(player))

    def get_players(self):
        return self.players

    def set_players(self, players):
        for p in players:
            self.add_player(p)

    def insert_player_at_index(self, winner_player, loser_index):
        self.players.insert(winner_player, loser_index)

    def add_player(self, player_name):
        self.players.append(Player(player_name))

    def remove_player(self, player):
        self.players.remove(player)

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

    def clear_players(self):
        self.players = []