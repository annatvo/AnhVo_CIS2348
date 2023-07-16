class Team:
    def __init__(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        if self.team_wins + self.team_losses == 0:
            return 0.0
        return self.team_wins / (self.team_wins + self.team_losses)

    # TODO: Define print_standing()
    def print_standing(self):
        win_percentage = self.get_win_percentage()
        if win_percentage >= 0.5:
            print(f'Congratulations, Team {self.teamname} has a winning average!')
        else:
            print(f'Team {self.teamname} has a losing average.')


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.teamname = user_name
    team.team_wins = user_wins
    team.team_losses = user_losses

    team.print_standing()
