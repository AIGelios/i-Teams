from .. import TestCase, reverse_lazy, Player
from .test_roster import add_players_to_test_db
from ...matches.models import Match
from ...players.tools import get_team_ids_json


LINEUPS_URL = reverse_lazy('lineups')


def add_all_test_players_to_roster():
    Player.objects.all().update(is_in_roster=True)


class TestLineUps(TestCase):
    fixtures = ['database.json']

    def test_lineups_page_with_empty_roster(self):
        response = self.client.get(LINEUPS_URL)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('players_index'))

    def test_lineups_page_with_4_players_roster(self):
        add_players_to_test_db()
        add_all_test_players_to_roster()
        response = self.client.get(LINEUPS_URL)
        self.assertEqual(response.status_code, 200)

    def test_lineups(self):
        add_players_to_test_db()
        add_all_test_players_to_roster()
        response = self.client.get(LINEUPS_URL)
        team_1 = response.context.get('team_1')
        self.assertEqual(len(team_1), 2)
        team_2 = response.context.get('team_2')
        self.assertEqual(len(team_2), 2)
        self.assertIsInstance(team_1[0], Player)

    def test_match_creation(self):
        add_players_to_test_db()
        add_all_test_players_to_roster()
        response = self.client.get(LINEUPS_URL)
        team_1 = get_team_ids_json(response.context.get('team_1'))
        team_2 = get_team_ids_json(response.context.get('team_2'))
        response = self.client.post(LINEUPS_URL, team_1, team_2)
        match_2 = Match.objects.get(pk=2)
        self.assertTrue(match_2)
        self.assertEqual(match_2.id, 2)
        self.assertRedirects(response, reverse_lazy(
            'match_details', kwargs=dict(pk=match_2.id)))
