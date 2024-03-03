import random
from .db_queries import get_roster_queryset
from .models import Player
import json


def get_team_skill(team: list) -> int:
    '''Take list with Player objects
    and return sum of players avg skill'''
    return sum((player.avg_skill for player in team))


def add_player_to_weak_team(
    player: Player,
    team1: list,
    team2: list,
) -> None:
    '''Take player object and add it
    into team that have lower team skill'''
    team1_skill = get_team_skill(team1)
    team2_skill = get_team_skill(team2)
    if team1_skill > team2_skill:
        team2.append(player)
    elif team1_skill < team2_skill:
        team1.append(player)
    else:
        random.choice([team1, team2]).append(player)


def generate_balanced_teams():
    """Automaticaly create balanced teams from roster players and return dict:
    {'team_1': [list of Player objects], 'team_2': [list of Player objects]}"""

    roster = list(get_roster_queryset())
    if not roster:
        return {'team_1': [], 'team_2': []}

    random.shuffle(roster)

    # goalkeepers division:
    team_1, team_2 = [], []
    teams = [team_1, team_2]
    random.shuffle(teams)
    for team in teams:
        best_goalkeeper = max(roster, key=lambda x: x.gk_skill)
        roster.remove(best_goalkeeper)
        team.append(best_goalkeeper)

    # forwards division:
    forwards = [player for player in roster if player.role == 3]
    while forwards:
        max_skill = max([player.frw_skill for player in forwards])
        best_forward = random.choice(
            [player for player in forwards if player.frw_skill == max_skill]
        )
        forwards.remove(best_forward)
        roster.remove(best_forward)
        add_player_to_weak_team(best_forward, team_1, team_2)

    # defenders division:
    defenders = [player for player in roster if player.role in (1, 2)]
    while defenders:
        max_skill = max([player.def_skill for player in defenders])
        best_defender = random.choice(
            [player for player in defenders if player.def_skill == max_skill]
        )
        defenders.remove(best_defender)
        roster.remove(best_defender)
        add_player_to_weak_team(best_defender, team_1, team_2)
    return {'team_1': team_1, 'team_2': team_2}


def get_team_ids_json(team: list) -> str:
    '''Take list with Player objrcts and return list with player IDs
    as JSON string'''
    return json.dumps([x.id for x in team])

