from random import shuffle, choice
from .db_queries import get_roster_queryset


def get_total_skill(team):
    return sum([x.avg_skill for x in team])


def add_player_to_weaker_team(player, team1, team2):
    team1_skill = get_total_skill(team1)
    team2_skill = get_total_skill(team2)
    if team1_skill > team2_skill:
        team2.append(player)
    elif team1_skill < team2_skill:
        team1.append(player)
    else:
        choice([team1, team2]).append(player)


def get_auto_created_teams():
    """Automaticaly create balanced teams"""
    orange_team, blue_team = [], []
    roster = get_roster_queryset()
    if not roster:
        return orange_team, blue_team
    shuffle(roster)

    # goalkeepers division:
    teams = [orange_team, blue_team]
    shuffle(teams)
    for team in teams:
        best_goalkeeper = max(
            roster,
            key=lambda x: x.gk_skill.value
        )
        roster.remove(best_goalkeeper)
        team.append(best_goalkeeper.id)

    # forwards division:
    forwards = [x for x in roster if x.role_id == 3]
    while forwards:
        max_skill = max(
            [x.off_skill.value for x in forwards])
        best_forward = choice(
            [x for x in forwards if x.off_skill.value == max_skill]
        )
        forwards.remove(best_forward)
        roster.remove(best_forward)
        add_player_to_weaker_team(
            best_forward, orange_team, blue_team
        )

    # defenders division:
    defenders = [x for x in roster if x.role_id in (2, 1)]
    while defenders:
        max_skill = max(
            [x.def_skill.value for x in defenders]
        )
        best_defender = choice(
            [x for x in defenders if x.def_skill.value == max_skill]
        )
        defenders.remove(best_defender)
        roster.remove(best_defender)
        add_player_to_weaker_team(
            best_defender, orange_team, blue_team
        )
    return {'orange': orange_team, 'blue': blue_team}
