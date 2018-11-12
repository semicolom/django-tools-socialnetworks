from djtools.socialnetworks.models import SocialNetwork
from django.test import TestCase


class SocialNetworkTestCase(TestCase):
    def setUp(self):
        self.twitter = SocialNetwork.objects.create(
            social_network='twitter',
            account_id='test'
        )
        self.github = SocialNetwork.objects.create(
            social_network='github',
            account_id='test'
        )

    def test_get_choices(self):
        choices = SocialNetwork.get_choices()
        expected_choices = [
            ('facebook', "Facebook"),
            ('instagram', "Instagram"),
            ('twitter', "Twitter"),
            ('youtube', "YouTube"),
            ('vimeo', "Vimeo"),
            ('github', "GitHub"),
        ]
        self.assertEqual(choices, expected_choices)

    def test_get_social_networks(self):
        self.assertListEqual(
            list(SocialNetwork.get_social_networks()),
            [self.twitter, self.github]
        )

    def test_info(self):
        self.assertDictEqual(
            self.github.info,
            {
                'name': 'GitHub',
                'link': 'https://github.com/',
                'icon': 'github',
            }
        )

    def test_get_name(self):
        self.assertEqual(self.github.get_name(), "GitHub")

    def test_get_link(self):
        self.assertEqual(self.github.get_link(), "https://github.com/test")

    def test_get_icon(self):
        self.assertEqual(self.github.get_icon(), "github")

    def test_add_non_existing_social_network(self):
        test = SocialNetwork.objects.create(
            social_network='test',
            account_id='test'
        )

        self.assertEqual(test.get_name(), None)
