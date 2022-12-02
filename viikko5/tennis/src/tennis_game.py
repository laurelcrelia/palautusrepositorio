class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.str = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 = self.m_score1 + 1
        elif player_name == self.player2_name:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.game_draw()
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.game_position()
        return self.score()

    def game_draw(self):
        if self.m_score1 < 4:
            return f"{self.str[self.m_score1]}-All"
        else:
            return "Deuce"

    def game_position(self):
        minus_result = self.m_score1 - self.m_score2

        if minus_result == 1:
            self.score = f"Advantage {self.player1_name}"
        elif minus_result == -1:
            self.score = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            self.score = f"Win for {self.player1_name}"
        else:
            self.score = f"Win for {self.player2_name}"
        
        return self.score

    def score(self):
        return f"{self.str[self.m_score1]}-{self.str[self.m_score2]}"
