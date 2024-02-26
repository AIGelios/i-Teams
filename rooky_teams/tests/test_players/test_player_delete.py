from .. import TestCase, reverse_lazy, Player


PLAYERS_INDEX_URL = reverse_lazy('players_index')
PLAYER_DELETE_URL = reverse_lazy('player_delete', kwargs=dict(pk=1))


class TestPlayerUpdate(TestCase):
    fixtures = ['database.json']

    def test_player_update_page(self):
        response = self.client.get(PLAYER_DELETE_URL)
        self.assertEqual(response.status_code, 200)

    def test_player_update(self):
        self.assertEqual(Player.objects.all().count(), 1)
        response = self.client.post(PLAYER_DELETE_URL)
        self.assertEqual(Player.objects.all().count(), 0)
        self.assertRedirects(response, PLAYERS_INDEX_URL)
