from .. import TestCase, reverse_lazy, Player


PLAYERS_INDEX_URL = reverse_lazy('players_index')
PLAYER_UPDATE_URL = reverse_lazy('player_update', kwargs=dict(pk=1))
NEW_PLAYER = dict(
    first_name='Test_name_2',
    last_name='Test_surname_2',
    role=2,
    gk_skill=3,
    def_skill=2,
    off_skill=1,
)


class TestPlayerUpdate(TestCase):
    fixtures = ['database.json']

    def test_player_update_page(self):
        response = self.client.get(PLAYER_UPDATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_player_update(self):
        self.assertEqual(Player.objects.all().count(), 1)
        response = self.client.post(PLAYER_UPDATE_URL, NEW_PLAYER)
        self.assertEqual(Player.objects.all().count(), 1)
        last_player = Player.objects.last()
        self.assertEqual(last_player.last_name, NEW_PLAYER['last_name'])
        self.assertEqual(last_player.avg_skill, 2)
        self.assertRedirects(response, PLAYERS_INDEX_URL)
