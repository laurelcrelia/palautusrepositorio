class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()
        self.players_by_nationality=[]

    def sorted_points(player):
        return player.goals + player.assists

    def top_scorers_by_nationality(self,nationality):
        for player in self.players:
            if player.nationality == nationality:
                self.players_by_nationality.append(player)       
        sorted_players = sorted(
            self.players_by_nationality,
            reverse=True,
            key=PlayerStats.sorted_points)
        
        return sorted_players
