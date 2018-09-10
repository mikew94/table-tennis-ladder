class Leaderboard:
    players = []

    def update_leaderboard(self, winner_name, loser_name):
        if winner_name not in players and loser_name not in players:
            new_player(winner_name)
            new_player(loser_name)
        else:
            if winner_name not in ladder:
                new_player(winner_name)
            if loser_name not in ladder:
                new_player(loser_name)
        move_players(winner_name, loser_name)

    def move_players(self, winner_name, loser_name):
        loser_position = players.index(loser_name)
        winner_position = players.index(winner_name)

        if (winner_position < loser_position):
            return

        players.remove(winner_name)
        players.insert(loser_position, winner_name)

    def get_players(self):
        return self.players

    def set_players(self, names):
        self.players = names

    def add_player(player):
        self.players.append(player)