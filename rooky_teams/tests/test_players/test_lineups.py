from .. import TestCase, reverse_lazy, Player
from .test_roster import add_players_to_test_db

LINEUPS_URL = reverse_lazy('lineups')


class TestLineUps(TestCase):
    fixtures = ['database.json']

    def test_lineups_page_with_empty_roster(self):
        response = self.client.get(LINEUPS_URL)
        self.assertEqual(response.status_code, 302)

    def test_lineups_page_with_4_players_roster(self):
        add_players_to_test_db()
        Player.objects.all().update(is_in_roster=True)
        response = self.client.get(LINEUPS_URL)
        self.assertEqual(response.status_code, 200)

    def test_lineups(self):
        add_players_to_test_db()
        response = self.client.get(LINEUPS_URL)
        Player.objects.all().update(is_in_roster=True)
        response = self.client.get(LINEUPS_URL)
        team_1 = response.context.get('team_1')
        self.assertEqual(len(team_1), 2)
        team_2 = response.context.get('team_2')
        self.assertEqual(len(team_2), 2)
        self.assertIsInstance(team_1[0], Player)
