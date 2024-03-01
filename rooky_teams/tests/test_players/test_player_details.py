from .. import TestCase, reverse_lazy, Player


PLAYER_DETAILS_URL = reverse_lazy('player_details', kwargs=dict(pk=1))


class TestPlayerDetails(TestCase):
    fixtures = ['database.json']

    def test_player_update_page(self):
        response = self.client.get(PLAYER_DETAILS_URL)
        self.assertEqual(response.status_code, 200)
        player_in_db = Player.objects.get(pk=1)
        player_on_page = response.context.get('player')
        self.assertEqual(player_in_db, player_on_page)
        self.assertContains(response, player_in_db.__str__())
        self.assertContains(response, player_in_db.role_name)
