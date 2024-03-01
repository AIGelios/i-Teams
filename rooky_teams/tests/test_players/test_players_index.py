from .. import TestCase, reverse_lazy, Player


class TestPlayersIndex(TestCase):
    fixtures = ['database.json']

    def test_players_page(self):
        response = self.client.get(reverse_lazy('players_index'))
        self.assertEqual(response.status_code, 200)

    def test_players_index(self):
        response = self.client.get(reverse_lazy('players_index'))
        players = response.context.get('object_list')
        player = Player.objects.get(id=1)
        self.assertIn(player, players)
        self.assertContains(response, player.__str__())
        self.assertContains(response, player.role_name)
