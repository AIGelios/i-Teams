from .. import TestCase, reverse_lazy, Player
from ...matches.models import Match


MATCHES_INDEX_URL = reverse_lazy('matches_index')
MATCH_1_DETAILS_URL = reverse_lazy('match_details', kwargs=dict(pk=1))
MATCH_1_UPDATE_URL = reverse_lazy('match_update', kwargs=dict(pk=1))
MATCH_1_DELETE_URL = reverse_lazy('match_delete', kwargs=dict(pk=1))


class TestMatches(TestCase):
    fixtures = ['database.json']

    def test_matches_index(self):
        self.assertEqual(Match.objects.all().count(), 1)
        response = self.client.get(MATCHES_INDEX_URL)
        self.assertEqual(response.status_code, 200)
        matches_on_page = response.context.get('object_list').all()
        self.assertEqual(matches_on_page.count(), 1)
        match = matches_on_page.last()
        self.assertEqual(
            (match.id, match.team_1_goals, match.team_2_goals),
            (1, 5, 4),
        )

    def test_match_details(self):
        response = self.client.get(MATCH_1_DETAILS_URL)
        self.assertEqual(response.status_code, 200)
        match = response.context['match']
        self.assertEqual(match, Match.objects.all().first())
        player = Player.objects.get(id=1)
        self.assertContains(response, player.__str__())

    def test_match_delete(self):
        self.assertEqual(Match.objects.all().count(), 1)
        response = self.client.get(MATCH_1_DELETE_URL)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(MATCH_1_DELETE_URL)
        self.assertEqual(Match.objects.all().count(), 0)
        self.assertRedirects(response, MATCHES_INDEX_URL)

    def test_match_update(self):
        self.assertEqual(Match.objects.all().count(), 1)
        response = self.client.get(MATCH_1_UPDATE_URL)
        self.assertEqual(response.status_code, 200)
        match = response.context.get('match')
        match.team_1_goals = 1
        match.team_2_goals = 1
        response = self.client.post(MATCH_1_UPDATE_URL, match.__dict__)
        self.assertEqual(Match.objects.all().count(), 1)
        match_1 = Match.objects.get(pk=1)
        self.assertEqual(match_1.team_1_goals, 1)
        self.assertEqual(match_1.team_2_goals, 1)
        self.assertRedirects(response, MATCH_1_DETAILS_URL)
