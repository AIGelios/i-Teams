import random
from .db_queries import get_roster_queryset, unteam_all, add_to_team
from .models import Player
import json


def get_team_skill(team: list) -> int:
    '''Take list with Player objects
    and return sum of players avg skill'''
    return round(sum((player.avg_skill for player in team)), 1)


def add_player_to_weak_team(player: Player, teams: dict) -> None:
    '''Take player object and add it
    into team that have lower team skill'''
    team1_skill = get_team_skill(teams['team_1'])
    team2_skill = get_team_skill(teams['team_2'])
    if team1_skill > team2_skill:
        teams['team_2'].append(player)
    elif team1_skill < team2_skill:
        teams['team_1'].append(player)
    else:
        random.choice([teams['team_1'], teams['team_2']]).append(player)


def get_team_ids_json(team: list) -> str:
    '''Take list with Player objects and return list with player IDs
    as JSON string'''
    return json.dumps([x.id for x in team])


class TooFewPlayersError(Exception):
    pass


def generate_balanced_teams(context=dict()):
    """Automaticaly create balanced teams from roster players and return dict:
    {'team_1': [list of Player objects], 'team_2': [list of Player objects]}"""

    teams = {'team_1': [], 'team_2': []}

    roster = list(get_roster_queryset())
    if len(roster) < 2:
        return teams

    random.shuffle(roster)

    # goalkeepers division:
    teams_list = [teams['team_1'], teams['team_2']]
    random.shuffle(teams_list)
    for team in teams_list:
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
        add_player_to_weak_team(best_forward, teams)

    # defenders division:
    defenders = [player for player in roster if player.role in (1, 2)]
    while defenders:
        max_skill = max([player.def_skill for player in defenders])
        best_defender = random.choice(
            [player for player in defenders if player.def_skill == max_skill]
        )
        defenders.remove(best_defender)
        roster.remove(best_defender)
        add_player_to_weak_team(best_defender, teams)
    context.update(teams)    
    return teams


def generate_balanced_teams_v2():
    """Automaticaly create balanced teams from roster players and return dict:
    {'team_1': [list of Player objects], 'team_2': [list of Player objects]}"""

    teams = {'team_1': [], 'team_2': []}
    roster = list(get_roster_queryset())
    random.shuffle(roster)
    if len(roster) < 2:
        return teams
    

    # goalkeepers division:
    teams_list = [teams['team_1'], teams['team_2']]
    random.shuffle(teams_list)
    for team in teams_list:
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
        add_player_to_weak_team(best_forward, teams)

    # defenders division:
    defenders = [player for player in roster if player.role in (1, 2)]
    while defenders:
        max_skill = max([player.def_skill for player in defenders])
        best_defender = random.choice(
            [player for player in defenders if player.def_skill == max_skill]
        )
        defenders.remove(best_defender)
        roster.remove(best_defender)
        add_player_to_weak_team(best_defender, teams)
    for x in teams['team_1']:
        x.update(team=1)
