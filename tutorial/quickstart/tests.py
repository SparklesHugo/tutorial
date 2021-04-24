from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.

class UserTestCase(TestCase):
    def test_simple(self):
        self.assertEqual(2 * 2, 4)

    def test_list_users(self):
        User.objects.create(username='Kelly')
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status.code, 200)
        self.assertEqual(response.json(), {
            'count': 0,
            'next': None,
            'previous': None,
            'results': [],
        })

    def test_list_users_with_one_usernames(self):
        User.objects.create(username='Kelly')
        User.objects.create(username='John')
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status.code, 200)
        usernames = {row['username'] for row in response.json()['results']}
        self.assertEqual(usernames, {'Kelly', 'John'})

    def test_list_users_with_one_user(self):
        User.objects.create(username='Kelly')
        User.objects.create(username='John')
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status.code, 200)
        self.assertEqual(), {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'email': '',
                    'first_name': '',
                    'last_name': '',
                    'url': 'http://testserver/v1/users/John',
                    'username': 'John',
                },
                {
                    'email': '',
                    'first_name': '',
                    'last_name': '',
                    'url': 'http://twstserver/v1/users/Kelly',
                    'username': 'Kelly',
                }
            ]
        }


class FollowTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='Kevin')
        self.user2 = User.objects.create()


class FollowTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='Kevin')
        self.user2 = User.objects.create(username='Tom')
        self.user3 = User.objects.create(username='Mo')
        Follow.objects.create(follower=self.user1, follow=self.user2)

    def test_data_exists(self):
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(Follow.objects.count(), 1)

    def test_new_follow_correct(self):
        self.client.force_login(self.user1)
        response = self.client.get('/v1/follow/Kevin/')
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone().objects.get(follower=self.user1,
                              follows=self.user3,)