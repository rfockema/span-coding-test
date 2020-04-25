import sys


def GetMatchPoints(goals_for, goals_against):
    if goals_for > goals_against:
        return 3, 0
    elif goals_for == goals_against:
        return 1, 1
    else:
        return 0, 3


class LeagueTable():
    teams = dict()
    
    def __init__(self):
        self.teams = dict()

    def AddMatchResults(self, matches):
        for match in matches:
            teams_goals = match.split(', ')
            team1_name = teams_goals[0][0:-2]
            team1_goals = teams_goals[0][-1]
            team2_name = teams_goals[1].rstrip()[0:-2]
            team2_goals = teams_goals[1].rstrip()[-1]
            team1_points, team2_points = GetMatchPoints(
                team1_goals, team2_goals)

            self.UpdatePoints(team1_name, team1_points)
            self.UpdatePoints(team2_name, team2_points)

    def UpdatePoints(self, team, points):
        if team not in self.teams:
            self.teams[team] = 0
        self.teams[team] += points

    def GetOrderedTableList(self):
        return sorted(self.teams.items(), key=lambda name_goal: (-name_goal[1], name_goal[0]))

    def PrintOrderedTable(self):
        i = 1
        rank = 1
        prev_score = -1
        for row in self.GetOrderedTableList():
            team_name = row[0]
            team_score = row[1]

            if prev_score > team_score:
                rank = i

            tail_str = 'pts'
            if team_score == 1:
                tail_str = 'pt'

            print(f'{rank}. {team_name}, {team_score} {tail_str}')
            prev_score = team_score
            i += 1


if __name__ == '__main__':
    league_table = LeagueTable()
    league_table.AddMatchResults(sys.stdin)
    league_table.PrintOrderedTable()
