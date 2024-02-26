from .. import TestCase, reverse_lazy, Player


PLAYERS_INDEX_URL = reverse_lazy('players_index')
PLAYER_CREATE_URL = reverse_lazy('player_create')
NEW_PLAYER = dict(
    first_name='Test_name_2',
    last_name='Test_surname_2',
    role=2,
    gk_skill=5,
    def_skill=4,
    off_skill=3,
)


class TestPlayerCreate(TestCase):
    fixtures = ['database.json']

    def test_player_create_page(self):
        response = self.client.get(PLAYER_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_player_create(self):
        self.assertEqual(Player.objects.all().count(), 1)
        response = self.client.post(PLAYER_CREATE_URL, NEW_PLAYER)
        self.assertEqual(Player.objects.all().count(), 2)
        last_player = Player.objects.last()
        self.assertEqual(last_player.last_name, NEW_PLAYER['last_name'])
        self.assertEqual(last_player.avg_skill, 4)
        self.assertRedirects(response, PLAYERS_INDEX_URL)
