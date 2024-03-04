from .. import TestCase, reverse_lazy, Player
import json

ROSTER_URL = reverse_lazy('roster')


def add_to_roster_url(player_id):
    return reverse_lazy('add_to_roster', kwargs=dict(pk=player_id))


def delete_from_roster_url(player_id):
    return reverse_lazy('delete_from_roster', kwargs=dict(pk=player_id))


CLEAR_ROSTER_URL = reverse_lazy('clear_roster')


def add_players_to_test_db():
    with open('rooky_teams/tests/fixtures/new_player_2.json') as file:
        PLAYER_2 = json.load(file)
    with open('rooky_teams/tests/fixtures/new_player_3.json') as file:
        PLAYER_3 = json.load(file)
    with open('rooky_teams/tests/fixtures/new_player_4.json') as file:
        PLAYER_4 = json.load(file)
    Player.objects.create(**PLAYER_2)
    Player.objects.create(**PLAYER_3)
    Player.objects.create(**PLAYER_4)


class TestRoster(TestCase):
    fixtures = ['database.json']

    def test_roster_page(self):
        response = self.client.get(ROSTER_URL)
        self.assertEqual(response.status_code, 200)

    def test_roster(self):
        add_players_to_test_db()
        Player.objects.filter(id__in=[1, 2, 3]).update(is_in_roster=True)
        player_1, player_2, player_3, player_4 = Player.objects.all()
        response = self.client.get(ROSTER_URL)
        self.assertContains(response, player_1.__str__())
        self.assertContains(response, player_2.__str__())
        self.assertContains(response, player_3.__str__())
        self.assertNotContains(response, player_4.__str__())
        players = response.context.get('object_list')
        self.assertIsInstance(players[0], Player)

    def test_add_to_roster(self):
        add_players_to_test_db()
        self.assertEqual(Player.objects.filter(is_in_roster=True).count(), 0)
        self.client.post(add_to_roster_url(1))
        self.assertEqual(Player.objects.filter(is_in_roster=True).count(), 1)

    def test_delete_from_roster(self):
        add_players_to_test_db()
        self.client.post(add_to_roster_url(1))
        self.assertEqual(Player.objects.filter(is_in_roster=True).count(), 1)
        self.client.post(delete_from_roster_url(1))
        self.assertEqual(Player.objects.filter(is_in_roster=True).count(), 0)

    def test_roster_clear(self):
        response = self.client.get(CLEAR_ROSTER_URL)
        self.assertEqual(response.status_code, 200)
        add_players_to_test_db()
        Player.objects.all().update(is_in_roster=True)
        self.assertEqual(Player.objects.filter(is_in_roster=True).count(), 4)
        self.client.post(CLEAR_ROSTER_URL)
        self.assertEqual(Player.objects.filter(is_in_roster=True).count(), 0)
