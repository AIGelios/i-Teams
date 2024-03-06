from .models import Match
import datetime
import json


def create_match(team_1_json, team_2_json):
    return Match.objects.create(
        team_1_ids=team_1_json,
        team_2_ids=team_2_json,
        match_date=datetime.date.today(),
        description='',
    )


def get_player_matches(player_id):
    all_matches = Match.objects.all().order_by('-match_date')
    player_matches = []
    for match in all_matches:
        if player_id in json.loads(match.team_1_ids):
            player_matches.append(match)
        elif json.loads(match.team_2_ids):
            player_matches.append(match)
    return player_matches
