from .models import Player
import json


def get_roster_queryset():
    return Player.objects.filter(is_in_roster=True)


def add_to_roster(id):
    Player.objects.filter(id=id).update(is_in_roster=True)


def delete_from_roster(id):
    Player.objects.filter(id=id).update(is_in_roster=False)


def clear_roster():
    (
        Player
        .objects
        .filter(is_in_roster=True)
        .update(is_in_roster=False)
    )


def get_team_queryset(player_ids_json_string):
    id_list = json.loads(player_ids_json_string)
    return Player.objects.filter(id__in=id_list)


def add_player_to_team(id, team_number):
    Player.objects.filter(id=id).update(team=team_number)

def change_team(id):
    player = Player.objects.filter(id=id)
    team_number = 1 if player.team in (0, 2) else 2
    player.update(team=team_number)
