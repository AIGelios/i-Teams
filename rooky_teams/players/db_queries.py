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
