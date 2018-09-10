class Leaderboard:
    players = []

    def update_leaderboard(self, winner_name, loser_name):
        if winner_name not in self.players and loser_name not in self.players:
            self.add_player(winner_name)
            self.add_player(loser_name)
        else:
            if winner_name not in self.players:
                self.add_player(winner_name)
            if loser_name not in self.players:
                self.add_player(loser_name)
        self.move_players(winner_name, loser_name)

    def move_players(self, winner_name, loser_name):
        loser_position = self.players.index(loser_name)
        winner_position = self.players.index(winner_name)

        if (winner_position < loser_position):
            return

        self.players.remove(winner_name)
        self.players.insert(loser_position, winner_name)

    def get_players(self):
        return self.players

    def set_players(self, names):
        self.players = names

    def add_player(self, player):
        self.players.append(Player)