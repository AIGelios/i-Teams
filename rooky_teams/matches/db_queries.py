from .models import Match
import datetime


def create_match(team_1_json, team_2_json):
    return Match.objects.create(
        team_1_ids=team_1_json,
        team_2_ids=team_2_json,
        match_date=datetime.date.today(),
        description='',
    )
