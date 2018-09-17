from controllers.leaderboardcontroller import LeaderboardController

class InputRouter():

    def __init__(self, leaderboard_controller):
        self.leaderboard_controller = leaderboard_controller

    def add_players(self, args):
        if len(args) >= 1 and len(args) < 6:
            players_not_added = self.leaderboard_controller.add_players(args)
            if len(players_not_added) == 0:
                if len(args) == 2:
                    return "> Player has been added: " + args[1]
                else:
                    return "> Players have been added: " + str(args[1:])
            else:
                return "! These players could not be added: " + str(players_not_added)
        else:
            return None

    def remove_players(self, args):
        if len(args) >= 1 and len(args) < 6:
            players_not_removed = self.leaderboard_controller.remove_players(args[1:])
            if len(players_not_removed) != "0":
                if len(args) == 2:
                    return "> Player has been removed: " + args
                else:
                    return "> Players have been removed: " + str(args[1:])
            else: 
                return "! These players could not be removed: " + str(players_not_removed)

    def clear_leaderboard(self):
        self.leaderboard_controller.clear_leaderboard()

    def submit_players_score(self, args):
        if len(args) == 2 and args[0] != args[1]:
            self.leaderboard_controller.submit_score(args[0], args[1])
            return "> Score: %s beat %s" % (args[0], args[1])
        else:
            return None

    def find_player(self, args):
        if len(args) == 2:
            player_index = self.leaderboard_controller.find_player(args[1])
            if player_index:
                return "> %s is at rank #%s" % (args[1].capitalize(), player_index)
            else:
                return "! Player %s could not be found in the leaderboard" % (args[1])
        else:
            return None

    # def show_leaderboard(self):
    #     return leaderboard_controller.get_leaderboard_players()

    def create_leaderboard(self, args):
        if len(args) == 2:
            success = self.leaderboard_controller.create_leaderboard(args[1])
            if success:
                leaderboard_controller.save_active_leaderboard_name(args[1])
                return "Table " + args[1] + " has been successfully created added"
            else:
                return "The table already exists, please choose different name"
        else:
            return None

    def delete_leaderboard(self, args):
        if len(args) == 2:
            success = self.leaderboard_controller.delete_leaderboard(args[1])
            if success:
                return "> Entered leaderboard has been deleted"
            else:
                return "! Could not find supplied leaderboard to delete"
        else:
            return None

    def change_active_leaderboard(self, args):
        if len(args) == 2:
            success = self.leaderboard_controller.change_leaderboard(args[1])
            if success:
                return "> Active leaderboard changed to " + args[1]
            else:
                return "! Could not change the active leaderboard to supplied name. Try entering a valid name"
        else:
            return None

    def show_active_leaderboard(self):
        return self.leaderboard_controller.get_active_leaderboard_name()