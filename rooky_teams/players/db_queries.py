from .models import Player
import json


def get_roster_queryset():
    return Player.objects.filter(is_in_roster=True)


def add_to_roster(id):
    Player.objects.filter(id=id).update(is_in_roster=True)


def delete_from_roster(id):
    Player.objects.filter(id=id).update(
        is_in_roster=False, team=0)
    

def clear_roster():
    Player.objects.filter(is_in_roster=True).update(
        is_in_roster=False, team=0)


def get_team_queryset(player_ids_json_string):
    id_list = json.loads(player_ids_json_string)
    return Player.objects.filter(id__in=id_list)


def change_team(id):
    team_number = 1 if Player.objects.filter(id=id)[0].team in (0, 2) else 2
    Player.objects.filter(id=id).update(team=team_number)
