from django.test import TestCase
from django.urls import reverse_lazy


TEST_URL = reverse_lazy('homepage')


class HomepageTest(TestCase):
    def test_homepage(self):
        response = self.client.get(TEST_URL)
        self.assertEqual(response.status_code, 200)

    def test_navbar(self):
        response = self.client.get(TEST_URL)
        correct_navbar_links = ('homepage', 'players_index')
        for pattern in correct_navbar_links:
            link = reverse_lazy(pattern)
            self.assertContains(response, link)
