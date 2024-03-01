from .models import Player


def add_to_roster(id):
    Player.objects.filter(id=id).update(is_in_roster=True)


def delete_from_roster(id):
    Player.objects.filter(id=id).update(is_in_roster=True)


def get_team_queryset(id_list):
    return Player.objects.filter(id__in=id_list)


def get_roster_queryset():
    return Player.objects.filter(is_in_roster=True)


def clear_roster():
    (
        Player
        .objects
        .filter(is_in_roster=True)
        .update(is_in_roster=False)
    )
